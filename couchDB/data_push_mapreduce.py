import requests
import json
import couchdb

# 连接到CouchDB服务器
ip = "172.26.135.96"
couch = couchdb.Server(f'http://admin:15011010377@{ip}:5984/')

# CouchDB视图的URL和对应的数据库名称
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

print("push_twi_mapreduce start")
for url, db_name in urls_and_dbs.items():
    # 发送get请求
    response = requests.get(url, auth=('admin', '15011010377'))

    # 解析返回的JSON数据
    data = json.loads(response.text)

    # 输出视图结果
    results = []
    for row in data['rows']:
        results.append({'_id': str(row['key']), 'value': row['value']})

    # 检查数据库是否存在，如果存在则删除
    if db_name in couch:
        del couch[db_name]
    
    # 创建新的数据库
    db = couch.create(db_name)
    
    # 上传数据
    for result in results:
        db.save(result)
print("push_twi_mapreduce finish")
 
 