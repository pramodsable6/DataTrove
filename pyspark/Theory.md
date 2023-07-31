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

```collect()```
- Collect pulls data to spark driver. This is useful only when you are working with filtered dataset.
- Running collect() on large dataset can result in out of memory error.

```Optimization teechniques```
- Use DataFrames over RDDs 
- Broadcast the smaller DataFrame to all the nodes
- Use cache() method to cache the intermediate transformations
- Reduce expensive shuffle operations - wide transformations
- Optimize the joins by repartitioning(redistributing) the data based on joining column
