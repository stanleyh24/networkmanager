import requests
import urllib3
from requests.exceptions import Timeout

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_resource(ip:str,command:str,username:str,password:str):

    try:
        r = requests.get(f'https://{ip}/rest/{command}', auth=(f'{username}', f'{password}'), verify=False, timeout=2)
        return r.json()
    except Timeout:
        print('Timeout has been raised.')
    
    

response=get_resource('190.160.1.10','ip/address','admin','Asd24690@')
print(response)