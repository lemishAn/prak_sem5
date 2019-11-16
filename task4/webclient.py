import csv
import pickle
import requests
import json

def csv_dict_reader(file_obj, num):
    i = 0
    reader = csv.reader(file_obj, delimiter = ';')
    send = pickle.dumps(list(reader)[1:num+1])
    return send

num = int(input("Tweet number = "))
command = input("Command = ")
if command.upper() != 'STAT' and command.upper() != 'ENTI':
    command = input('Enter the correct command = ')
with open("dataSet.csv", encoding = "ISO8859-1") as f_obj:
    res = csv_dict_reader(f_obj, num)
    # print(files)
    if command.upper() == 'STAT':
        r = requests.post("http://127.11.0.1:8000", data=res)
        our_content = r.content
        data_for_client = pickle.loads(our_content)
        with open('statistics_2.csv', "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data_for_client)
    if command.upper() == 'ENTI':
        r = requests.post("http://127.11.0.1:8001", data=res)
        our_content = r.content
        data_for_client = pickle.loads(our_content)
        with open('enti_2.json', 'w') as f:
            f.write(json.dumps(data_for_client))