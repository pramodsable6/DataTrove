import pandas as pd
import s3fs

s3 = s3fs.S3FileSystem(anon=False)
f = s3.glob('s3://bucket_name/folder/*.parquet')
f2 = ['s3://' + i for i in f]
df = pd.concat([pd.read_parquet(i) for i in f2]).reset_index(drop=True)
