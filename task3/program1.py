import librosa
import os
import time
import numpy as np
import warnings
warnings.filterwarnings('ignore')
DATA_PATH = ''
DATA = '/home/anastasia/sem5/test/'
OUTPUT = '/home/anastasia/sem5/output/'
os.mkdir(OUTPUT)
for p in sorted(os.listdir(DATA)):
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
