import json
import requests
import couchdb

# 上传vic_sport的数据
ip = '172.26.135.96'
couch = couchdb.Server(f'http://admin:15011010377@{ip}:5984/')
response = requests.get(f'http://admin:15011010377@{ip}:5984/_all_dbs')
headers = {'Content-type': 'application/json'}

# 创建数据库
db_name_list = ['vic_sport_dbs', 'country_of_birth_dbs', 'income_annual_dbs', 'brisbane_dbs', 'life_dbs']
for db_name in db_name_list:
    # 删除本来的数据库 防止clash
    if db_name in couch:
        del couch[db_name]
    
    # 创建新的数据库
    db = couch.create(db_name)

# life
with open('/Users/hexiangyi/Desktop/life.json') as f:
    data = json.load(f)

    for key in data.keys():
        # Create a new document for each city
        document = {'_id': key, 'value': data[key]}
        response = requests.post(f'http://admin:15011010377@{ip}:5984/life_dbs', headers = headers, json=document)

# vic_sports 需要修改文件上传路径
file_name_list = [f"/Users/hexiangyi/Desktop/CCC_Assignment2_Group56/Json file/vic_sports_part{i}.json" for i in range(30)]
for file_name in file_name_list:
    with open(file_name) as f:
        data = json.load(f)

    for item in data:
        response = requests.post(f'http://admin:15011010377@{ip}:5984/vic_sport_dbs', headers = headers, json=item)
    print("finish", file_name)

# country_of_birth 需要修改文件上传路径
with open('/Users/hexiangyi/Desktop/country_of_birth.json') as f:
    data = json.load(f)

    for item in data:
        response = requests.post(f'http://admin:15011010377@{ip}:5984/country_of_birth_dbs', headers = headers, json=item)

# Income Annual 需要修改文件上传路径
with open('/Users/hexiangyi/Desktop/Income Annual.json') as f:
    data = json.load(f)

    for item in data:
        response = requests.post(f'http://admin:15011010377@{ip}:5984/income_annual_dbs', headers = headers, json=item)

# Brisbane_sport_data 需要修改文件上传路径
with open('/Users/hexiangyi/Desktop/Brisbane_sport_processed.json') as f:
    data = json.load(f)

    for item in data:
        response = requests.post(f'http://admin:15011010377@{ip}:5984/brisbane_dbs', headers = headers, json=item)


     