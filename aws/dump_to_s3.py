from pickle import dump
fs = s3fs.S3FileSystem(anon=False)
bucket = 'your-s3-bucket'
key = 'path-prefix/object_name'
data = pd.read_pickle('path/to/sample/data')
dump(data, fs.open(f's3://{bucket}/{key}', 'wb'))
