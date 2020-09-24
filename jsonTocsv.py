import numpy as numpy
import json
import csv
from io import open
data_count = 0
sum_time = 0.01

contain_id = []
contain_title = []
contain_channel = []
contain_step = []

file_path = "KR_category_id.json"


#0
with open(file_path, "r", encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    # print(json_data['items']['id'])
    for item in json_data['items']:
        # print(item['id'])
        contain_id.append(item['id'])
        contain_title.append(item['snippet']['title'])
        contain_channel.append(item['snippet']['channelId'])
#     for title in json_data['items']['snippet']['title'].values():
#         contain_title.append(title)(title)
#     for channel in json_data['items']['snippet']['channelId'].values():
#         contain_channel.append(channel)
    
    
json_file.close()

with open('category.csv', 'w', newline='') as f:
    fieldnames = ['id', 'title', 'channelId']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    length = len(contain_id)
    print(length)
    # thewriter.writerow({'AccX' : contain_id[700], 'AccY' : contain_title[700], 'AccZ' : contain_channel[700], 'stepCount' : step_count})
    for i in range(length):
        thewriter.writerow({'id' : contain_id[i], 'title' : contain_title[i], 'channelId' : contain_channel[i]})
        sum_time += 0.01

contain_id.clear()
contain_title.clear()
contain_channel.clear()
sum_time = 0
f.close()