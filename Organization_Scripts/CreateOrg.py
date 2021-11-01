import requests
API_KEY = input("Enter your API-KEY:")
url = "https://api.meraki.com/api/v1/organizations"

payload='''{"Name": "Test"}'''
headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    'X-Cisco-Meraki-API-Key': (API_KEY),
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)