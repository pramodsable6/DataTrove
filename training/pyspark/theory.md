```Spark Cluster Managers:```
1. local[n]
2. YARN
3. Kubernetes
4. Mesos
5. Standalone

```Execution Modes -> Execution Tools:```
1. Client -> IDE, Notebooks
2. Cluster -> Submit

```Serialization and de-serialization:```
Serialization is the process of converting objects into bytes to transfer them between nodes or store them in a file/memory buffer. In Spark, serialization is crucial for transferring objects between different nodes in a distributed cluster.
Serialization is used by Spark for a variety of operations, including:
 - RDD transformations: When an RDD is transformed, the objects in the RDD are serialized and sent to the executors where the transformation is performed.
 - Broadcast variables: Broadcast variables are shared by all executors in a cluster. When a broadcast variable is created, it is serialized and sent to all executors.
 - Accumulators: Accumulators are used to aggregate data across a cluster. When an accumulator is updated, the update is serialized and sent to all executors.

```Transformations:```
1. Narrow Transformations - no shuffling needed (e.g. select(), filter(), withColumn(), drop())
2. Wide Transformations - shuffling needed (such as groupBy(), distinct(), join(), agg(), etc.)
- Lazily evaluated
- https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations

```Actions:```
- Not lazily evaluated
- https://spark.apache.org/docs/latest/rdd-programming-guide.html#actions
- Used to trigger some work(Job)
- e.g. write(), collect(), take(), count(), etc.

```Hierarchies:```
1. Driver > Worker > Executer
2. Jobs > Stages > Tasks
- Job - Each action creates a job.
- Stage
  - Spark driver creates a logical plan for each job and breaks down the plan into stages at each wide dependency transformation.
  - If there are n wide transformations there will be n + 1 stages.
  - Stages can only run sequentially as data from 1 stage is input for the next stage. The data from 1 stage is shared with other by shuffle/sort operation.
- Task
  - Each stage can be executed as number of parallel tasks. The no. of tasks that can run in parallel = no. of input partitions.
  - Task is the smallest unit of work which is executed on executers. Executer needs dataframe partition and code API to perform the task.

```collect()```
- Collect pulls data to spark driver. This is useful only when you are working with filtered dataset.
- Running collect() on large dataset can result in out of memory error.

```Optimization techniques```
- Use DataFrames over RDDs since its queries can be optimized by Spark's Catalyst Optimizer
- Improving the performance of Joins 
  - Broadcast Hash Join - Broadcast the smaller DataFrame to all the nodes
  - Shuffle Sort Merge Join - We can eliminate exchange step from this join if we create **partitioned buckets** `using bucketBy()` for common sorted keys or columns on which we want to perform frequent equi joins
- Use cache() or persist() method to cache the intermediate transformations
- Reduce expensive shuffle operations - wide transformations
- `repartition()` the dataframe where necessary to increase parallelism
- Enable dynamic resource allocation
  ```
  from pyspark.sql import SparkSession
  spark = SparkSession.builder \
      .appName("My app") \
      .config("spark.dynamicAllocation.enabled", "true") \
      .config("spark.dynamicAllocation.minExecutors", 1) \
      .config("spark.dynamicAllocation.maxExecutors", 10) \
      .config("spark.shuffle.service.enabled", "true") \
      .getOrCreate()
  ```

```What is data skewness?```
- Data skewness is a common issue that can significantly impact the performance and efficiency of Apache Spark, a popular big data processing framework. 
- Data skewness occurs when the distribution of data across partitions is uneven, leading to some partitions having much larger data sizes than others. 
- This can result in certain tasks taking significantly longer to complete, causing performance bottlenecks and delaying overall job completion times.
- Data skewness can occur in various scenarios, such as when the input data has skewed keys or values, when the data is unevenly distributed across partitions, or when there are imbalanced operations like joins or aggregations.
- Data Partitioning:
Data partitioning is a key strategy in Spark for distributing data across multiple worker nodes for parallel processing. Proper data partitioning can help achieve a balanced distribution of data across partitions, reducing the chances of data skewness. Some common data partitioning techniques include:
  - Hash Partitioning: In hash partitioning, data is partitioned based on the hash value of a specific column. This ensures that the data is distributed evenly across partitions, reducing the chances of data skewness.
  - Range Partitioning: In range partitioning, data is partitioned based on a specific range of values of a particular column. This can help distribute data evenly across partitions, especially when the data has a known range or distribution.
  - Custom Partitioning: Custom partitioning allows users to define their own partitioning logic based on the specific characteristics of their data. This can help optimize data distribution and minimize data skewness.

```How to mitigate the data skewness caused by repartitioning the data on specific column?```  
- Salting is a technique in Spark that adds random values to data to distribute it more evenly across partitions. This technique is used to mitigate the effects of skewed data. Salting can result in a more balanced workload and improved performance.  
- Salting works by adding a random component, or "salt", to the data. This salt is concatenated to the driving key of the data. When reshuffling occurs, the data distribution is fairly even. This ensures that each task on its respective partition takes nearly the same amount of time.  
- Salting is usually good to adopt for wide transformations that require shuffling, like join operations.
- Salting is unrelated to any of the keys. This is a significant benefit because you don't have to worry about some keys with similar contexts having the same value again.
```
import pyspark.sql.functions as F
df = df.withColumn('salt', F.rand())
df = df.repartition(8, 'salt')
# To check if our salt worked, we can use groupBy -
df.groupBy(F.spark_partition_id()).count().show()
```

```Repartition vs Coalesce```
Repartition creates new partitions and shuffles all the data. Coalesce uses existing partitions to avoid a full shuffle.

```How to deal with small file problem?```   
1. Reduce the number of shuffle partitions   
```spark.conf.set("spark.sql.shuffle.partitions", 10)```
2. Combine small files into larger files   
```spark.conf.set("spark.sql.shuffle.consolidateFiles", 10)```
3. Use a different file format   
```df.write.parquet("/path/to/parquet/files")```
4. Use a different storage system   
```df.write.hdfs("/path/to/hdfs/files")```

```Spark Config Order of Precedence```
1. Any values defined in spark-defaults.conf will be read first
2. Followed by those supplied on the command line with spark-submit
3. And finally those set via SparkSession in the spark Application
   ```
   spark.conf.get("spark.sql.shuffle.partitions")
   spark.conf.set("spark.sql.shuffle.partitions", 10)
   ```
