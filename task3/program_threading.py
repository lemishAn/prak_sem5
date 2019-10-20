import warnings
warnings.filterwarnings('ignore')
import librosa
import os
import numpy as np
from threading import Thread
from threading import current_thread
from sys import maxsize
def mfcc_sign(start_dir, end_dir, data, output):
	print(sorted(os.listdir(data))[start_dir:end_dir])
	for p in sorted(os.listdir(data))[start_dir:end_dir]:
		#print(os.listdir(DATA)[start_dir:end_dir])
		DATA_PATH = data + p
		OUTPUT_PATH = output + p
		os.mkdir(OUTPUT_PATH)
		print("1")
		for path in sorted(os.listdir(DATA_PATH)):
			print("2")

			full_path = os.path.join(DATA_PATH, path)
			full_path_output = OUTPUT_PATH + '/' + path
			if os.path.isdir(full_path):
				print("3")
				os.mkdir(full_path_output)
				class_name = path.upper()
				class_files = [os.path.join(full_path, f) for f in sorted(os.listdir(full_path))]
				for file in class_files:
					print(current_thread())
					print("!!!",file,"!!!")
					y = librosa.load(file)[0]
					mfcc = librosa.feature.mfcc(y)
					np.save(full_path_output + '/' + file[-9:-4], mfcc)

#DATA_PATH = ''
DATA = '/home/anastasia/sem5/test/'
OUTPUT = '/home/anastasia/sem5/output2/'
os.mkdir(OUTPUT)
num = int(input("What is the number of threads? \n"))
for_one_thread = len(os.listdir(DATA)) // num
a, b = 0, for_one_thread
thread = []
for i in range(num):
	if i != num - 1:
		thread.append(Thread(target=mfcc_sign, args=(a,b,DATA,OUTPUT)))
		a = b
		b += for_one_thread
	else:
		b = maxsize
		thread.append(Thread(target=mfcc_sign, args=(a,b,DATA,OUTPUT)))
for i in range(num):
	print(os.listdir(DATA))
	thread[i].start()
for i in range(num):
	thread[i].join()