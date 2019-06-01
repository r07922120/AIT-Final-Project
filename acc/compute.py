import cv2
import time
import math

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


def iou(x1, y1, w1, h1, x2, y2, w2, h2):
	# computing area of each rectangles
	predx0 = x1 - w1 / 2
	predy0 = y1 - h1 / 2
	predx1 = x1 + w1 / 2 
	predy1 = y1 + h1 / 2
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
"""
def match(imgName, x1, y1, w1, h1, scale):
	img = cv2.imread(imgName, 0)
	t1 = time.time()
	faces = face_cascade.detectMultiScale(img, scale, 3)#face detect
	t2 = time.time()
	
	for (x2, y2, w2, h2) in faces:
		#print(iou(x1, y1, w1, h1, x2, y2, w2, h2))
		
		if(iou(x1, y1, w1, h1, x2, y2, w2, h2) > 0.5):
			return 1, len(faces), t2 - t1
	#cv2.imshow("test", img)
	return 0, len(faces), t2 - t1

def matchEye(imgName, x1, y1, w1, h1, scale):
	
	img = cv2.imread(imgName, 0)
	maxEyes = -1
	face = None

	t1 = time.time()
	faces = face_cascade.detectMultiScale(img, scale, 3)#face detect
	
	
	for (x2, y2, w2, h2) in faces:
		roi_gray = img[y2 : y2 + h2, x2 : x2 + w2]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		if(len(eyes) > maxEyes):
			face = (x2, y2, w2, h2)
			maxEyes = len(eyes)
	t2 = time.time()
	
	if(face == None):
		return 0, 0, t2 - t1
	
	if(iou(x1, y1, w1, h1, face[0], face[1], face[2], face[3]) > 0.5):
		return 1, 1, t2 - t1
	else:
		return 0, 1, t2 - t1
"""

def matchIOU(imgName, x1, y1, w1, h1, scale, previousX, previousY, previousW, previousH):
	
	img = cv2.imread(imgName, 0)
	maxIOU = -1
	face = None

	t1 = time.time()
	faces = face_cascade.detectMultiScale(img, scale, 3)#face detect
	
	
	for (x2, y2, w2, h2) in faces:
		#roi_gray = img[y2 : y2 + h2, x2 : x2 + w2]
		IOU = iou(x2, y2, w2, h2, previousX, previousY, previousW, previousH)
		if(IOU > maxIOU):
			face = (x2, y2, w2, h2)
			maxIOU = IOU
		
	t2 = time.time()
	
	if(face == None):
		return 0, 0, t2 - t1, previousX, previousY, previousW, previousH
	
	if(iou(x1, y1, w1, h1, face[0], face[1], face[2], face[3]) > 0.5):
		return 1, 1, t2 - t1, face[0], face[1], face[2], face[3]
	else:
		return 0, 1, t2 - t1, face[0], face[1], face[2], face[3]

def matchIOUandEyes(imgName, x1, y1, w1, h1, scale, previousX, previousY, previousW, previousH):
	
	img = cv2.imread(imgName, 0)
	maxIOU = -1
	maxEyes = -1
	face = None
	

	t1 = time.time()
	faces = face_cascade.detectMultiScale(img, scale, 3)#face detect
	
	
	for (x2, y2, w2, h2) in faces:
		IOUBecomeBig = False
		roi_gray = img[y2 : y2 + h2, x2 : x2 + w2]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		IOU = iou(x2, y2, w2, h2, previousX, previousY, previousW, previousH)
		if(IOU > maxIOU):
			maxIOU = IOU
			IOUBecomeBig = True

		if(len(eyes) > maxEyes):
			face = (x2, y2, w2, h2)
			maxEyes = len(eyes)
		elif(len(eyes) == maxEyes and IOUBecomeBig):
			face = (x2, y2, w2, h2)
		
	t2 = time.time()
	
	if(face == None):
		return 0, 0, t2 - t1, previousX, previousY, previousW, previousH
	
	if(iou(x1, y1, w1, h1, face[0], face[1], face[2], face[3]) > 0.5):
		return 1, 1, t2 - t1, face[0], face[1], face[2], face[3]
	else:
		return 0, 1, t2 - t1, face[0], face[1], face[2], face[3]
