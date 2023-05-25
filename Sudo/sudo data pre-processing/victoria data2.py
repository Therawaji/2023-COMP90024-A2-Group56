#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Group56 Team members:

#ZIyi Wang (Student ID: 1166087)
#Zhou Zhou (Student ID: 1234764)
#Xiangyi He (Student ID: 1166146)
#Boyu Pan (Student ID: 1319288)
#Huating Ji (Student ID: 1078362)

import pandas as pd


# In[3]:


df2 = pd.read_csv('part_1.csv')
df2


# In[62]:



from geopy.geocoders import Nominatim

def get_city_from_coordinates(latitude, longitude):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.reverse((latitude, longitude), addressdetails=True)

    city = location.raw['address'].get('city', None)
    if not city:
        city = location.raw['address'].get('town', None)
    if not city:
        city = location.raw['address'].get('village', None)

    return city
for i in range(len(df2[' longitude'])):
    longitude = df2.iloc[i][' longitude']
    latitude = df2.iloc[i][' latitude']
    city = get_city_from_coordinates(latitude, longitude)
    df2.loc[i, ' City'] = city
df2.to_json('vic_sports_part28.json', orient='records')


# In[63]:


import json

# Open the JSON file
with open('vic_sports_part28.json', 'r') as file:
    json_data2 = json.load(file)
json_data2


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




