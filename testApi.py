import sys
import requests

url = "http://localhost:8000/dailyloglists/"

header = {'Authorization': 'Token ' + sys.argv[1]}
print(header)
response = requests.get(url,headers=header)
print(response.json())

files = {'upload': open(sys.argv[2],'rb')}

payload = {'name': sys.argv[3]}

response = requests.post(url,headers=header, files= files, data=payload)

print(response.json())
