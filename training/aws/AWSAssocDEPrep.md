`Athena`
- Partition projection with Amazon Athena -  
   https://docs.aws.amazon.com/athena/latest/ug/partition-projection.html
- Access to Amazon S3 from Athena -  
  https://docs.aws.amazon.com/athena/latest/ug/s3-permissions.html

`S3`
- UltraWarm storage for Amazon OpenSearch Service -  
   https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ultrawarm.html

- S3 storage classes -  
   https://aws.amazon.com/s3/storage-classes/

- S3 object lambda -  
   https://aws.amazon.com/s3/features/object-lambda/

`Lambda`
- Lambda Reserved vs Provisioned concurrency -  
   https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html

`Redshift`
- Redshift System tables and views reference -  
   https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_system-tables.html

- Redshift concurrency scaling for spiky workloads

- Federated queries for querying data from multiple remote sources  
   https://docs.aws.amazon.com/redshift/latest/gsg/federated-query.html

`Eventbridge`  
- When you create the EventBridge event trigger, you can optionally specify batch conditions. If you specify batch conditions, you must specify the batch size (number of events), and can optionally specify a batch       window (number of seconds). The default and maximum batch window is 900 seconds (15 minutes). The batch condition that is met first starts the workflow. The batch window starts when the first event arrives. If you     don't specify batch conditions when creating a trigger, the batch size defaults to 1.

`EMR`  
- Why does aws emr file system need dynamodb access?  
   - Metadata Storage: EMRFS uses DynamoDB to store metadata about the files in Amazon S3. This metadata helps ensure that the file system has a consistent view of the data, even when multiple EMR clusters are accessing the same S3 bucket1.
   - Data Consistency: DynamoDB helps EMRFS track changes to the data in S3, ensuring that all nodes in the EMR cluster have a consistent view of the data. This is crucial for maintaining data integrity and consistency across distributed systems1.
  - Performance Optimization: By using DynamoDB to store metadata, EMRFS can quickly retrieve information about the files without having to repeatedly scan the S3 bucket. This improves the performance of data-intensive operations1.
 
`File formats`  
- File formats and data compression  
https://docs.aws.amazon.com/whitepapers/latest/aws-glue-best-practices-build-performant-data-pipeline/building-a-performance-efficient-data-pipeline.html#file-formats-and-data-compression

`Optimization`  
- Building a performance efficient data pipeline  
https://docs.aws.amazon.com/whitepapers/latest/aws-glue-best-practices-build-performant-data-pipeline/building-a-performance-efficient-data-pipeline.html
- Building a cost-effective data pipeline  
https://docs.aws.amazon.com/whitepapers/latest/aws-glue-best-practices-build-performant-data-pipeline/building-a-cost-effective-data-pipeline.html
