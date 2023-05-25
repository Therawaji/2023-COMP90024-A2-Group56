#!/usr/bin/env python
# coding: utf-8

# In[62]:
# Group56 Team members:

# Ziyi Wang (Student ID: 1166087)
# Zhou Zhou (Student ID: 1234764)
# Xiangyi He (Student ID: 1166146)
# Boyu Pan (Student ID: 1319288)
# Huating Ji (Student ID: 1078362)


import pandas as pd
new_df22 = pd.read_csv('abs_personal_income_employee_income.csv')
new_df22


# In[63]:


new_df22.columns


# In[64]:


new_df222 = new_df22.drop(columns=['fid', ' median_aud_2011_12', ' median_age_of_earners_years_2014_15',
                                   ' median_aud_2014_15', ' median_age_of_earners_years_2013_14',
       ' median_age_of_earners_years_2012_13', ' median_aud_2013_14',
       ' median_age_of_earners_years_2017_18',
       ' median_aud_2015_16', ' earners_persons_2011_12', ' mean_aud_2013_14',
       ' median_age_of_earners_years_2016_17', ' median_aud_2016_17',
       ' median_age_of_earners_years_2015_16',
       ' main_source_pc_of_earners_2016_17',
       ' main_source_pc_of_earners_2017_18', ' mean_aud_2011_12',
       ' mean_aud_2012_13', ' median_aud_2017_18', ' earners_persons_2015_16',
       ' main_source_pc_of_earners_2013_14', ' earners_persons_2013_14',
       ' mean_aud_2016_17',' mean_aud_2015_16',
       ' median_age_of_earners_years_2011_12', ' earners_persons_2012_13',
       ' median_aud_2012_13', ' mean_aud_2014_15',
       ' main_source_pc_of_earners_2012_13',
       ' main_source_pc_of_earners_2015_16', 
       ' mean_aud_2017_18', ' main_source_pc_of_earners_2014_15',
       ' earners_persons_2014_15', ' main_source_pc_of_earners_2011_12',
       ' earners_persons_2017_18', ' earners_persons_2016_17'])

# Save the modified dataframe to a new CSV file
new_df222.to_csv('Annual income.csv', index=False)


# In[65]:


df222222 = pd.read_csv('Annual income.csv')
df222222.columns


# In[66]:


# Convert the values from scientific notation to full number form
df222222[' sum_aud_2016_17'] = df222222[' sum_aud_2016_17'].apply(lambda x: "{:.0f}".format(x))
df222222[' sum_aud_2011_12'] = df222222[' sum_aud_2011_12'].apply(lambda x: "{:.0f}".format(x))
df222222[' sum_aud_2014_15'] = df222222[' sum_aud_2014_15'].apply(lambda x: "{:.0f}".format(x))
df222222[' sum_aud_2012_13'] = df222222[' sum_aud_2012_13'].apply(lambda x: "{:.0f}".format(x))
df222222[' sum_aud_2015_16'] = df222222[' sum_aud_2015_16'].apply(lambda x: "{:.0f}".format(x))
df222222[' sum_aud_2013_14'] = df222222[' sum_aud_2013_14'].apply(lambda x: "{:.0f}".format(x))
df222222[' sum_aud_2017_18'] = df222222[' sum_aud_2017_18'].apply(lambda x: "{:.0f}".format(x))
df222222



# In[67]:


df222222[' gccsa_code'] = df222222[' gccsa_code'].str.lower()


# In[68]:


df222222.columns


# In[69]:


import pandas as pd
# Existing Index object
index = df222222.columns
# Remove leading whitespace from index elements
new_index = pd.Index([x.strip() for x in index], dtype='object')


# In[70]:


df3 = df222222.rename(columns=dict(zip(df222222.columns, new_index)))
print(df222222.columns)
print(df3.columns)
df3


# In[71]:


df3.to_json('Income Annual1.json', orient='records')


# In[72]:


import json

# Open the JSON file
with open('Income Annual1.json', 'r') as file:
    json_data222222 = json.load(file)
json_data222222


# In[ ]:




