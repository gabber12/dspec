class Dataset(object):
    def __init__(self):
        self.registered_metrics = []
        pass

    def compute_metrics(self):
        """
            aggs: min, max, avg, sum, cardinality, quantiles
            columns: [column_name1, column_nm2]
        """
        raise NotImplementedError

    def register_metrics(self, *args):
        self.registered_metrics = list(args)

    def expect(self, *args):
        results = {}
        for expectations in args:
            results[str(expectations)] = expectations.test(self)
        return results


class PandasDataSet(Dataset):
    def __init__(self, df):
        self.df = df
    
    def compute_metrics(self):
        pass
    
    def count_null(self, column):
        return self.df[column].isna().sum()

    def count_rows(self):
        return self.df.shape[0]

    def count_columns(self):
        return self.df.shape[1]

    def count_distinct(self, column):
        return self.df[column].nunique()

    def column_aggregate(self, aggs_by_columns):
        pass
