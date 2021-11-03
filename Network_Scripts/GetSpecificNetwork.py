import requests
import json
API_Key = input("Enter the API KEY:")
organizationID = input("Enter the organization ID:")
NetworkID = input("Enter the network ID:")

url = "https://api.meraki.com/api/v1/organizations/%s/networks/%s" % (organizationID, NetworkID)
print(url)
payload = {}
headers = {
    'Accept': '*/*',
    'X-Cisco-Meraki-API-Key': (API_Key),

}
response = requests.request("GET", url, headers=headers, data=payload).json()
print(json.dumps(response, indent=2))