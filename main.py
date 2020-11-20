import winwifi 					#'dumps' the 'windows netsh command'output into a phython object
import requests					#ease the use of HTTP methods for RESTful services  
import json						#handle json objects (captain obvious...)
import os 						#misc OS features, use to load environment vars 
from dotenv import load_dotenv	#handles .env-a-like files
from pathlib import Path		#enables file navigation  

loads your API-key from a file 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
key=os.getenv("GEOLOC_KEY")

url= 'https://www.googleapis.com/geolocation/v1/geolocate?key='+key
headers = {'Content-Type': 'application/json'}
macAddresses=[]
#wi-fi scan
wlanNetworks= winwifi.WinWiFi.scan()
#build the json object based on google API documentation
for macAddr in wlanNetworks:
	macAddresses.append({'macAddress':macAddr.bssid})
payload = json.dumps({'considerIp':'false','wifiAccessPoints': macAddresses})
#send the API request
r = requests.post(url, data=payload, headers=headers)

print (r.text)
