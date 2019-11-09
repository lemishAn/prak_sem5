import socket
import csv
import pickle
import time
import json

def csv_dict_reader(sock,file_obj, num):
	i = 0
	reader = csv.reader(file_obj, delimiter = ';')
	send = pickle.dumps(list(reader)[1:num+1])
	lenght = len(send)
	sock.sendall((command + ' ' + str(lenght)).encode("utf8"))
	time.sleep(1)
	sock.sendall(send)
	# for line in reader:
	# 	if i <= num:
	# 		send = pickle.dump(i, )
	# 		sock.sendall(send.encode("utf8"))
	# 	else:
	# 		return	
	
with socket.create_connection(("127.0.0.1", 30000)) as sock:
	num = int(input("Tweet number = "))
	command = input("Command = ")
	if command.upper() != 'STAT' and command.upper() != 'ENTI':
		command = input('Enter the correct command = ')
	with open("../../JavaScriptCourse/Tasks/tweets_analysis/input/dataSet.csv", encoding = "ISO8859-1") as f_obj:
		csv_dict_reader(sock,f_obj, num)
	if (int(num) < 10) and (command.upper() == 'STAT'):
		error = sock.recv(4096)
		print(error.decode("utf8"))
	else:
		lst = b''
		data_size = sock.recv(4096)
		data_size = int(data_size.decode("utf8"))
		i = 0
		while i < data_size:
			data = sock.recv(1024)
			lst += data
			i += 1024
		# print("Amount of data = ", data_size)
		data_for_client = pickle.loads(lst)
		if command.upper() == 'STAT':
			with open('statistics.csv', "w", newline="") as file:
				writer = csv.writer(file)
				writer.writerows(data_for_client)
		if command.upper() == 'ENTI':
			with open('enti.json', 'w') as f:
				f.write(json.dumps(data_for_client))
		
