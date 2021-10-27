import requests
API_Key = input("Enter the API KEY:")
print("Enter the serial number of effected deviced:")

serialID = input()
url = "https://api.meraki.com/api/v1/devices/%s" % (serialID)
print (url)

payload = {}
headers = {
 'Accept': '*/*',
 'X-Cisco-Meraki-API-Key': (API_Key),
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text.encode('utf8'))
