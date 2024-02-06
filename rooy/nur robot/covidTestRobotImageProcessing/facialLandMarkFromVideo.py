# import the necessary packages
from imutils import face_utils
import dlib
import cv2
import math
import time
from config import *
import serialCommunication
from distanceCalculationOfHumanFace import cap
from playsound import playsound

# cap = cv2.VideoCapture(0)


# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)



def findFacialLandMark():
    global human_detect_flag, mouth_open_flag
    result = 0
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale image
    rects = detector(gray, 0)
    # time.sleep(1)

    # loop over the face detections
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        # print(shape)
        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        flag = 0
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
            flag += 1
            result = math.sqrt(pow(
                abs(shape[51][0] - shape[57][0]), 2) + pow(abs(shape[51][1] - shape[57][1]), 2))
            if RASPBERRY:
                pass
            else:
                print(result)
            # cv2.waitKey(0)
        # print(flag)
        if result > mouthOpenThreshold:
            cv2.putText(frame, "open", (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            mouth_open_flag += 1
            if mouth_open_flag > 15:
                print("open")
            if human_detect_flag == True:
                serialCommunication.sendCmd("MO\n")
                print("MO")
        else:
            cv2.putText(frame, "close", (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            mouth_open_flag = 0
            print("close")
            if human_detect_flag == True:
                serialCommunication.sendCmd("MC\n")
                print("MC")
                say = "open.mp3"
                playsound(say, True)
    # show the output image with the face detections + facial landmarks
    if RASPBERRY:
        pass
    else:
        cv2.imshow("Output", frame)


if __name__ == "__main__":

    while True:
        # _, frame = cap.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # # detect faces in the grayscale image
        # rects = detector(gray, 0)
        # # loop over the face detections
        # for (i, rect) in enumerate(rects):
        # 	# determine the facial landmarks for the face region, then
        # 	# convert the facial landmark (x, y)-coordinates to a NumPy
        # 	# array
        # 	shape = predictor(gray, rect)
        # 	shape = face_utils.shape_to_np(shape)
        # 	# print(shape)
        # 	# loop over the (x, y)-coordinates for the facial landmarks
        # 	# and draw them on the image
        # 	flag  = 0
        # 	for (x, y) in shape:
        # 		cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
        # 		flag += 1
        # 		result = math.sqrt( pow( abs( shape[51][0] - shape[57][0] ) , 2 ) + pow( abs( shape[51][1] - shape[57][1] ) , 2 )  )
        # 		print(result)
        # 		# cv2.waitKey(0)
        # 	# print(flag)
        # 	if result > mouthOpenThreshold:
        # 		cv2.putText(frame,"open", (30,60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
        # 	else:
        # 		cv2.putText(frame,"close", (30,60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
        # # show the output image with the face detections + facial landmarks
        # cv2.imshow("Output", frame)
        findFacialLandMark()
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
