import requests
print("Enter the serial number of effected deviced:")
serialID = input()
url = "https://api.meraki.com/api/v1/devices/%s" % (serialID)
print (url)
payload = {}
headers = {
 'Accept': '*/*',
 'X-Cisco-Meraki-API-Key': 'bcde40199feda1625701bc2af1f7cb972ddd676a',
}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text.encode('utf8'))
