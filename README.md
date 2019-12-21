Dspec 
=====
DSpec is a way to write specification on data.

Usage
-----

Create specifications by code
```python
 Specification.pandas(df) \
    .expect(NullPercentage('o_city'), LessThan(), 10) \
    .expect(NullPercentage('o_state'), LessThan(), 10) \
    .expect(CountRows(), Equals(), 6448) \
    .expect(CountColumns(), Equals(), 6) \
    .expect(Cardinality('o_city') ,LessThan(), 8000)
```
or Load from a spec file
```python
Specification.pandas(df) \
    .loadSuite('suite.yml')
```