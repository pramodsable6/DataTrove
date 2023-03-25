- Overwrite:
```python
spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")
df.write.mode("overwrite")\
    .format("parquet")\
    .save(output_dir)
```

- _SUCCESS completeness indicator:
```python
df.write.mode("overwrite")\
    .option("mapreduce.fileoutputcommitter.marksuccessfuljobs", "true")\
    .format("parquet")\
    .save(output_dir)
```
