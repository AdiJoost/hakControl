#Script to handle all API-Calls from Hakuna
import os
import requests

#Gets User-token and Auth-Token for Hakuna from Enviroment-Variables
user = os.environ.get("HAKUSER")
personell_auth_token = os.environ.get("PERSHAKAUTH")
organisation_auth_token = os.environ.get("ORGHAKAUTH") 

