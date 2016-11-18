from numpy import *
import scipy as sp
from pandas import *
import pandas.rpy.common as com
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import sys
import cPickle
from scipy.stats import kurtosis, skew, entropy
from sklearn import svm
import pyaudio
import wave
import numpy as np
import csv
import os

r_source = ro.r['source']
r_source(os.getcwd() + '/sound.R')
specan3 = ro.globalenv['specan3']
warbler = importr('warbleR')
tuner = importr('tuneR')
seewave = importr('seewave')

def get_file_attributes(filename):
	d = {'start': ro.r(0), 'end': ro.r(5), "sound.files": filename, "selec": ro.r(0)}
	inp = ro.DataFrame(d)
	x = specan3(inp, bp = ro.IntVector((0,22)), wl = 2048, threshold = 5, parallel = 1)
	data_list = x[3:]
	raw_data = []
	print(x)
	for (i, data) in enumerate(data_list):
		if i is not 12:
			raw_data.append(data[0])
	return raw_data

def get_model(model_name):
	with open(model_name, 'rb') as fid:
		clf = cPickle.load(fid)
	return clf

"""
if __name__ == "__main__":
	clf = get_model('voice_recognition.pkl')
	print(clf.predict([[0.0597809849598081,0.0642412677031359,0.032026913372582,0.0150714886459209,0.0901934398654331,0.0751219512195122,12.8634618371626,274.402905502067,0.893369416700807,0.491917766397811,0,0.0597809849598081,0.084279106440321,0.0157016683022571,0.275862068965517,0.0078125,0.0078125,0.0078125,0,0]]))
	print(clf.predict([[0.165508946001837,0.0928835369116316,0.183043922369765,0.0700715015321757,0.250827374872319,0.180755873340143,1.70502911922022,5.76911536636857,0.938829422236203,0.601528810198165,0.267701736465781,0.165508946001837,0.185606931233589,0.0622568093385214,0.271186440677966,0.227022058823529,0.0078125,0.5546875,0.546875, 0.035]]))
"""