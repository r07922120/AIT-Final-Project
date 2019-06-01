import os
import numpy as np

textType = ['.txt']
imgType = ['.jpg', '.png']

def dirList(path):#get the filenames list from the path

	list_ = []
	for filename in sorted(os.listdir(path)):
		ext = os.path.splitext(filename)[1]
		if (ext.lower() not in textType):
			list_.append(os.path.join(path, filename))
	
	return np.array(list_)

def imgList(path):#get the filenames list from the path

	list_ = []
	for filename in sorted(os.listdir(path)):
		ext = os.path.splitext(filename)[1]
		if (ext.lower() in imgType):
			list_.append(os.path.join(path, filename))
	
	return np.array(list_)