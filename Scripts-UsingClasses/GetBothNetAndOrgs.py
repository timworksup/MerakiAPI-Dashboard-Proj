import requests
import json
import linecache
import pandas as pd
API_Key = linecache.getline(r"ScriptInputInfo.env", 1).rstrip()
OrgID_Line = linecache.getline(r"ScriptInputInfo.env", 2).rstrip()

def WelcomeMessage():
    print("///////////////////////////////////////////////////////////////////////\n//Hello There, and welcome to the testing zone for Python made by Tim.H \n//Hope you will enjoy ;)\n///////////////////////////////////////////////////////////////////////")
    print("Remember to add the needed information in a the excel file, that can be found in the Github Rep")
WelcomeMessage()

# Function to get basic network information
def BaseInfoNet():
    print("You have chosen to get all the networks in the applied organization!!!")
    urlNet = "https://api.meraki.com/api/v1/organizations/%s/networks" % (OrgID_Line)
    payload = {}
    headers = {
        'Accept': '*/*',
        'X-Cisco-Meraki-API-Key': (API_Key)
    }
    response = requests.request("GET", urlNet, headers=headers, data=payload).json()
    print(json.dumps(response,indent=2))
    
# Function to get all the organizations that a user has 
def BaseInfoOrg():
    print("You have chosen to get all the organizations that you have access to!!!")
    urlOrgs = "https://api.meraki.com/api/v1/organizations"
    payload = {}
    headers = {
        'Accept': '*/*',
        'X-Cisco-Meraki-API-Key': (API_Key)
    }
    response = requests.request("GET", urlOrgs, headers=headers, data=payload).json()
    print(json.dumps(response,indent=2))

def ChoseOption():
    UserChoise = input("It is now time for you to make a choice\n what do you wanna know?\n1.All the networks that an organization has?\n2.All the organizations you have access to?")
    if UserChoise == "1":
        return BaseInfoNet()
    if UserChoise == "2":
        return BaseInfoOrg()
ChoseOption()

