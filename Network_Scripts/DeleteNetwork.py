import requests

API_Key = input("Enter your API Key:")
NetworkID = input("Enter the ID of the network that is wished to be removed: ")

url = "https://api.meraki.com/api/v1/networks/%s" % (NetworkID)
print(url)

payload = None
headers = {
    "Content-Type": "applications/json",
    "Accept": "applications/json",
    "X-Cisco-Meraki-API-Key": (API_Key),
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)