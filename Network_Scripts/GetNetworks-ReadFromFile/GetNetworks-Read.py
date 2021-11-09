import requests
import linecache
import json

API_Line = linecache.getline(r"ScriptInput.txt", 1).rstrip()
OrgID_Line = linecache.getline(r"ScriptInput.txt", 2).rstrip()

url = "https://api.meraki.com/api/v1/organizations/%s/networks" % (OrgID_Line)
print(url)

payload = {} 
headers = {
    'Accept': '*/*',
    'X-Cisco-Meraki-API-Key': (API_Line),
}

response = requests.request("GET", url, headers=headers, data=payload).json()
print(json.dumps(response,indent=2))
