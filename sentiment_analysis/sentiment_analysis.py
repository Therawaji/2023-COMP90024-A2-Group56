#Group56 Team members:

#Ziyi Wang (Student ID: 1166087)
#Zhou Zhou (Student ID: 1234764)
#Xiangyi He (Student ID: 1166146)
#Boyu Pan (Student ID: 1319288)
#Huating Ji (Student ID: 1078362)


#analyse sentiment and add polarity and subjectivity for twitter data

from textblob import TextBlob
import json 
with open("sport_data.json",'r') as f:
    data=json.load(f)
    f.close()

for d in data:
    text=d['text']
    blob = TextBlob(text)
    sentiment = blob.sentiment #generate sentiment using textblob
    polarity = sentiment.polarity  # sentiment polarity [-1.0, 1.0]
    subjectivity = sentiment.subjectivity  #sentiment subjectivity[0.0, 1.0]
    if polarity>0:
        d['polarity']="positive"
    else:
        d['polarity']="negative"
    if subjectivity>0.5:
        d['subjectivity']='subjective'
    else:
        d['subjectivity']='objective'
    
with open("sentiment_analysis.json",'w') as file:
    json.dump(data,file)
    file.close()