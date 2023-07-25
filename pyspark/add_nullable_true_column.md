> Context
- When you add a new column having constant value using `lit()` the default nullable property is set to **false**.
- This can be altered by using following code -

> Code
```python
df.withColumn('region_id', when(lit(True), lit(1))).printSchema()
```

> O/P -
```shell
root
 |-- _c0: string (nullable = true)
 |-- _c1: string (nullable = true)
 |-- _c2: string (nullable = true)
 |-- _c3: string (nullable = true)
 |-- _c4: string (nullable = true)
 |-- _c5: string (nullable = true)
 |-- _c6: string (nullable = true)
 |-- _c7: string (nullable = true)
 |-- region_id: integer (nullable = true)
```
