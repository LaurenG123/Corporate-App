import json
from cloudant.client import Cloudant
from datetime import datetime


current_timestamp = datetime.now().timestamp()
dt_object = datetime.utcfromtimestamp(current_timestamp)
formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')

with open("IBMcred.json",'r') as credentials:
    config_data = json.load(credentials)
account_name = config_data['username']
api_key = config_data['apikey']

client = Cloudant.iam(account_name, api_key, connect=True)
my_database = client['corporateapp']

#EXAMPLE TESTED
# effectively the following should be submitted on the click of a button on the app
# note that despite rev field, this doc is not overwritten by running again
partition_key1 = 'part'
document_key = 'flap'
my_database.create_document({
    '_id': ':'.join((partition_key1, document_key)),
    "in_items": [],
    "URL": "next flap"
})

#


#_rev is added as revision, it is effectively the revision number of the document (could be used when rescanning same code on same item?)

client.disconnect()
