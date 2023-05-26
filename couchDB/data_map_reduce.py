# Group56 Team members:

# Ziyi Wang (Student ID: 1166087)
# Zhou Zhou (Student ID: 1234764)
# Xiangyi He (Student ID: 1166146)
# oyu Pan (Student ID: 1319288)
# Huating Ji (Student ID: 1078362)

import couchdb

print("data_mapreduce start")

# Connect to couchDB Serve
ip = "172.26.134.151"
couch = couchdb.Server(f'http://admin:15011010377@{ip}:5984/')

db_twi = couch['twi_dbs']

# Doc 1
map_fun1_1 = '''function (doc) {
  emit(doc.month, 1);
}'''

map_fun1_2 = '''function (doc) {
  if(doc.month === 5){
   	emit([doc.month, doc.sport_type], 1);
    }
}'''

map_fun1_3 = '''function (doc) {
  if(doc.month === 5){
   	emit([doc.month, doc.event], 1);
  }
}
'''

# Doc 2
map_fun2 = '''function (doc) {
  emit(doc.gcc, 1);
}'''

# Doc 3
map_fun3_syd = '''function (doc) {
  if (doc.gcc === '1gsyd'){
    emit([doc.gcc, doc.sport_type], 1);
  }
}'''

map_fun3_mel = '''function (doc) {
  if (doc.gcc === '2gmel'){
    emit([doc.gcc, doc.sport_type], 1);
  }
}'''

map_fun3_bri = '''function (doc) {
  if (doc.gcc === '3gbri'){
    emit([doc.gcc, doc.sport_type], 1);
  }
}'''

# Doc 4
map_fun4 = '''function (doc) {
  if (doc.sport_type === 'Ball Sports'){
    emit([doc.sport_type, doc.event], 1);
  }
}'''

# Doc 5
map_fun5 = '''function (doc) {
  emit([doc.sport_type, doc.polarity], 1);
  }'''

# Doc 6
map_fun6 = '''function (doc) {
  if(doc.gcc === '2gmel' || doc.gcc === '2rvic'){
    emit([doc.gcc, doc.sport_type], 1);
  }
}'''
# Doc 7
map_fun7 = '''function (doc) {
  if(doc.gcc === '3gbri'){
    emit([doc.gcc, doc.sport_type], 1);
  }
}'''

# Design doc
twi_design_docs = [
    # Doc 1
    {
        '_id': '_design/doc1',
        'views': {
            'month': {
                'map': map_fun1_1,
                'reduce': '_count'
            },
            'type': {
                'map': map_fun1_2,
                'reduce': '_count'
            },
            'event': {
                'map': map_fun1_3,
                'reduce': '_count'
            }
        }
    },

    # Doc 2
    {
        '_id': '_design/doc2',
        'views': {
            'view': {
                'map': map_fun2,
                'reduce': '_count'
            }
        }
    },

    # Doc 3
    {
        '_id': '_design/doc3',
        'views': {
            'syd': {
                'map': map_fun3_syd,
                'reduce': '_count'
            },
            'mel': {
                'map': map_fun3_mel,
                'reduce': '_count'
            },
            'bri': {
                'map': map_fun3_bri,
                'reduce': '_count'
            }
        }
    },

    # Doc 4
    {
        '_id': '_design/doc4',
        'views': {
            'view': {
                'map': map_fun4,
                'reduce': '_count'
            }
        }
    },
    
    # Doc 5
    {
        '_id': '_design/doc5',
        'views': {
            'view': {
                'map': map_fun5,
                'reduce': '_count'
            }
        }
    },
    # Doc 6
    {
        '_id': '_design/doc6',
        'views': {
            'view': {
                'map': map_fun6,
                'reduce': '_count'
            }
        }
    },
    # Doc 7
    {
        '_id': '_design/doc7',
        'views': {
            'view': {
                'map': map_fun7,
                'reduce': '_count'
            }
        }
    }
]
# Iterate through the list of design documents for db_twi and save them to the database
for design_doc in twi_design_docs:
    if design_doc['_id'] in db_twi:
        del db_twi[design_doc['_id']]
    db_twi.save(design_doc)


db_vic = couch['vic_sport_dbs']

map_fun6_vic = '''function (doc) {
    emit([doc.gcc, doc.classification], 1);
  }'''

vic_design_docs = [
    {
        '_id': '_design/doc6',
        'views': {
            'view': {
                'map': map_fun6_vic,
                'reduce': '_count'
            }
        }
    }
]
# Iterate through the list of design documents for db_vic and save them to the database
for design_doc in vic_design_docs:
    if design_doc['_id'] in db_vic:
        del db_vic[design_doc['_id']]
    db_vic.save(design_doc)


db_bri = couch['brisbane_dbs']

map_fun7_bri = '''function (doc) {
    emit(doc.Classification, doc.Values);
  }'''

bri_design_docs = [
    {
        '_id': '_design/doc7',
        'views': {
            'view': {
                'map': map_fun7_bri,
                'reduce': '_sum'
            }
        }
    }
]
# Iterate through the list of design documents for db_bri and save them to the database
for design_doc in bri_design_docs:
    if design_doc['_id'] in db_bri:
        del db_bri[design_doc['_id']]
    db_bri.save(design_doc)
print("data_mapreduce finish")
