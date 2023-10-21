import json
from cloudant.client import Cloudant

def update_user_training(username, part): #admin name
    try:

        with open("IBMcred.json", 'r') as credentials:
            config_data = json.load(credentials)

        account_name = config_data['username']
        api_key = config_data['apikey']

        client = Cloudant.iam(account_name, api_key, connect=True)

        my_database = client['corporateapp']
        doc = my_database[f'Machine_Op:{username}']

        if 'trained_in' in doc:
            doc['trained_in'][f'{part}'] = f'admin_name' #{}

            # Update the document in Cloudant
            doc.save()

            print("Training approved successfully.")
        else:
            print("The 'trained_in' dictionary does not exist in the document.")

        client.disconnect()
    except Exception as e:
        print(f"An error occurred: {e}")

#create_user_json('jenny','flap')

#def approval_interface(username, part):
    # create a print or? on admin screen