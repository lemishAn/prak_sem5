import librosa
import os
from multiprocessing import Process
import numpy as np
from sys import maxsize
def mfcc_sign(start_dir, end_dir):
	for p in sorted(os.listdir(DATA))[start_dir:end_dir]:
		DATA_PATH = DATA + p
		OUTPUT_PATH = OUTPUT + p
		os.mkdir(OUTPUT_PATH)
		for path in sorted(os.listdir(DATA_PATH)):
			full_path = os.path.join(DATA_PATH, path)
			full_path_output = OUTPUT_PATH + '/' + path
			if os.path.isdir(full_path):
				os.mkdir(full_path_output)
				class_name = path.upper()
				class_files = [os.path.join(full_path, f) for f in sorted(os.listdir(full_path))]
				for file in class_files:
					y, sr = librosa.load(file)
					mfcc = librosa.feature.mfcc(y, sr)
					np.save(full_path_output + '/' + file[-9:-4], mfcc)

DATA_PATH = ''
DATA = '/home/anastasia/sem5/test/'
OUTPUT = '/home/anastasia/sem5/output3/'
os.mkdir(OUTPUT)
num = int(input("What is the number of process? \n"))
for_one_process = len(os.listdir(DATA)) // num
a, b = 0, for_one_process
process = []
for i in range(num):
	if i != num - 1:
		process.append(Process(target=mfcc_sign, args=(a,b)))
		a = b
		b += for_one_process
	else:
		b = maxsize
		process.append(Process(target=mfcc_sign, args=(a,b)))
for i in range(num):
	process[i].start()
for i in range(num):
	process[i].join()