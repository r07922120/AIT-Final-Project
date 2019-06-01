import os
import csv

import data
import compute

#Title :   Rotation Invariant Neural Network-Based Face Detection


def main():

	root = "frame_images_DB/"
	names = data.dirList(root)
	f = open("frame_images_DB/Aaron_Eckhart.labeled_faces.txt", "r")	
	line = f.readline()#gt
	s = line[13]
	f.close()


	with open("acc2.csv", 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["type", "scale", "correctSum", "predictSum", "gtSum", "precision", "recall", "f1 score", "FP", "timeMean"])
		
		"""
		correctSum = 0
		predictSum = 0
		gtSum = 0
		timeSum = 0

		for name in names:	
			print("ori", name)
			textName = os.path.join(root, os.path.basename(name) + ".labeled_faces.txt")
			f = open(textName, "r")	
			paths = data.dirList(name)
			line = f.readline()
			while line:
				imgLine = line.split(s)
				imgLine[2] = imgLine[2].split(",")[0]
				imgName = os.path.join(root, imgLine[0], imgLine[1], imgLine[2])
				gtLine = line.split(s)
				gtLine = gtLine[2].split(",")
				x = int(gtLine[2])
				y = int(gtLine[3])
				w = int(gtLine[4])
				h = int(gtLine[5])
				line = f.readline()
				correct, faceNum, time = compute.match(imgName, x, y, w, h, 1.1)
				correctSum += correct
				predictSum += faceNum
				gtSum += 1
				timeSum += time
				#print(correct, total)
			f.close()
			
		precision = correctSum / predictSum
		recall = correctSum / gtSum
		f1 = 2 * precision * recall / (precision + recall)
		writer.writerow(["orignal", 1.1, correctSum, predictSum, gtSum, precision, recall, f1, predictSum - correctSum, timeSum / gtSum])

		correctSum = 0
		predictSum = 0
		gtSum = 0
		timeSum = 0

		for name in names:	
			print("eye", name)
			textName = os.path.join(root, os.path.basename(name) + ".labeled_faces.txt")
			f = open(textName, "r")	
			paths = data.dirList(name)
			line = f.readline()
			while line:
				imgLine = line.split(s)
				imgLine[2] = imgLine[2].split(",")[0]
				imgName = os.path.join(root, imgLine[0], imgLine[1], imgLine[2])
				gtLine = line.split(s)
				gtLine = gtLine[2].split(",")
				x = int(gtLine[2])
				y = int(gtLine[3])
				w = int(gtLine[4])
				h = int(gtLine[5])
				line = f.readline()
				correct, faceNum, time = compute.matchEye(imgName, x, y, w, h, 1.1)
				correctSum += correct
				predictSum += faceNum
				gtSum += 1
				timeSum += time
			f.close()
			
		precision = correctSum / predictSum
		recall = correctSum / gtSum
		f1 = 2 * precision * recall / (precision + recall)
		writer.writerow(["orignal", 1.1, correctSum, predictSum, gtSum, precision, recall, f1, predictSum - correctSum, timeSum / gtSum])
		
		correctSum = 0
		predictSum = 0
		gtSum = 0
		timeSum = 0

		for name in names:

			print("IOU", name)
			previousX = 0
			previousY = 0
			previousW = 0
			previousH = 0
			
			textName = os.path.join(root, os.path.basename(name) + ".labeled_faces.txt")
			f = open(textName, "r")	
			paths = data.dirList(name)
			line = f.readline()
			
			while line:
				imgLine = line.split(s)
				imgLine[2] = imgLine[2].split(",")[0]
				imgName = os.path.join(root, imgLine[0], imgLine[1], imgLine[2])
				gtLine = line.split(s)
				gtLine = gtLine[2].split(",")
				x = int(gtLine[2])
				y = int(gtLine[3])
				w = int(gtLine[4])
				h = int(gtLine[5])
				line = f.readline()
				correct, faceNum, time, previousX, previousY, previousW, previousH = compute.matchIOU(imgName, x, y, w, h, 1.1, previousX, previousY, previousW, previousH)
				correctSum += correct
				predictSum += faceNum
				gtSum += 1
				timeSum += time
				#print(correct, total)
			f.close()
			
		"""
		precision = correctSum / predictSum
		recall = correctSum / gtSum
		f1 = 2 * precision * recall / (precision + recall)
		writer.writerow(["IOU", 1.1, correctSum, predictSum, gtSum, precision, recall, f1, predictSum - correctSum, timeSum / gtSum])

		correctSum = 0
		predictSum = 0
		gtSum = 0
		timeSum = 0

		for name in names:	
			print("IOU&eye", name)

			previousX = 0
			previousY = 0
			previousW = 0
			previousH = 0
			textName = os.path.join(root, os.path.basename(name) + ".labeled_faces.txt")
			f = open(textName, "r")	
			paths = data.dirList(name)
			line = f.readline()
			while line:
				imgLine = line.split(s)
				imgLine[2] = imgLine[2].split(",")[0]
				imgName = os.path.join(root, imgLine[0], imgLine[1], imgLine[2])
				gtLine = line.split(s)
				gtLine = gtLine[2].split(",")
				x = int(gtLine[2])
				y = int(gtLine[3])
				w = int(gtLine[4])
				h = int(gtLine[5])
				line = f.readline()
				correct, faceNum, time, previousX, previousY, previousW, previousH = compute.matchIOUandEyes(imgName, x, y, w, h, 1.1, previousX, previousY, previousW, previousH)
				correctSum += correct
				predictSum += faceNum
				gtSum += 1
				timeSum += time
			f.close()
			
			
		precision = correctSum / predictSum
		recall = correctSum / gtSum
		f1 = 2 * precision * recall / (precision + recall)
		writer.writerow(["IOU and eye", 1.1, correctSum, predictSum, gtSum, precision, recall, f1, predictSum - correctSum, timeSum / gtSum])
		
if __name__ == "__main__":
	main()