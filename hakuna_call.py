#Script to handle all API-Calls from Hakuna
import os
import requests

#Gets User-token and Auth-Token for Hakuna from Enviroment-Variables
user = os.environ.get("HAKUSER")
personell_auth_token = os.environ.get("PERSHAKAUTH")
organisation_auth_token = os.environ.get("ORGHAKAUTH") 

def get_users():
    hdr = {
        "X-Auth-Token": personell_auth_token,
        "Host": user
        }
    request = requests.get(f"https://{user}/api/v1/users", headers=hdr)
    print_request(request.json())
    


def print_request(json_list):
    print("Got inital request")
    for item in json_list:
        get_every_user(item['id'])
    
    
    
def get_every_user(user_id):
    hdr = {
        "X-Auth-Token": personell_auth_token,
        "Host": user
        }
    parameters = {
        "user_id": user_id,
        "start_date": "2021-11-29",
        "end_date": "2021-12-4"
        }
    request = requests.get(f"https://{user}/api/v1/time_entries", headers=hdr, params=parameters)
    for item in request.json():
        print(item)
        print("________________________________")
    print("***********************************")
    print("***********************************")
    
    
    
get_users()
