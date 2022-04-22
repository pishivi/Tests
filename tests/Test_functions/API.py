import requests
import json
from requests.structures import CaseInsensitiveDict



headers =""
access_token =""
def authorisation(self):
    url = "https://stage.connect.lol:443/api/v1/sms/verification"
    payload = json.dumps({"phone": "+7..."})
    headers = {'Content-Type': 'application/json'}
    answer_1 = requests.request("POST", url, headers=headers, data=payload, verify=False)


def get_token(self):
    url = ""
    payload = {}
    headers = CaseInsensitiveDict()
    answer_2 = requests.request("GET", url, headers=headers, data=payload, verify=False)
    response = answer_2.json()
    access_token = {}
    access_token['Token'] = response["access_token"]
    print(access_token)

def send_invite(self):
    url = "https://stage.connect.lol:443/api/v1/invite"
    payload = json.dumps({"phone": "+7..."})
    headers['Authorization'] = f'Bearer {access_token["Token"]}'
    headers['Content-Type'] = 'application/json'
    print(headers)
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(response)