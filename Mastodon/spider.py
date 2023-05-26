#Group56 Team members:

#Ziyi Wang (Student ID: 1166087)
#Zhou Zhou (Student ID: 1234764)
#Xiangyi He (Student ID: 1166146)
#Boyu Pan (Student ID: 1319288)
#Huating Ji (Student ID: 1078362)


# A spider to crawl data from mastodon, preprocess data and push data to CouchDB

import couchdb
from mastodon import Mastodon, StreamListener
import json
from textblob import TextBlob

sport_events = ['australian open', 'aus open', 'australian football league', 'afl', 'national rugby league', 'nrl', 'super rugby', 'super 15', 'a-league', 'a-league men', 'a-league women', 'big bash league', 'bbl', "women's big bash league", 'wbbl', 'australian grand prix', 'aus gp', 'sydney to hobart yacht race', 'sydney hobart', 'the championships', 'randwick', 'melbourne cup', 'melb cup', 'australian surf life saving championships', 'aussies', 'bathurst 1000', 'the great race', 'gold coast marathon', 'gcm', 'noosa triathlon', 'noosa tri', 'ironman australia', 'ironman oz', 'swimming australia', 'v8supercars']
sport_events_dict = {
    'Australian Open': ['aus open', 'australian open'],
    'Australian Football League': ['afl', 'australian football league'],
    'National Rugby League': ['nrl', 'national rugby league'],
    'Super Rugby': ['super 15', 'super rugby'],
    'A-League': ['a-league men', 'a-league women', 'a-league'],
    'Big Bash League': ['bbl', 'big bash league'],
    "Women's Big Bash League": ['wbbl', "women's big bash league"],
    'Australian Grand Prix': ['aus gp', 'australian grand prix'],
    'Sydney to Hobart Yacht Race': ['sydney hobart', 'sydney to hobart yacht race'],
    'The Championships': ['randwick', 'the championships'],
    'Melbourne Cup': ['melb cup', 'melbourne cup'],
    'Australian Surf Life Saving Championships': ['australian surf life saving championships'],
    'Bathurst 1000': ['the great race', 'bathurst 1000'],
    'Gold Coast Marathon': ['gcm', 'gold coast marathon'],
    'Noosa Triathlon': ['noosa tri', 'noosa triathlon'],
    'Ironman Australia': ['ironman oz', 'ironman australia'],
    'swimming australia': ['swimming australia'],
    'v8supercars': ['v8supercars']
}
classified_sports = {
    'Strength and Fitness': [
        'fitness', 'workout', 'exercise', 'gym', 'training', 'crossfit', 'weightlifting', 'cardio', 'strength training',
        'hiit', 'bodybuilding', 'martialarts', 'nutrition', 'healthy eating', 'meal prep', 'protein',
        'vegan fitness', 'intermittent fasting', 'fitness goals', 'weight loss', 'personal trainer',
        'fitness tips', 'fitness / gymnasium workouts', 'yoga', 'pilates','body building', 'callisthenics', 'aerobics', 'fencing', 'tae kwon do', 'judo', 'boxing'
    ],
    'Running and Cycling': [
        'running', 'cycling', 'motor cycling', 'athletics', 'gold coast marathon', 'gcm', 'noosa triathlon', 'noosa tri', 'ironman australia', 'ironman oz'
    ],
    'Ball Sports': [
        'sports', 'cricket australia', 'aussie rules', 'tennis (outdoor)', 'cricket', 'basketball', 'volleyball', 'netball',
        'netball (indoor)', 'polo', 'rugby union', 'rugby league', 'soccer', 'soccer (indoor soccer / futsal)', 'softball', 'table tennis',
        'australian rules football', 'bocce', 'canoe polo', 'gaelic football', 'martial arts', 'cricket (indoor)', 'australian football league', 'afl', 'national rugby league', 'nrl', 'super rugby', 'super 15', 'a-league', 'a-league men',
        'a-league women', 'big bash league', 'bbl', "women's big bash league", 'wbbl', 'gridiron', 'touch football', 'afl (indoor)', 
        'tennis (indoor)', 'snooker / billiards / pool', 'ten pin bowling', 'team handball'
    ],
    'Water Sports': [
        'surfing australia', 'sydney tohobart', 'sailing', 'swimming', 'underwater hockey', 'jet skiing', 'water skiing', 'surf life saving', 'diving', 'water polo', 'swimming australia', 'sydney to hobart yacht race',
        'sydney hobart', 'australian surf life saving championships', 'rowing'
    ],
    'Outdoor and Adventure Sports': [
        'bmx', 'golf', 'equestrian', 'carpet bowls', 'polocrosse', 'badminton', 'canoeing', 'baseball', 'karate', 'squash / racquetball', 'lawn bowls', 
        'shooting sports', 'skating', 'archery', 'motor sports', 'croquet', 'hockey', 'dancing', 'modern pentathlon', 'beach volleyball', 'lacrosse', 'go karting', 'rock climbing / abseiling (indoor)', 
        'disk golf', 'rodeo', 'open space', 'roller sports', 'ice hockey', 'flying disk', 'inline hockey',
        'wheelchair sports', 'orienteering', 'power boating', 'australian open', 'aus open', 'australian grand prix', 'aus gp',
        'the championships', 'randwick', 'melbourne cup', 'melb cup', 'bathurst 1000', 'the great race', 'v8supercars'
    ]
}
sport_data = ['fitness', 'workout', 'exercise', 'gym', 'training', 'sports', 'running', 'yoga', 'pilates', 'crossfit', 'weightlifting', 'cardio', 'strength training', 'hiit', 'bodybuilding', 'martialarts', 'nutrition', 'healthy eating', 'meal prep', 'protein', 'vegan fitness', 'intermittent fasting', 'fitness goals', 'weight loss', 'personal trainer', 'fitness tips', 'cricket australia', 'surfing australia', 'aussie rules', 'sydney tohobart', 'bmx', 'fitness / gymnasium workouts', 'tennis (outdoor)', 'golf', 'equestrian', 'cricket', 'sailing', 'gymnastics', 'cycling', 'carpet bowls', 'polocrosse', 'badminton', 'canoeing', 'baseball', 'karate', 'squash / racquetball', 'motor cycling', 'lawn bowls', 'basketball', 'volleyball', 'netball', 'netball (indoor)', 'polo', 'rugby union', 'rugby league', 'shooting sports', 'skating', 'soccer', 'soccer (indoor soccer / futsal)', 'softball', 'swimming', 'table tennis', 'athletics', 'australian rules football', 'bocce', 'boxing', 'canoe polo', 'gaelic football', 'martial arts', 'underwater hockey', 'archery', 'motor sports', 'cricket (indoor)', 'croquet', 'hockey', 'dancing', 'jet skiing', 'modern pentathlon', 'water skiing', 'gridiron', 'surf life saving', 'tae kwon do', 'beach volleyball', 'diving', 'lacrosse', 'snooker / billiards / pool', 'go karting', 'touch football', 'rowing', 'afl (indoor)', 'rock climbing / abseiling (indoor)', 'aerobics', 'ten pin bowling', 'disk golf', 'body building', 'callisthenics', 'fencing', 'rodeo', 'open space', 'water polo', 'judo', 'roller sports', 'tennis (indoor)', 'ice hockey', 'flying disk', 'inline hockey', 'wheelchair sports', 'orienteering', 'team handball', 'power boating', 'australian open', 'aus open', 'australian football league', 'afl', 'national rugby league', 'nrl', 'super rugby', 'super 15', 'a-league', 'a-league men', "a-league women", 'big bash league', 'bbl', "women's big bash league", 'wbbl', 'australian grand prix', 'aus gp', 'sydney to hobart yacht race', 'sydney hobart', 'the championships', 'randwick', 'melbourne cup', 'melb cup', 'australian surf life saving championships', 'bathurst 1000', 'the great race', 'gold coast marathon', 'gcm', 'noosa triathlon', 'noosa tri', 'ironman australia', 'ironman oz', 'swimming australia', 'v8supercars',
            '💪', '🏋️', '🤼‍♀️', '🤸‍♀️', '⛹️‍♀️', '⛹️', '🏌🏿', '🤺', '🏇', '🏌️', '🥋', '🥊', '🧘‍♀️', '🏃‍♀️', '🏃', '🏃‍♂️', '🚵‍♀️', '🚵', '🚵‍♂️', '🚴', '⚽️', '🏀', '🏈', '⚾️', '🥎', '🎱', '🥏', '🏉', '🏐', '🎾', '🪀', '🏓', '🏸', '🏒', '🏑', '⛳️', '🥅', '🤿', '🏄‍♀️', '🏄', '🏄‍♂️', '🏊‍♀️', '🏊', '🏊‍♂️', '🤽‍♀️', '🤽', '🤽‍♂️', '🚣‍♀️', '🚣', '🚣‍♂️', '🧗‍♀️', '🧗', '🧗‍♂️', '🛷', '⛸️', '🥌', '🎿', '⛷️', '🏂', '🪂', '🎣', '🛼', '🏆', '🥇', '🥈', '🥉', '🏅', '🎖️', '🏵️']
emoji_dict = {
    'Strength and Fitness': ['💪', '🏋️', '🤼‍♀️', '🤸‍♀️', '⛹️‍♀️', '⛹️', '🏌🏿', '🤺', '🏇', '🏌️', '🥋', '🥊','🧘‍♀️'],
    'Running and Cycling': ['🏃‍♀️', '🏃', '🏃‍♂️', '🚵‍♀️', '🚵', '🚵‍♂️','🚴'],
    'Ball Sports': ['⚽️', '🏀', '🏈', '⚾️', '🥎', '🎱', '🥏', '🏉', '🏐', '🎾', '🪀', '🏓', '🏸', '🏒', '🏑', '⛳️', '🥅'],
    'Water Sports': ['🤿', '🏄‍♀️', '🏄', '🏄‍♂️', '🏊‍♀️', '🏊', '🏊‍♂️', '🤽‍♀️', '🤽', '🤽‍♂️', '🚣‍♀️', '🚣', '🚣‍♂️'],
    'Outdoor and Adventure Sports': ['🧗‍♀️', '🧗', '🧗‍♂️', '🛷', '⛸️', '🥌', '🎿', '⛷️', '🏂', '🪂', '🎣', '🛼'],
    'Awards': ['🏆', '🥇', '🥈', '🥉', '🏅', '🎖️', '🏵️']
}


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
url= f'http://{admin}:{password}@172.26.133.58:5984/'
#password ='18507007226'
#url= f'http://{admin}:{password}@127.0.0.1:5984/'

#get couchdb instance
couch= couchdb.Server(url)

#indicate the db name
db_name= 'mastodon_dbs'
if db_name not in couch:
    db=couch.create(db_name)
else:
    db=couch[db_name]
    
#optional, better not hardcode here
token='bUaCd-Fd8AP6XbKdopzA-VwT72HDfnGtPsfBP-NVxQA'
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
        d=json.loads(json_str)
        content_str=d['content']
        for keyword in keywords:
            if keyword in content_str:
                sorted_d={}
                
                sorted_d['author_id']=d["account"]["id"]
                sorted_d['create_at']=d["created_at"]
                sorted_d['text']=d["content"]
                text=d["content"]
                blob = TextBlob(text)
                sentiment = blob.sentiment
                polarity = sentiment.polarity  # sentiment polarity [-1.0, 1.0]
                subjectivity = sentiment.subjectivity  # sentiment subjectivity [0.0, 1.0]
                if polarity>0:
                    sorted_d['polarity']="positive"
                else:
                    sorted_d['polarity']="negative"
                if subjectivity>0.5:
                    sorted_d['subjectivity']='subjective'
                else:
                    sorted_d['subjectivity']='objective'
                for i in sport_data:
                    if i.lower() in sorted_d['text'].lower():
                        sorted_d['sport_word']=i
                        break
        
                for key in list(classified_sports.keys()):
                    flag=0
                    if key.lower() in sorted_d['text'].lower():
                        sorted_d['sport_type']=key
                        break
                    for i in classified_sports[key]:
                        if i.lower() in sorted_d['text'].lower():
                            sorted_d['sport_type']=key
                            flag=1
                            break
                    if flag==1:
                        break
                if sorted_d.get('sport_type')== None:
                    for key in emoji_dict:
                        flag=0
                        for e in emoji_dict[key]:
                            if e in sorted_d['text']:
                                sorted_d['sport_type']=key
                                flag=1
                                break
                        if flag==1:
                            break
                if sorted_d.get('sport_type')== None:
                    sorted_d['sport_type']='None'
                for key in list(sport_events_dict.keys()):
                    flag=0
                    if key.lower() in sorted_d['text'].lower():
                        sorted_d['event']=key
                        break
                    for i in sport_events_dict[key]:
                        if i.lower() in sorted_d['text'].lower():
                            sorted_d['event']=key
                            flag=1
                            break
                    if flag==1:
                        break
                if sorted_d.get('event')== None:
                    sorted_d['event']='None' 





                doc_id, doc_rev=db.save(sorted_d)
                print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')
                break
#make it better with try-catch and error-handling


m.stream_public(Listener())

