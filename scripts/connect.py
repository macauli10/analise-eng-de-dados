import boto3
import pandas as pd
import io
from dotenv import load_dotenv
import os
load_dotenv()

S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")
AWS_REGION = os.getenv("AWS_REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

s3 = boto3.client(
    "s3",
    region_name=AWS_REGION,
    endpoint_url=S3_ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
)


#response = s3.list_objects(Bucket=BUCKET_NAME)
#arquivos = [obj["Key"] for obj in response["Contents"]]
#print(arquivos)

FILE_KEY='preco_competidores.parquet'
response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
parquet_bytes = response["Body"].read()
df_preco_competidores = pd.read_parquet(io.BytesIO(parquet_bytes))
print(df_preco_competidores.head(10))