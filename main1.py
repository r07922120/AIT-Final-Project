import cv2
import numpy as np
import face
import compute
import math

def main():
	#paramaters
	WINDOW_NAME = ("WEBCAM")
	webcam = cv2.VideoCapture(0)
	frame = 0
	faceInit = []
	initFrames = 5
	nearRatio = 1.66
	farRatio = 0.66
	start = False
	state = 0#face distance state
	previousX = 0
	previousY = 0
	previousW = 0
	previousH = 0
	#Read Shooting images
	while 1:
		#get face
		ret, webImage = webcam.read()
		faceIndex = face.faceDetection(webImage, previousX, previousY, previousW, previousH)
		
		cv2.imshow(WINDOW_NAME, webImage)
		

		if(faceIndex != None):
			
			#print(faceInit)
			if(start == False):#init
				faceInit.append(faceIndex)
				if(len(faceInit) == initFrames):
					original = compute.computeThreshold(np.asarray(faceInit))
					start = True

			else:#compute state
				faceArea = faceIndex[2] * faceIndex[3]
				state = compute.stateCompute(faceArea, state, original, nearRatio, farRatio)
				# print(ratio, end = '\r')
			frame += 1
			
			previousX = faceIndex[0]
			previousY = faceIndex[1]
			previousW = faceIndex[2]
			previousH = faceIndex[3]
			
			yield state
		else:
			yield state

		k = cv2.waitKey(20) & 0xFF
		if k == 27:
			break
			
	#press ESC leave
	cv2.destroyAllWindows()

if __name__ == "__main__":
	
	fp = open("output.txt", "w")	
	preState = 0
	fp.write(str(preState))
	fp.close()
	print(preState)
	for state in main():
		if(state != preState and abs(preState - state) != 2):#prevent detect error
			fp = open("output.txt", "w")
			preState = state
			if(state == -1):
				state = 0
			fp.write(str(state))
			fp.close()
			print(state)
	