#!/usr/bin/env python
# coding: utf-8

# In[51]:
#Group56 Team members:

#ZIyi Wang (Student ID: 1166087)
#Zhou Zhou (Student ID: 1234764)
#Xiangyi He (Student ID: 1166146)
#Boyu Pan (Student ID: 1319288)
#Huating Ji (Student ID: 1078362)

import pandas as pd
df = pd.read_csv('vic_sport_and_recreation_2015-679030468100113511.csv')


# In[52]:


df = df.drop(columns=[' changerooms',' streetno',' facilityupgradeage',' facilityage',' numberfieldcourts',
                      ' facilitycondition', ' faciltysportplayedid',' lga',' streetname','fieldsurfacetype',
                     ' postcode',' facility_id',' streettype', ' objectid'])

# Save the modified dataframe to a new CSV file
df.to_csv('new_file.csv', index=False)


# In[53]:


df1 = pd.read_csv('new_file.csv')
df1.columns.values[1] = ' City'
df1


# In[54]:


import pandas as pd


# Calculate the number of rows in the dataframe and divide by 10
part_size = int(len(df1) / 30)

# Slice the dataframe into 10 parts
for i in range(30):
    start = i * part_size
    end = (i + 1) * part_size
    if i == 29:
        end = len(df1)
    part = df1.iloc[start:end]

    # Write the part to a separate CSV file
    part.to_csv(f'part_{i}.csv', index=False)


# In[57]:


df2 = pd.read_csv('part_0.csv')
df2


# In[59]:


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
df2.to_json('vic_sports_part0.json', orient='records')


# In[60]:


import json

# Open the JSON file
with open('vic_sports_part0.json', 'r') as file:
    json_data = json.load(file)
json_data


# In[ ]:





# In[ ]:




