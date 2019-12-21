import yaml
from tabulate import tabulate
from .dataset import PandasDataSet
import inspect
import pandas as pd

class DataSpec(object):
    def test(self, dataset):
        raise NotImplementedError


class MetricConstantSpec(DataSpec):
    def __init__(self, metric, op, value):
        self.metric = metric
        self.op = op
        self.value = value

    def __str__(self):
        return "assert %s %s %s" % (str(self.metric), str(self.op), str(self.value))

    def test(self, dataset):
        # print(self.op, self.metric.get(dataset),", ", self.value)
        return self.op.test(self.metric.get(dataset),  float(self.value)) 
class UnarySpec(DataSpec):
    def __init__(self, metric):
        self.metric = metric
        

    def __str__(self):
        return "assert %s" % (str(self.metric))

    def test(self, dataset):
        # print(self.op, self.metric.get(dataset),", ", self.value)
        return self.metric.get(dataset)
class Registry(object):
    def __init__(self):
        self.operators = {}
        self.metrics = {}
    def registerOp(self, str_op, op):
        self.operators[str_op] = op
    def registerMetric(self, str_metric, metric):
        self.metrics[str_metric] = metric
    def createOp(self, op):
        if op not in self.operators:
            raise Exception("Unknown op")
        return self.operators[op]()
    def createMetric(self, metric, args):
        if metric not in self.metrics:
            raise Exception("Unknown metric")
        return self.metrics[metric](*args)
registry = Registry()
class Specification(object):
    def __init__(self):
        
        self.specs = []
    
    def loadSuite(self, file_name):
        f = open(file_name)
        content = f.read()
        spec = yaml.load(content)
        for rule in spec['rules']:
            tokens = rule.split(" ")[1:]
            value = tokens[-1]
            op = tokens[-2]
            metric = tokens[0]
            args = [arg.replace("`", "") for arg in tokens[1:-2]]
            # print(registry.createMetric(metric, args))
            # print(op)
            # print(registry.createOp(op))
            self.specs.append(MetricConstantSpec(registry.createMetric(metric, args), registry.createOp(op), value))
        return self
            
    def expect(self, metric, op=None, value = None):
        if self.specs is None:
            self.specs = []
        if op is None:
            self.specs.append(UnarySpec(metric() if inspect.isclass(metric) else metric))   
            return self 
        self.specs.append(MetricConstantSpec(metric() if inspect.isclass(metric) else metric , op() if inspect.isclass(op) else op, value))
        return self

    def run(self, df):
        if isinstance(df, pd.DataFrame):
            ds = PandasDataSet(df)
        return SpecRun(ds.expect(*self.specs))
    def test(self, df):
        if isinstance(df, pd.DataFrame):
            ds = PandasDataSet(df)
        failing = SpecRun(ds.expect(*self.specs)).get_failing()
        if len(failing) > 0:
            raise Exception("Failing Specs %s" % failing)
        return failing

    def serialize(self, **kwargs):
        rules = [str(spec) for spec in self.specs]
        suite = {'rules': rules}
        specs = yaml.dump(suite)
        if 'file_name' in kwargs:
            f = open(kwargs['file_name'], 'w')
            f.write(specs)
            f.close()
        return specs


class SpecRun(object):
    def __init__(self, results):
        self.results = results
    def get_failing(self):
        return [k for k, v in self.results.items() if not v]
            
    def print(self):
        header = "Spec Run results"
        print(header+"\n"+"="*len(header)+"\n")
        print(tabulate([[k, str(v)]
                        for k, v in self.results.items()], headers=['Rule', 'Result']))
