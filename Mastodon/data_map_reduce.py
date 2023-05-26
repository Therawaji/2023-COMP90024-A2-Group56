#Group56 Team members:

#Ziyi Wang (Student ID: 1166087)
#Zhou Zhou (Student ID: 1234764)
#Xiangyi He (Student ID: 1166146)
#Boyu Pan (Student ID: 1319288)
#Huating Ji (Student ID: 1078362)


#map reduce for mastodon, design doc and view for mastodon data

import couchdb

couch = couchdb.Server('http://admin:15011010377@172.26.135.65:5984/')

db_mas = couch['mastodon_dbs']

#Doc 1
map_doc1 = '''function (doc) {
  emit(doc.sport_type, 1);
}'''


#Doc 2
map_doc2 ='''function(doc) {
    if (doc.polarity === 'positive'){
    emit(doc.sport_type, 1);
  }
}'''

#Doc 3
map_doc3 = '''function (doc) {
  emit(doc.event, 1);
}'''


#Design Views

twi_design_docs = [
    # Doc 1
    {
        '_id': '_design/doc1',
        'views': {
            'view': {
                'map': map_doc1 ,
                'reduce': '_count'
            }
        }
    },

    # Doc 2
    {
        '_id': '_design/doc2',
        'views': {
            'view': {
                'map': map_doc2,
                'reduce': '_count'
            }
        }
    },
    
    # Doc 3
    {
        '_id': '_design/doc3',
        'views': {
            'view': {
                'map': map_doc3 ,
                'reduce': '_count'
            }
        }
    },

]
# save to Database
for design_doc in twi_design_docs:
    if design_doc['_id'] in db_mas:
        del db_mas[design_doc['_id']]
    db_mas.save(design_doc)




