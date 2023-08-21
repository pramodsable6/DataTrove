```Spark Cluster Managers:```
1. local[n]
2. YARN
3. Kubernetes
4. Mesos
5. Standalone

```Execution Modes -> Execution Tools:```
1. Client -> IDE, Notebooks
2. Cluster -> Submit

```Transformations:```
1. Narrow Transformations - no shuffling needed (e.g. select(), filter(), withColumn(), drop())
2. Wide Transformations - shuffling needed (such as groupBy(), distinct(), join(), agg(), etc.)
- Lazily evaluated
- https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations

```Actions:```
- Not lazily evaluated
- https://spark.apache.org/docs/latest/rdd-programming-guide.html#actions
- Used to trigger some work(Job)
- e.g. read(), write(), collect(), take(), count(), etc.

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

```Optimization teechniques```
- Use DataFrames over RDDs since its queries can be optimized by Spark's Catalyst Optimizer
- Broadcast the smaller DataFrame to all the nodes
- Use cache() method to cache the intermediate transformations
- Reduce expensive shuffle operations - wide transformations
- Optimize the joins by repartitioning(redistributing) the data based on joining column

```Spark Config Order of Precedence```
1. Any values defined in spark-defaults.conf will be read first
2. Followed by those supplied on the command line with spark-submit
3. And finally those set via SparkSession in the spark Application
   ```
   spark.conf.get("spark.sql.shuffle.partitions")
   spark.conf.set("spark.sql.shuffle.partitions", 10)
   ```
