import requests
import json


data = {
"date": "Date Here",
"link": "None",
"title": "Title",
"des": "Budget : $3,000 Posted On : July 21, 2024 08:32 UTC Category : Full Stack Development Skills :Node.js, SQL, MongoDB, Web Application, RESTful API, Django, SaaS, JavaScript, Vue.js Country : United States"
}

def send_File():
    url = 'http://131.186.0.242:5000/update'
    payload = {'data': data}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    
def getProposals():
    url = 'http://127.0.0.1:5000/getProposals' #131.186.0.242
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    response = response.json()
    print(response['Data'])
    # print(response['Data'][0][0].keys())
    # print(response.json())

if __name__ == '__main__':
    # send_File()
    getProposals()

    
    
