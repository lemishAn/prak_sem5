import socket
import threading
import multiprocessing
import os
import csv
from collections import Counter
import pickle
from pycorenlp import StanfordCoreNLP
import time

def tmp(line):
	if line[8] == '':
		return 0
	else:
		return int(line[8])	

def retweet_top10(lst): # most common tweet
	return (reversed(sorted(lst,key = tmp)))

def tmp2(line):
	if not line[14].isdigit():
		return 0
	else:
		return int(line[14])	


def author_top10 (lst):
	followers = list(reversed(sorted(lst, key=tmp2)))[:10]
	follower = []
	j = 0
	for i in followers:
		follower.append([])
		follower[j].append(i[4])
		follower[j].append(i[14])
		j += 1
	return follower


def tweet_top10 (lst): # 10 most common words
	tweet = list()
	for i in lst:
		tweet.extend(i[6].split())
	tweet_top = Counter(tweet)
	tmp = tweet_top.most_common(10)
	tmp2 = []
	for i in range(len(tmp)):
		tmp2.append([])
		tmp2[i].append(tmp[i][0])
		tmp2[i].append(tmp[i][1])
	return tmp2

def country(lst):
	country_tweet = set()
	country_retweet = set()
	for i in lst:
		if i[11] != '':
			if i[6][:2] == "RT":
				country_retweet.add(i[11])
			else:
				country_tweet.add(i[11])
	return list(country_tweet), list(country_retweet)

def process_request(conn, addr):
	print("connected client:", addr)
	lst = b''
	data_com = conn.recv(4096)
	data_com = data_com.decode("utf8")
	data_com = data_com.split(' ')
	lenght = int(data_com[1])
	i = 0
	while i < lenght:
		data = conn.recv(1024)
		lst += data
		i += 1024
	# print(data_com)
	lst2 = pickle.loads(lst)

	if data_com[0].upper() == 'STAT':
		if len(lst2) < 10:
			error = 'Not enough data'
			conn.sendall(error.encode("utf8"))
		else:
			tweet_top = tweet_top10(lst2)
			retweet_top = (list(retweet_top10(lst2)))[:10]
			retweet_top10_necessary = []
			for i in range(len(retweet_top)):
				retweet_top10_necessary.append([])
				retweet_top10_necessary[i].append(retweet_top[i][6])
				retweet_top10_necessary[i].append(retweet_top[i][3])
				retweet_top10_necessary[i].append(retweet_top[i][8])
			author_top = author_top10(lst2)
			country_tweet, country_retweet = country(lst2)
			# print(tweet_top)
			# print(retweet_top10_necessary)
			# print(author_top)
			data_for_client = [['Popular words', 'Number of words']]
			data_for_client.extend(tweet_top)
			data_for_client.extend([])
			data_for_client.extend([['Tweet content', 'author', 'RT']])
			data_for_client.extend(retweet_top10_necessary)
			data_for_client.extend([['author', 'followers']])
			data_for_client.extend(author_top)
			data_for_client.extend([['country_tweet'], country_tweet])
			data_for_client.extend([['country_retweet'], country_retweet])
			# print(data_for_client)
			message = pickle.dumps(data_for_client)
			size = len(message)
			conn.sendall((str(size)).encode("utf8"))
			time.sleep(1)
			conn.sendall(message)

	if data_com[0].upper() == 'ENTI':
		nlp = StanfordCoreNLP('http://localhost:9000')
		pos = []
		for i in lst2:
			text = i[6].replace('\n',' ')
			# print(i[6])
			result = nlp.annotate( text, properties = {'annotators': 'ner', 'outputFormat': 'json', 'timeout': 100000, })
			# print(result["sentences"][0])
			for word in result["sentences"][0]["tokens"]:
				pos.append('{} ({})'.format(word["word"], word["ner"]))
				# print(pos)
			# print('')
			# print(text)
		string = " ".join(pos)
		# print(pos)
		message = pickle.dumps(string)
		size = len(message)
		conn.sendall((str(size)).encode("utf8"))
		time.sleep(1)
		conn.sendall(message)

	conn.close()

def worker(sock):
	while True:
		conn, addr = sock.accept()
		print("pid", os.getpid())
		th = threading.Thread(target=process_request, args=(conn, addr))
		th.start()

with socket.socket() as sock:
	sock.bind(("", 30000))
	sock.listen()
	
	workers_count = 3
	workers_list = [multiprocessing.Process(target=worker, args=(sock,))
					for _ in range(workers_count)] 
	for w in workers_list:
		w.start()
	for w in workers_list:
		w.join()