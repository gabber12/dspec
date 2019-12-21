import pandas as pd
from dspec import *





if __name__ == '__main__':
    df = pd.read_csv('~/Notebooks/atlas_city_codes/city_codes.csv')
    # spec = Specification.pandas(df) \
    # .expect(NullPercentage('o_city'), LessThan(), 10) \
    # .expect(NullPercentage('o_state'), LessThan(), 10) \
    # .expect(CountRows(), Equals(), 6448) \
    # .expect(CountColumns(), Equals(), 6) \
    # .expect(Cardinality('o_city') ,LessThan(), 8000)
    spec = Specification.pandas(df) \
    .loadSuite('suite.yml')
    result = spec.run()
    # print(spec.serialize(file_name='suite.yml'))
    result.pretty_print()
    