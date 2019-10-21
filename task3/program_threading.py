import warnings
warnings.filterwarnings('ignore')
import librosa
import os
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from sys import maxsize
def mfcc_sign(data, output):
	for p in sorted(os.listdir(data)):
		DATA_PATH = data + p
		OUTPUT_PATH = output + p
		os.mkdir(OUTPUT_PATH)
		for path in sorted(os.listdir(DATA_PATH)):
			full_path = os.path.join(DATA_PATH, path)
			full_path_output = OUTPUT_PATH + '/' + path
			if os.path.isdir(full_path):
				os.mkdir(full_path_output)
				class_name = path.upper()
				class_files = [os.path.join(full_path, f) for f in sorted(os.listdir(full_path))]
				for file in class_files:
					y = librosa.load(file)[0]
					mfcc = librosa.feature.mfcc(y)
					np.save(full_path_output + '/' + file[-9:-4], mfcc)

#DATA_PATH = ''
DATA = '/home/anastasia/sem5/test/'
OUTPUT = '/home/anastasia/sem5/output2/'
os.mkdir(OUTPUT)
num = int(input("What is the number of threads? \n"))
with ThreadPoolExecutor(max_workers = num) as pool:
	pool.submit(mfcc_sign, DATA, OUTPUT)