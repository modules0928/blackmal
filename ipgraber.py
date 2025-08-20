import requests
import json

def ip_grabber():
    ip = requests.get('https://api.ipify.org?format=json').text
    parse = json.loads(ip)
    ip_t = parse['ip']
    geolocation = requests.get(f'http://ip-api.com/json/{ip_t}').text
    return geolocation

print(ip_grabber())
