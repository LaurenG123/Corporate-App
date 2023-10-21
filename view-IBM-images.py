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
cos_endpoint = #personal


# Initialize COS client
cos_client = ibm_boto3.client('s3',
    ibm_api_key_id=cos_api_key_id,
    ibm_service_instance_id=cos_service_instance_id,
    config=Config(signature_version='oauth'),
    endpoint_url=cos_endpoint)


bucket_name = 'jacket-parts'
collar_key = 'regular-collar.png'
# function to display image in bucket
def get_and_display_image(bucket_name, image_key):
    try:
        response = cos_client.get_object(Bucket=bucket_name, Key=image_key)
        image_data = response['Body'].read()
        image = Image.open(io.BytesIO(image_data))
        image.show()  # Display the image using the default image viewer
        return image
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve and display image: {0}".format(e))

# Retrieve and display the image
#get_and_display_image(bucket_name, collar_key)