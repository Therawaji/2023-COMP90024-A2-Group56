#Group56 Team members:

#Ziyi Wang (Student ID: 1166087)
#Zhou Zhou (Student ID: 1234764)
#Xiangyi He (Student ID: 1166146)
#Boyu Pan (Student ID: 1319288)
#Huating Ji (Student ID: 1078362)


# push view created to CouchDB
import requests
import json
import couchdb


couch = couchdb.Server('http://admin:15011010377@172.26.135.65:5984/')


urls_and_dbs = {

    f'http://172.26.135.65:5984/mastodon_dbs/_design/doc1/_view/view?group=true': 'vmas1_sport_type',
    f'http://172.26.135.65:5984/mastodon_dbs/_design/doc2/_view/view?group=true':'vmas2_positive_sport_type',
    f'http://172.26.135.65:5984/mastodon_dbs/_design/doc3/_view/view?group=true':'vmas3_sport_event',
}

print("push_twi_mapreduce start")
for url, db_name in urls_and_dbs.items():
    
    response = requests.get(url, auth=('admin', '15011010377'))

    
    data = json.loads(response.text)


    results = []
    for row in data['rows']:
        results.append({'id': str(row['key']), 'value': row['value']})

    if db_name in couch:
        del couch[db_name]
    
    db = couch.create(db_name)
    
    for result in results:
        db.save(result)
print("push_twi_mapreduce finish")
 
 