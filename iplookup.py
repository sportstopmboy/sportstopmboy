import requests
import json
import sys
from pprint import pprint

if len(sys.argv) == 1:
    request_url = 'http://ident.me'
    response = requests.get(request_url)
    result = response.content.decode()
    ip_address = result
    print("You forgot to provide an IP address so here's information about yours ¯\_(ツ)_/¯ :")

elif len(sys.argv) >= 2:
    ip_address = sys.argv[1]

request_url = f'https://api.ipgeolocation.io/ipgeo?apiKey=```super secret key```&ip={ip_address}&excludes=continent_code,continent_name,country_code2,country_code3,district,connection_type,country_capital,country_flag,is_eu,currency,country_tld,geoname_id,languages,time_zone'
response = requests.get(request_url)
result = response.content.decode()
result  = json.loads(result)
pprint(result)
