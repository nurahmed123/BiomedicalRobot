from facialLandMarkFromVideo import *
import serialCommunication

# from distanceCalculationOfHumanFace import *

import distanceCalculationOfHumanFace

# from distanceCalculationOfHumanFace import findDistance

# from distanceCalculationOfHumanFace import Distance

while True:
    while True:
        distanceCalculationOfHumanFace.findDistance()
        print("running {}".format( distanceCalculationOfHumanFace.Distance ))
        if distanceCalculationOfHumanFace.Distance < human_detect_threshold:
            print("break")
            break
            # return
        key = cv2.waitKey(0)
        if key == 27:
            break
        
    while True:
        findFacialLandMark()
        # serialCommunication.receiveCmd()
        key = cv2.waitKey(1)
        if key == 27:
            # cap.release()
            # cv2.destroyAllWindows()
            break
    print("#####################")
# cap.release()
# cv2.destroyAllWindows()
