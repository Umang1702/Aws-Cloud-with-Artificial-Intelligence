import cv2
from cvzone.HandTrackingModule import HandDetector
import os
cap=cv2.VideoCapture(0)
cap.read()
status,photo=cap.read()
print(status)
#For selecting the image:-
cv2.imwrite("photo.jpeg",photo)
# for Directly showing the image:-
cv2.imshow("photo.jpeg",photo)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#For HAnd Detecting:-
detector=HandDetector()
myfindhands=detector.findHands(photo)
mylmlist=myfindhands[0][0]
myfingerup=detector.fingersUp(mylmlist)
print(myfingerup)
if myfingerup==[1,1,1,1,1]:
    os.system("File Explorar")
elif myfingerup==[0,1,1,0,0]:
    os.system("notepad")
elif myfingerup==[0,0,1,1,0]:
    os.system("comand prompt")
elif myfingerup==[0,0,0,1,1]:
    os.system("Recycle Bin")
else:
    print("idk")
    