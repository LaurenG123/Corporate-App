import json
from cloudant.client import Cloudant
from datetime import datetime

def create_user_json(username):
    try:
        formatted_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        with open("IBMcred.json", 'r') as credentials:
            config_data = json.load(credentials)

        account_name = config_data['username']
        api_key = config_data['apikey']

        client = Cloudant.iam(account_name, api_key, connect=True)
        my_database = client['corporateapp']

        partition_key = 'Machine_Op'
        document_key = f'{username}'

        my_database.create_document({
            '_id': ':'.join((partition_key, document_key)),
            'trained_in': {},
            'joined': formatted_time
        })

        client.disconnect()

        print("User document created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
