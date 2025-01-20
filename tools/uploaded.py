# file_uploader.py MinIO Python SDK example
from minio import Minio
from minio.error import S3Error
import sys
import os

def main():
    if len(sys.argv) < 5:
        print("Usage: python upfile.py <server> <access_key> <secret_key> <file_path>")
        sys.exit(0)
    print(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    server = sys.argv[1]
    access_key = sys.argv[2]
    secret_key = sys.argv[3]
    client = Minio(server,
        access_key=access_key,
        secret_key=secret_key,
        secure=False,
    )

    # 上传文件夹路径
    source_file = "build"

    # The destination bucket and filename on the MinIO server
    bucket_name = sys.argv[4]
    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # 上传文件夹
    for root, _, files in os.walk(source_file):
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = source_file.replace(source_file, file)
            client.fput_object(bucket_name, destination_file, source_file)
            print("Uploading", source_file, "as", destination_file, "to bucket", bucket_name)



if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
