Dspec 
=====
DSpec is a way to write specification on data.
DSpec supports currently pandas dataframe, plans to support spark is work in progress
Specifications look like these

```yaml
- assert NullPercentageFor `o_city` < 10
- assert NullPercentageFor `o_state` < 10
- assert CountRows == 6448
- assert CountColumns == 6
- assert CountUnique `o_city` < 8000
```

Usage
-----

Create specifications by code
```python
specs = Specification() \
    .expect(NullPercentage('o_city'), LessThan, 10) \
    .expect(NullPercentage('o_state'), LessThan, 10) \
    .expect(CountRows, Equals, 6448) \
    .expect(CountColumns, Equals, 6) \
    .expect(Cardinality('o_city') ,Equals, 8000)

# Dump specifications to file
specs.serialize(file_name='suite.yml')

```
or Load from a spec file
```python

specs = Specification() \
    .loadSuite('suite.yml')

```

Test Specifications on pandas dataframe
```python

specs.test(df)

Exception: Failing Specs ['assert CountUnique `o_city` == 8000']
    
```

or print results
```python

results = specs.run(df)
results.print()
    
```