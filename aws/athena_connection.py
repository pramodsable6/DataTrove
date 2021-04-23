import pandas as pd
from pyathena import connect

conn = connect(s3_staging_dir='s3://ABCD/abcd/',
               region_name='enter_region_name')


df = pd.read_sql_query('select * from ABC.XYZ', conn)
df.head()
