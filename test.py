import requests
import json

def send_File():
    url = 'http://131.186.0.242:5000/download'
    payload = {'url': 'https://zapier-dev-files.s3.amazonaws.com/cli-platform/19925/MjDPmwosAMxsN_kmR8d0aylZFgD0AOQeqUwMamqmei9KYMBcGgvdahBkz7kq7OBEBCacLNTGj1AAj1T3apF0ttxOHC0hfq_6zltN_Q3A5stEuhwRiSvY0_Kwb7o1SeZeQ4JABSO-kfsv8gcB9mhTXKM5XIE8jOvbsOwTOpODwKg'}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    
def getProposals():
    url = 'http://131.186.0.242:5000/getProposals'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    response = response.json()
    print(response['Data'][0])
    # print(response.json())

if __name__ == '__main__':
    # send_File()
    getProposals()
