import couchdb
from mastodon import Mastodon, StreamListener
import json

keywords=[ 'fitness', 'workout', 'exercise', 'gym', 'sports', 
    'running', 'yoga', 'pilates', 'crossFit', 'weightlifting','cardio', 'strength training', 
    'hiit', 'bodybuilding', 'martialArts', 'nutrition', 'healthy Eating', 'meal prep','protein', 
    'vegan fitness', 'intermittent fasting', 'fitness goals', 'weight loss', 'motivation', 'personal trainer', 
    'fitness tips', 'cricket australia', 'surfing australia', 'aussie rules', 'sydney tohobart', 'BMX', 'Fitness / Gymnasium Workouts', 
    'Tennis (Outdoor)', 'Golf', 'Equestrian', 'Cricket', 'Sailing', 'Gymnastics', 'Cycling', 'Carpet Bowls', 
    'Polocrosse', 'Badminton', 'Canoeing', 'Baseball', 'Karate', 'Squash / Racquetball', 'Motor Cycling', 'Lawn Bowls', 
    'Basketball', 'Volleyball', 'Netball', 'Netball (indoor)', 'Polo', 'Rugby Union', 'Rugby League', 'Shooting Sports', 'Skating', 'Soccer', 
    'Soccer (Indoor Soccer / Futsal)', 'Softball', 'Swimming', 'Table Tennis', 'Athletics', 'Australian Rules Football', 'Bocce', 'Boxing', 'Canoe Polo', 
    'Gaelic Football', 'Martial Arts', 'Underwater Hockey', 'Archery', 'Motor Sports', 'Cricket (Indoor)', 'Croquet', 'Hockey', 'Dancing', 
    'Jet Skiing', 'Modern Pentathlon', 'Water Skiing', 'Gridiron', 'Surf Life Saving', 'Tae Kwon Do', 'Beach Volleyball', 'Diving', 'Lacrosse', 
    'Snooker / Billiards / Pool', 'Go Karting', 'Touch Football', 'Rowing', 'AFL (Indoor)', 'Rock Climbing / Abseiling (Indoor)', 
    'Aerobics', 'Ten Pin Bowling', 'Disk Golf', 'Body Building', 'Callisthenics', 'Fencing', 'Rodeo', 'Open Space', 'Water Polo', 'Judo', 
    'Roller Sports', 'Tennis (indoor)', 'Ice Hockey', 'Flying Disk', 'Inline Hockey', 'Wheelchair Sports', 
    'Orienteering', 'Team Handball', 'Power Boating', 'Australian Open', 'Aus Open','Australian Football League', 'AFL', 
    'National Rugby League', 'NRL','Super Rugby', 'Super 15', 'A-League', 'A-League Men', 'A-League Women', 'Big Bash League', 'BBL',
    "Women's Big Bash League", 'WBBL', 'Australian Grand Prix', 'Aus GP',  'Sydney to Hobart Yacht Race', 'Sydney Hobart',
    'The Championships', 'Randwick', 'Melbourne Cup', 'Melb Cup', 'Australian Surf Life Saving Championships', 'Aussies',
    'Bathurst 1000', 'The Great Race', 'Gold Coast Marathon', 'GCM', 'Noosa Triathlon', 'Noosa Tri', 'Ironman Australia', 'Ironman Oz',
    'swimming australia', 'v8supercars']
#authentication
admin= 'admin'
password ='15011010377'
url= f'http://{admin}:{password}@172.26.134.44:5984/'

#get couchdb instance
couch= couchdb.Server(url)

#indicate the db name
db_name= 'mastodon_sport'
if db_name not in couch:
    db=couch.create(db_name)
else:
    db=couch[db_name]
    
#optional, better not hardcode here
token='rhlJiPkVsIcQs_KUuRHI7T0aYW1Z91icCd9H7mwQLCw'
m= Mastodon(
    #your server here
    api_base_url=f'https://mastodon.social',
    access_token=token
)

#listen on the timeline
class Listener(StreamListener):

    #called when receiving new post or status update
    def on_update(self,status):
        # do sth
        
        json_str =json.dumps(status, indent=2,sort_keys=True,default=str)
        temp_dict=json.loads(json_str)
        content_str=temp_dict['content']
        for keyword in keywords:
            if keyword in content_str:
                doc_id, doc_rev=db.save(temp_dict)
                print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')
                break
#make it better with try-catch and error-handling
m.stream_public(Listener())