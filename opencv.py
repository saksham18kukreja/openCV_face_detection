#importing the necessary files
from cv2 import imread
from cv2 import imshow
from cv2 import CascadeClassifier
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import rectangle
from cv2 import VideoCapture
import cv2

#importing the classifier and setting the input source as webcam
classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
camera = VideoCapture(0)

while True:
    
    (_,frame) = camera.read()

    bbox = classifier.detectMultiScale(frame,1.1,5,minSize=(30,30))
    #print(bbox)

    for box in bbox:
      x,y,height,width = box 
      x2,y2 = x+width,y+height
      rectangle(frame,(x,y),(x2,y2),(0,255,0), 2)

    imshow('face detection',frame) 
    if cv2.waitKey(1) & 0xFF == ord('n'):
          break
   
camera.release()
destroyAllWindows()           
