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
    
def create_resource(ip:str,command:str,_data:str,username:str,password:str):
    try:
        r = requests.put(f'https://{ip}/rest/{command}',data=_data, auth=(f'{username}', f'{password}'), verify=False, timeout=2)
        return r.json()
    except Timeout:
        print('Timeout has been raised.')    

def update_resource(ip:str,command:str,_data:str,username:str,password:str):
    try:
        r = requests.put(f'https://{ip}/rest/{command}',data=_data, auth=(f'{username}', f'{password}'), verify=False, timeout=2)
        return r.json()
    except Timeout:
        print('Timeout has been raised.') 

def delete_resource(ip:str,command:str,username:str,password:str):
    try:
        r = requests.delete(f'https://{ip}/rest/{command}', auth=(f'{username}', f'{password}'), verify=False, timeout=2)
    except Timeout:
        print('Timeout has been raised.')

response=delete_resource('190.160.1.1','ppp/secret/*2','admin','Asd24690@')
print(response)