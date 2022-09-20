from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('abc').getOrCreate()

df1 = spark.read.format('csv').load('abcd/pqrs/filename.csv')
# your code
df1.write.format('csv').save('path_to_file/filename2.csv')

