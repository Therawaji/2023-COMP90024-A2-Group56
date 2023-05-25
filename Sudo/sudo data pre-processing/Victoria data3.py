#!/usr/bin/env python
# coding: utf-8

# In[365]:
# Group56 Team members:

# Ziyi Wang (Student ID: 1166087)
# Zhou Zhou (Student ID: 1234764)
# Xiangyi He (Student ID: 1166146)
# Boyu Pan (Student ID: 1319288)
# Huating Ji (Student ID: 1078362)

import pandas as pd
import json

# Path and filename of the JSON file
df2 = pd.read_json('Json file/vic_sports_part28.json')


# In[366]:


df1 = pd.read_json('sal.json')


# In[367]:


dic2 = dict()
for j in df1:
    if j not in dic2:
        dic2[j] = df1[j]['gcc']


# In[368]:


cl = []
for i in df2['City']:
    appended = False
    for j in dic2.keys():
        if i is not None and isinstance(i, str):
            if i.lower() == j:
                cl.append(dic2[j])
                appended = True
    if not appended:
        cl.append('None')
df2['gcc'] = cl
df2


# In[369]:


import pandas as pd
# Existing Index object
index = df2.columns
# Remove leading whitespace from index elements
new_index = pd.Index([x.strip() for x in index], dtype='object')


# In[370]:


df3 = df2.rename(columns=dict(zip(df2.columns, new_index)))
print(df2.columns)
print(df3.columns)


# In[371]:


df3['sportsplayed'] = df3['sportsplayed'].str.lower()


# In[372]:


classified_sports = {
    'Strength and Fitness': [
        'fitness', 'workout', 'exercise', 'gym', 'training', 'crossfit', 'weightlifting', 'cardio', 'strength training',
        'hiit', 'bodybuilding', 'martialarts', 'nutrition', 'healthy eating', 'meal prep', 'protein',
        'vegan fitness', 'intermittent fasting', 'fitness goals', 'weight loss', 'personal trainer',
        'fitness tips', 'fitness / gymnasium workouts', 'yoga', 'pilates','body building', 'callisthenics', 'aerobics', 'fencing', 'tae kwon do', 'judo', 'boxing'],
    'Running and Cycling': [
        'running', 'cycling', 'motor cycling', 'athletics', 'gold coast marathon', 'gcm', 'noosa triathlon', 'noosa tri', 'ironman australia', 'ironman oz','bikeway','bike','walking track'],
    'Ball Sports': [
        'sports', 'cricket australia', 'aussie rules', 'tennis (outdoor)', 'cricket', 'basketball', 'volleyball', 'netball',
        'netball (indoor)', 'polo', 'rugby union', 'rugby league', 'soccer', 'soccer (indoor soccer / futsal)', 'softball', 'table tennis',
        'australian rules football', 'bocce', 'canoe polo', 'gaelic football', 'martial arts', 'cricket (indoor)', 'australian football league', 'afl', 'national rugby league', 'nrl', 'super rugby', 'super 15', 'a-league', 'a-league men',
        'a-league women', 'big bash league', 'bbl', "women's big bash league", 'wbbl', 'gridiron', 'touch football', 'afl (indoor)', 
        'tennis (indoor)', 'snooker / billiards / pool', 'ten pin bowling', 'team handball'],
    'Water Sports': [
        'surfing australia', 'sydney tohobart', 'sailing', 'swimming', 'underwater hockey', 'jet skiing', 'water skiing', 'surf life saving', 'diving', 'water polo', 'swimming australia', 'sydney to hobart yacht race',
        'sydney hobart', 'australian surf life saving championships', 'rowing'],
    'Outdoor and Adventure Sports': [
        'bmx', 'golf', 'equestrian', 'carpet bowls', 'polocrosse', 'badminton', 'canoeing', 'baseball', 'karate', 'squash / racquetball', 'lawn bowls', 
        'shooting sports', 'skating', 'archery', 'motor sports', 'croquet', 'hockey', 'dancing', 'modern pentathlon', 'beach volleyball', 'lacrosse', 'go karting', 'rock climbing / abseiling (indoor)', 
        'disk golf', 'rodeo', 'open space', 'roller sports', 'ice hockey', 'flying disk', 'inline hockey',
        'wheelchair sports', 'orienteering', 'power boating', 'australian open', 'aus open', 'australian grand prix', 'aus gp',
        'the championships', 'randwick', 'melbourne cup', 'melb cup', 'bathurst 1000', 'the great race', 'v8supercars','playground']
}


# In[373]:


count = df3['sportsplayed'].isnull()
null_count = count.sum()
null_count


# In[374]:


df3.dropna(subset=['sportsplayed'], inplace=True)


# In[375]:


count = df3['sportsplayed'].isnull()
null_count = count.sum()
null_count


# In[376]:


for index, row in df3.iterrows():
    sport = row['sportsplayed']
    for category, sports_list in classified_sports.items():
        if any(sport in s for s in sports_list):
            df3.at[index, 'classification'] = category
            break


# In[377]:


df3


# In[378]:


df3.to_json('Json file/vic_sports_part28.json', orient='records')


# In[379]:


import json

# Open the JSON file
with open('Json file/vic_sports_part28.json', 'r') as file:
    json_data2 = json.load(file)
json_data2


# In[ ]:




