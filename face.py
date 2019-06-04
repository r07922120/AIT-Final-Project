import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def faceDetection(img, previousX, previousY, previousW, previousH):
	#init
	maxEyes = -1
	maxIOU = -1
	face = None
	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#rgb to gray
	
	faces = face_cascade.detectMultiScale(gray, 1.1, 3)#face detect
	
	if(previousX == 0 and previousY == 0 and previousW == 0 and previousH == 0):
		for (x,y,w,h) in faces:
			roi_gray = gray[y:y+h, x:x+w]
			#roi_color = img[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray)
			if(len(eyes) > maxEyes):
				face = (x, y, w, h)
				maxEyes = len(eyes)
	else:
		for (x,y,w,h) in faces:			
			IOU = iou(x, y, w, h, previousX, previousY, previousW, previousH)
			if(IOU > maxIOU):
				maxIOU = IOU
				face = (x, y, w, h)
				maxIOU = IOU
		#cv2.rectangle(img,(x, y),(x + w,y + h), (255,0,0),2)
		#for (ex,ey,ew,eh) in eyes:
		#	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	if(face != None):
		cv2.rectangle(img, (face[0], face[1]),(face[0] + face[2], face[1] + face[3]), (255,0,0),2)
	return face

def iou(x1, y1, w1, h1, x2, y2, w2, h2):
	# computing area of each rectangles
	predx0 = x1
	predy0 = y1
	predx1 = x1 + w1
	predy1 = y1 + h1
	targetx0 = x2
	targety0 = y2
	targetx1 = x2 + w2
	targety1 = y2 + h2
	S_rec1 = (predy1 - predy0) * (predx1 - predx0)
	S_rec2 = (targety1 - targety0) * (targetx1 - targetx0)

	# computing the sum_area
	sum_area = S_rec1 + S_rec2

	# find the each edge of intersect rectangle
	left_line = max(predx0, targetx0)
	right_line = min(predx1, targetx1)
	top_line = max(predy0, targety0)
	bottom_line = min(predy1, targety1)

	# judge if there is an intersect
	if left_line >= right_line or top_line >= bottom_line == 0:
		return 0
	else:
		intersect = (right_line - left_line) * (bottom_line - top_line)
		return intersect / (sum_area - intersect)
