import boto3

def list_s3_buckets():
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.list_buckets()
        buckets = response['Buckets']
        
        print("S3 Buckets:")
        for bucket in buckets:
            print(f"- {bucket['Name']} (Created: {bucket['CreationDate']})")
        
        return buckets
    
    except Exception as e:
        print(f"Error listing S3 buckets: {e}")
        return []

if __name__ == "__main__":
    list_s3_buckets()