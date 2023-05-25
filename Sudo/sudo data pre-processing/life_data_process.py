import pandas as pd
import json
import csv
# Group56 Team members:

# Ziyi Wang (Student ID: 1166087)
# Zhou Zhou (Student ID: 1234764)
# Xiangyi He (Student ID: 1166146)
# Boyu Pan (Student ID: 1319288)
# Huating Ji (Student ID: 1078362)


df = pd.read_csv("E:/chrome download/Life_Tables/life.csv")

cities = ['Melbourne','Sydney', 'Perth', 'Brisbane', 'Adelaide', 'Darwin',
          'Hobart', 'Australian Capital Territory']
dict = {}
for i in range(len(df['SA4_NAME21'])):
    for city in cities:
        if city in df['SA4_NAME21'][i]:
            if city in dict:
                dict[city].append(df['life_expectancy_p_2017_19'][i])
            else:
                dict[city] = [df['life_expectancy_p_2017_19'][i]]
for keys in dict:
    dict[keys] = sum(dict[keys])/len(dict[keys])
# with open("E:/chrome download/Life_Tables/life_n.json", "w") as outfile:
#     json.dump(dict, outfile)

new_df = pd.DataFrame()
new_df['cities'] = dict.keys()
new_df['life'] = dict.values()
new_df.to_csv("E:/chrome download/Life_Tables/life_new.csv")

