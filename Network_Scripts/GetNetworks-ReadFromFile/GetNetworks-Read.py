import requests
import json

FileRead = open("ScriptInput.txt", "r")

API_KEY = print(FileRead.readline(0))
OrgID = print(FileRead.readline(1))

url = "https://api.meraki.com/api/v1/organizations/%s/networks" % (OrgID)
print(url)

payload = {}
header = {
    'Accept': '*/*',
    'X-Cisco-Meraki-API-Key': (API_KEY),
}

response = requests.request("GET", url, headers=header, data=payload).json
print(json.dumps(response,indent=2))