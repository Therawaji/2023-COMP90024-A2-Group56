from flask import Flask, render_template, request, redirect, Response
import pandas as pd
from flask_cors import CORS
from flask import send_file
from flask import Flask, render_template, request
import couchdb



url = 'http://admin:15011010377@172.26.129.133:5984'
couch = couchdb.Server(url)
ms_url = 'http://admin:15011010377@172.26.131.221:5984'
ms_couch = couchdb.Server(ms_url)


cor={'1gsyd': 'Great Sydney', '2gmel': 'Great Melbourne',
     '3gbri': 'Great Brisbane', '4gade': 'Great Adelaide',
     '5gper': 'Great Perth', '6ghob': 'Great Hobart',
     '7gdar': 'Great Darwin', '8acte': 'Australian Capital \n Territory',
     '9oter': 'Other'
     }

rev_cor = {'Great Sydney':'1gsyd', 'Great Melbourne':'2gmel',
     'Great Brisbane': '3gbri', 'Great Adelaide': '4gade',
     'Great Perth': '5gper', 'Great Hobart': '6ghob',
     'Great Darwin': '7gdar' , 'Australian Capital \n Territory': '8acte',
     'Other': '9oter'
     }

month = {'2':'Feb', '3':'Mar', '4':'Apr', '5':'May',
         '6':'Jun', '7':'Jul', '8':'Aug'}

cities = {'Melbourne': '2gmel','Sydney': '1gsyd', 'Perth': '5gper',
          'Brisbane': '3gbri', 'Adelaide': '4gade', 'Darwin': '7gdar',
          'Hobart': '6ghob', 'Australian Capital Territory': '8acte'}


app = Flask(__name__)
CORS(app, origins=["http://172.26135.125:8080"])



@app.route('/life')
def life():
    db = couch['view2_gcc_count']
    query = {
        "selector": {
            "$or": [
                {"_id": {
                    "$regex": "g"
                }
                },
                {"_id": {
                    "$regex": "8"
                }
                },
                {"_id": {
                    "$regex": "9"
                }
                }
            ]
        }
    }
    return_list = []
    for rows in db.find(query):
        if not rows == "None":
            dict = {}
            dict['value'] = rows['value']
            dict['name'] = cor[rows['_id']]
            return_list.append(dict)
    return return_list


@app.route('/view5')
def view5():
    db = couch['view5_sentiment']
    name_list = []
    pros = []
    cons = []
    for id in db:
        if id[1:-13] != 'None':
            if not id[2:-14] in name_list:
                name_list.append(id[2:-14])
            if id[-10:-2] == 'positive':
                pros.append(db[id]['value'])
            elif id[-10:-2] == 'negative':
                cons.append(db[id]['value'])
    return [name_list, pros, cons]


@app.route('/view6')
def view6():
    db = couch['view6_vic_type']
    name_list = []
    gm_list = []
    vr_list = []
    for id in db:
        if id[-5:-1] != 'None':
            if id[2:6] != 'None':
                if not id[11:-2] in name_list:
                    name_list.append(id[11:-2])
                if id[2:7] == '2gmel':
                    gm_list.append(db[id]['value'])
                if id[2:7] == '2rvic':
                    vr_list.append(db[id]['value'])
    return [name_list, gm_list, vr_list]



@app.route('/view1')
def view1():
    db1 = couch['view1_month']
    db2 = couch['view1_month_event']
    db3 = couch['view1_month_type']
    l1 = []
    for id in db1:
        l1.append(db1[id]['value'])
        if id == '5':
            dict = {}
            dict['value'] = db1[id]['value']
            dict['itemSytle'] = {'color': '#a90000'}
            l1.append(dict)
    event_list = []
    for id in db2:
        n_id = id[5:-2]
        if n_id != 'None':
            event_list.append({'value': db2[id]['value'],
                               'name': n_id})
    type_list = []
    for id in db3:
        n_id = id[5:-2]
        type_list.append({'value': db3[id]['value'],
                           'name': n_id})
    type_list = type_list[:-1]
    return [l1, event_list, type_list]



@app.route('/view4')
def view4():
    db = couch['view4_ball_event']
    r_list = []
    for id in db:
        if id[17:-2] != 'None':
            dict = {}
            dict['value'] = db[id]['value']
            dict['name'] = id[17:-2]
            r_list.append(dict)
    return r_list


@app.route('/view7')
def view7():
    db = couch['view7_bri']
    n_list = []
    v_list = []
    for id in db:
        if id != 'None':
            v_list.append(db[id]['value'])
            n_list.append(id)
    return [n_list, v_list]


@app.route('/genre')
def genre():
    db1 = couch['view3_syd']
    db2 = couch['view3_mel']
    db3 = couch['view3_bri']
    r_list = [['']]
    for id in db1:
        if not id[2:7] in r_list[0]:
            r_list[0].append(id[2:7])
        r_list.append([id[11:-2]])
    i = 1
    for id in db1:
        r_list[i].append(db1[id]['value'])
        i = i+1
    i = 1
    for id in db2:
        if not id[2:7] in r_list[0]:
            r_list[0].append(id[2:7])
        r_list[i].append(db2[id]['value'])
        i = i+1
    i = 1
    for id in db3:
        if not id[2:7] in r_list[0]:
            r_list[0].append(id[2:7])
        r_list[i].append(db3[id]['value'])
        i = i+1
    return r_list[:-1]


@app.route('/events/by_month')
def genre_by_month():
    db1 = couch['view4_month_bri']
    db2 = couch['view4_month_mel']
    db3 = couch['view4_month_syd']
    r_list = [['Aug', []],
              ['Jul', []],
              ['Jun', []],
              ['May', []],
              ['Apr', []],
              ['Mar', []],
              ['Feb', []]]
    i = 6
    for id in db1:
        r_list[i][1].append(db1[id]['value'])
        i -= 1
    i = 6
    for id in db2:
        r_list[i][1].append(db2[id]['value'])
        i -= 1
    i = 6
    for id in db3:
        r_list[i][1].append(db3[id]['value'])
        i -= 1
    return r_list

@app.route('/view8')
def view8():
    db = couch['view2_gcc_count']
    query = {
        "selector": {
            "$or": [
                {"_id": {
                    "$regex": "g"
                }
                },
                {"_id": {
                    "$regex": "8"
                }
                },
                {"_id": {
                    "$regex": "9"
                }
                }
            ]
        }
    }
    n_list = []
    twi_list = []
    for rows in db.find(query):
        if rows != "None":
            if cor[rows['_id']] != "Other":
                twi_list.append(rows['value'])
                n_list.append(cor[rows['_id']])
    db2 = couch['life_dbs']
    dict = {}
    for id in db2:
        dict[cor[cities[id]]] = db2[id]['value']
    life_list = []
    name_list = []
    for name in n_list:
        life_list.append(dict[name])
        name_list.append(rev_cor[name])
    db3 = couch["income_annual_dbs"]
    query3 = {
        "selector": {
            "$or": [
                {"gccsa_code": {
                    "$regex": "g"
                }
                },
                {"gccsa_code": {
                    "$regex": "8"
                }
                }
            ]
        }
    }
    income_list = []
    for rows in db3.find(query3):
        if not rows == "None":
            income_list.append(int(rows['sum_aud_2017_18']))
    return [name_list, twi_list, life_list, income_list]


@app.route('/ms_view1')
def ms_view1():
    db1 = ms_couch['vmas1_sport_type']
    db2 = ms_couch['vmas2_positive_sport_type']
    n_list = []
    t_list = []
    p_list = []
    for id in db1:
        if id != 'None':
            n_list.append(id)
            t_list.append(db1[id]['value'])
    for id in db2:
        if id != 'None':
            p_list.append(db2[id]['value'])
    return [n_list, t_list, p_list]


@app.route('/ms_view2')
def ms_view2():
    db = ms_couch['vmas3_sport_event']
    r_list = []
    for id in db:
        if id != 'None':
            dict = {}
            dict['value'] = db[id]['value']
            dict['name'] = id
            r_list.append(dict)
    return r_list


@app.route('/cob')
def cob():
    return send_file('templates/testmap.png', mimetype='image/gif')

if __name__ == "__main__":
    app.run(debug=True)

