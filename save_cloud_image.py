from ibm_botocore.exceptions import NoCredentialsError  # Ensure you import NoCredentialsError
from ibm_botocore.client import Config
import ibm_boto3
from ibm_botocore.exceptions import ClientError
from PIL import Image
import io
import json

#change this sort of thing later (security credentials)
with open("IBM_images.json",'r') as credentials:
    config_data = json.load(credentials)

cos_api_key_id = config_data['apikey']
cos_service_instance_id = config_data['resource_instance_id']
cos_endpoint = 'https://s3.ams03.cloud-object-storage.appdomain.cloud'


# Initialize COS client
cos_client = ibm_boto3.client('s3',
    ibm_api_key_id=cos_api_key_id,
    ibm_service_instance_id=cos_service_instance_id,
    config=Config(signature_version='oauth'),
    endpoint_url=cos_endpoint)

# therefore we should first read the contents of the bucket and save each one to local

# see objects and last modified date
#def list_objects_in_bucket(bucket_name):
 #   try:
  #      objects = cos_client.list_objects(Bucket=bucket_name)
   #     for obj in objects.get('Contents', []):
    #        print(f"Object Key: {obj['Key']} - Last Modified: {obj['LastModified']}")


#    except Exception as e:
 #       print(f"Unable to list objects in bucket: {e}")

# Function to save an image from COS
def save_image_from_cos(bucket_name, image_key, save_path):
    try:
        response = cos_client.get_object(Bucket=bucket_name, Key=image_key)
        image_data = response['Body'].read()
        image = Image.open(io.BytesIO(image_data))
        image.save(save_path)
        print(f"Image saved to {save_path}")
    except NoCredentialsError:
        print("AWS credentials not available")
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve and save image: {0}".format(e))


# Function to list objects in a bucket
def objects_in_bucket(bucket_name):
    object_keys = []
    try:
        objects = cos_client.list_objects(Bucket=bucket_name)
        for obj in objects.get('Contents', []):
            object_keys.append(obj['Key'])
    except Exception as e:
        print(f"Unable to list objects in bucket: {e}")

    return object_keys

def find_and_save():
    bucket_name = 'jacket-parts'
    # Get the list of object keys in the bucket
    object_keys = objects_in_bucket(bucket_name)

    # Iterate and save each object as an image
    for object_key in object_keys:
        save_image_from_cos(bucket_name, object_key, f'{object_key}')

find_and_save()