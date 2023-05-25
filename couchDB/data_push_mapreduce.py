# Group56 Team members:

# Ziyi Wang (Student ID: 1166087)
# Zhou Zhou (Student ID: 1234764)
# Xiangyi He (Student ID: 1166146)
# Boyu Pan (Student ID: 1319288)
# Huating Ji (Student ID: 1078362)


import requests
import json
import couchdb

print("data_push_mapreduce start")
# connect to couchdb server
ip = "172.26.134.151"
couch = couchdb.Server(f'http://admin:15011010377@{ip}:5984/')

# URL of the CouchDB view and the corresponding database name
urls_and_dbs = {
    f'http://{ip}:5984/twi_dbs/_design/doc1/_view/month?group=true': 'view1_month',
    f'http://{ip}:5984/twi_dbs/_design/doc1/_view/type?group=true': 'view1_month_type',
    f'http://{ip}:5984/twi_dbs/_design/doc1/_view/event?group=true': 'view1_month_event',


    f'http://{ip}:5984/twi_dbs/_design/doc2/_view/view?group=true': 'view2_gcc_count',

    f'http://{ip}:5984/twi_dbs/_design/doc3/_view/syd?group=true': 'view3_syd',
    f'http://{ip}:5984/twi_dbs/_design/doc3/_view/mel?group=true': 'view3_mel',
    f'http://{ip}:5984/twi_dbs/_design/doc3/_view/bri?group=true': 'view3_bri',

    f'http://{ip}:5984/twi_dbs/_design/doc4/_view/view?group=true':'view4_ball_event',

    f'http://{ip}:5984/twi_dbs/_design/doc5/_view/view?group=true':'view5_sentiment',

    f'http://{ip}:5984/vic_sport_dbs/_design/doc6/_view/view?group=true':'view6_vic_type',
    f'http://{ip}:5984/twi_dbs/_design/doc6/_view/view?group=true':'view6_twi_vic_typet',

    f'http://{ip}:5984/brisbane_dbs/_design/doc7/_view/view?group=true':'view7_bri',
    f'http://{ip}:5984/twi_dbs/_design/doc7/_view/view?group=true':'view7_twi'
}

# Upload the result of mapreduce
for url, db_name in urls_and_dbs.items():
    response = requests.get(url, auth=('admin', '15011010377'))

    data = json.loads(response.text)

    results = []
    for row in data['rows']:
        results.append({'_id': str(row['key']), 'value': row['value']})

    if db_name in couch:
        del couch[db_name]

    db = couch.create(db_name)

    for result in results:
        db.save(result)

print("data_push_mapreduce finish")
 