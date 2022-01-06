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
1. Narrow Transformations - no shuffling needed
2. Wide Transformations - shuffling needed (such as group by, distinct, etc.)
- Lazily evaluated
- https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations

```Actions:```
- Not lazily evaluated
- https://spark.apache.org/docs/latest/rdd-programming-guide.html#actions
