#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Group56 Team members:

#Ziyi Wang (Student ID: 1166087)
#Zhou Zhou (Student ID: 1234764)
#Xiangyi He (Student ID: 1166146)
#Boyu Pan (Student ID: 1319288)
#Huating Ji (Student ID: 1078362)

import pandas as pd
df111 = pd.read_csv('bcc_sport_recreation_2015-2323462154628490517.csv')


# In[2]:


df111


# In[3]:


df111 = df111.drop(columns=['node_use', ' park_name', ' items_name', ' easting', ' node_id',
       ' description', ' ogc_fid', ' pr_no',' northing'])
df111['item_type'] = df111[' item_type'].str.lower()
df111 = df111.drop(columns=[' item_type'])
df111['nodes_name'] = df111[' nodes_name'].str.lower()
df111 = df111.drop(columns=[' nodes_name'])
# Save the modified dataframe to a new CSV file
df111.to_csv('birisbane_sport_file.csv', index=False)


# In[9]:


new_df = pd.read_csv('birisbane_sport_file.csv')
new_df


# In[10]:


dict1 = dict()
for i in new_df['item_type']:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
dict1


# In[11]:


for index, item_type in new_df['item_type'].items():
    if item_type == 'sport facility component':
        new_df.at[index, 'item_type'] = new_df.at[index, 'nodes_name']
    if item_type == 'sporting clubhouse':
        new_df.at[index, 'item_type'] = new_df.at[index, 'nodes_name']
    if item_type == 'sporting field':
        new_df.at[index, 'item_type'] = new_df.at[index, 'nodes_name']
    if item_type == 'sporting court':
        new_df.at[index, 'item_type'] = new_df.at[index, 'nodes_name']
    if item_type == 'recreation facility component':
        new_df.at[index, 'item_type'] = new_df.at[index, 'nodes_name']
    if item_type == 'rebound wall':
        new_df.at[index, 'item_type'] = new_df.at[index, 'nodes_name']
    if item_type == 'upper body equipment':
        new_df.at[index, 'item_type'] = new_df.at[index, 'nodes_name']
    if item_type == 'dog exercise equipment':
        new_df.drop(index, axis=0, inplace=True)
    if item_type == 'piers & jetties':
        new_df.drop(index, axis=0, inplace=True)


# In[13]:


new_df


# In[79]:


dict2 = dict()
for i in new_df['item_type']:
    if i in dict2:
        dict2[i] += 1
    else:
        dict2[i] = 1
dict2


# In[80]:


classified_sports = {
    'Strength and Fitness': [
        'fitness', 'workout', 'exercise', 'gym', 'training', 'crossfit', 'weightlifting', 'cardio', 'strength training',
        'hiit', 'bodybuilding', 'martialarts', 'nutrition', 'healthy eating', 'meal prep', 'protein',
        'vegan fitness', 'intermittent fasting', 'fitness goals', 'weight loss', 'personal trainer',
        'fitness tips', 'fitness / gymnasium workouts', 'yoga', 'pilates','body building', 'callisthenics', 'aerobics', 'fencing', 'tae kwon do', 'judo', 'boxing'
    ],
    'Running and Cycling': [
        'running', 'cycling', 'motor cycling', 'athletics', 'gold coast marathon', 'gcm', 'noosa triathlon', 'noosa tri', 'ironman australia', 'ironman oz','bikeway','bike','walking track'
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
        'the championships', 'randwick', 'melbourne cup', 'melb cup', 'bathurst 1000', 'the great race', 'v8supercars','playground'
    ]
}


# In[81]:


df666 = pd.DataFrame.from_dict(dict2, orient='index', columns=['Values'])
df666.index.name = 'Sports'
df666.index


# In[82]:


import pandas as pd

# Assuming your DataFrame is named 'df'
df666['Classification'] = None  # Create a new column to store the classification

for index in df666.index:
    for key, sports_list in classified_sports.items():
        if any(sport in index for sport in sports_list):
            df666.loc[index, 'Classification'] = key
            break


# In[83]:


count = df666['Classification'].isnull()


# In[84]:


null_count = count.sum()


# In[85]:


null_count


# In[86]:


df666


# In[87]:


sorted_df = df666.sort_values(by='Values',ascending=False)


# In[88]:


sorted_df


# In[89]:


sport_category_values = sorted_df['Classification'].unique()


# In[90]:


sorted_df.reset_index(inplace=True)


# In[91]:


sorted_df.to_json('New_Brisbane_sport_processed.json', orient='records')


# In[92]:


print(sorted_df)


# In[93]:


import json
with open('New_Brisbane_sport_processed.json', 'r') as f2:
    json_data11 = json.load(f2)
json_data11

