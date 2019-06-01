import numpy as np

def computeThreshold(faces):
	mean = np.mean(faces, axis = 0)
	std = np.std(faces, axis = 0)
	absolutes = np.zeros(faces.shape, dtype = np.float32)
	for i in range(len(faces)):
		sub = faces[i] - mean
		absolutes[i] = np.absolute(sub)
		#print(faces[i],absolute, std)
	#remove extreme value
	faces = faces[np.all(~(absolutes > 3 * std), axis = 1)] 
	mean = np.mean(faces, axis = 0)
	original = mean[2] * mean[3]
	return original

def stateCompute(faceArea, state, original, nearRatio = 1.5, farRatio = 0.5):
	if(faceArea >= original * nearRatio):
		return -1
	elif(faceArea <= original * farRatio):
		return 1
	else:
		return 0
