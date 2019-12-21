from .specs import *
class Metric(object):
    def __init__(self):
        pass



class NullPercentage(Metric):
    def __init__(self, column_name, percentage = 0):
        self.column_name = column_name
        self.percentage = percentage
    def __str__(self):
        return "NullPercentageFor `%s`"%(self.column_name)
    def get(self, dataset):
        count_null = dataset.count_null(self.column_name)
        count_rows = dataset.count_rows()
        return (count_null*100.0)/float(count_rows)

class Cardinality(Metric):
    def __init__(self, column_name):
        self.column_name = column_name
        
    def __str__(self):
        return "CountUnique `%s`"%(self.column_name)

    def get(self, dataset):
        return dataset.count_distinct(self.column_name)
class CountRows(Metric):
    def __init__(self, *args):
        pass
    def __str__(self):
        return "CountRows"
    def get(self, dataset):
        return dataset.count_rows() 

class CountColumns(Metric):
    def __init__(self, *args):
        pass
    def __str__(self):
        return "CountColumns"
    def get(self, dataset):
        return dataset.count_columns()

registry.registerMetric("NullPercentageFor", NullPercentage)
registry.registerMetric("CountUnique", Cardinality)
registry.registerMetric("CountRows", CountRows)
registry.registerMetric("CountColumns", CountColumns)
