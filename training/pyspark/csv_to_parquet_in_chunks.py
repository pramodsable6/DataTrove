# How to convert large CSV file which does not fit into your machine/cluster memory to Parquet without scaling up
# This code needs to be tested with exact scenario mentioned in the question, got this answer from Bing chat

from pyspark.sql.functions import monotonically_increasing_id, col

# Read the CSV file
df = spark.read.option("header", "true").csv("./input/spotify-2023.csv")

# Add row_num column for chunking
df = df.withColumn("row_num", monotonically_increasing_id())
chunk_size = 100
offset = 0

while True:
    chunk_df = df.filter((col("row_num") >= offset) & (col("row_num") < offset + chunk_size))
    if chunk_df.count() == 0:
        break
    chunk_df.write.mode("append").parquet("./output/")    
    offset += chunk_size
