#Group56 Team members:

#ZIyi Wang (Student ID: 1166087)
#Zhou Zhou (Student ID: 1234764)
#Xiangyi He (Student ID: 1166146)
#Boyu Pan (Student ID: 1319288)
#Huating Ji (Student ID: 1078362)

df <- read.csv("sudo original data/abs_life_tables_sa4_2010_2019-7439425676767672303.csv")
code_name <- read.csv("sudo original data/sa4 code.csv")
df <- merge(df, code_name, by.x="sa4_code16",by.y ="SA4_CODE21")
library(rgdal)
myspdf <- readOGR("E:/chrome download/SA4_2021_AUST_SHP_GDA2020/SA4_2021_AUST_GDA2020.shp")
mynewspdf <- merge(myspdf, df, by.y="sa4_code16",by.x='SA4_CODE21')
write.csv(df, "E:/chrome download/Life_Tables/life.csv")
writeOGR(mynewspdf, dsn = 'E:/chrome download/', layer = 'poly', driver = "ESRI Shapefile")
