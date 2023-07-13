#importing modules
import json
import requests
import time
                                           
# MAIN CODE
print("78 50 61 6E 74 68 79 72 72")
time.sleep(2)
IP = input("Enter IP \n[CONSOLE] ")
URL = ("http://ip-api.com/json/%s" % (IP))

request = requests.get(URL)

x = request.content

y = json.loads(x)

status = y["status"]
country = y["country"]
region = y["region"]
org = y["org"]
aslime = y["as"]
ipslime = y["query"]
regioncode = y["regionName"]


print("STATUS: ", status)
print("COUNTRY: ", country)
print("REGION2: ", regioncode)
print("REGION: ", region)
print("ORGANISATION: ", org)
print("AS: ", aslime)
print("IP: ", ipslime)


