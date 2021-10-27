import requests
import meraki
API_Key = input("Enter the API KEY:")
url = "https://api.meraki.com/api/v1/organizations"

payload={}
headers = {
  'Accept': '*/*',
  'X-Cisco-Meraki-API-Key': (API_Key), 
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)