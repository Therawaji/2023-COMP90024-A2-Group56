import json
import requests
import couchdb

print("data_push_external start")
ip = '172.26.135.65'
couch = couchdb.Server(f'http://admin:15011010377@{ip}:5984/')
response = requests.get(f'http://admin:15011010377@{ip}:5984/_all_dbs')
headers = {'Content-type': 'application/json'}

# create database in couchDB
db_name_list = ['vic_sport_dbs', 'income_annual_dbs', 'brisbane_dbs', 'life_dbs']
for db_name in db_name_list:
    #  Delete the original database to prevent clash
    if db_name in couch:
        del couch[db_name]
    
    # creat new couchDB database
    db = couch.create(db_name)

# life
with open('/home/ubuntu/2023-COMP90024-A2-Group56/life.json') as f:
    data = json.load(f)

    for key in data.keys():
        # Create a new document for each city
        document = {'_id': key, 'value': data[key]}
        response = requests.post(f'http://admin:15011010377@{ip}:5984/life_dbs', headers = headers, json=document)

# vic_sports 
file_name_list = [f"/home/ubuntu/2023-COMP90024-A2-Group56/Json file/vic_sports_part{i}.json" for i in range(30)]
for file_name in file_name_list:
    with open(file_name) as f:
        data = json.load(f)

    for item in data:
        response = requests.post(f'http://admin:15011010377@{ip}:5984/vic_sport_dbs', headers = headers, json=item)
    print("finish", file_name)

# Income Annual 
with open('/home/ubuntu/2023-COMP90024-A2-Group56/Income Annual.json') as f:
    data = json.load(f)

    for item in data:
        response = requests.post(f'http://admin:15011010377@{ip}:5984/income_annual_dbs', headers = headers, json=item)

# Brisbane_sport_processed
with open('/home/ubuntu/2023-COMP90024-A2-Group56/Brisbane_sport_processed.json') as f:
    data = json.load(f)

    for item in data:
        response = requests.post(f'http://admin:15011010377@{ip}:5984/brisbane_dbs', headers = headers, json=item)

print("data_push_external finish")

     