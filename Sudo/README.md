# Group56 Team members:

Ziyi Wang (Student ID: 1166087)

Zhou Zhou (Student ID: 1234764)

Xiangyi He (Student ID: 1166146)

Boyu Pan (Student ID: 1319288)

Huating Ji (Student ID: 1078362)

# Directory Structure
# original data: sudo original data
You will find the  original data of life expectancy under `sudo original data/abs_life_tables_sa4_2010_2019-7439425676767672303.csv`.

You will find the  original data of annual income under `sudo original data/abs_personal_income_employee_income.csv`.

You will find the  original data of Brisbane sports and entertainment facility under `sudo original data/bcc_sport_recreation_2015-2323462154628490517.csv`.

You will find the  original data of sa4 code to covert to greater capital city under `sudo original data/sa4 code.csv`.

You will find the  original data of greater capital city name under `sudo original data/sal.json`.

You will find the  original data of Victoria sports and entertainment facility under `sudo original data/vic_sport_and_recreation_2015-679030468100113511.csv`.
# preprocessing data: sudo data pre-processing
-`Brisbane data.py` pre-processing Brisbane sports and entertainment facility, save to json file.

-`income annual1.py` pre-processing the annual income of each capital city, save to json file

-`life_data_process.R` read the original life expectancy data and pre-processing

-`life_data_process.py`convert to json file

-`victoria data1.py` read the original Victoria sports and entertainment facility data,and split it into 30 parts

-`Victoria data2.py` convert the longitude and latitude to the corresponding city and save it to json file

-`Victoria data3.py` convert the city to the capital city and classification.
