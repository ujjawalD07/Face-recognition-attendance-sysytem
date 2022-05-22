import cv2
import numpy as np
import face_recognition

imgCR=face_recognition.load_image_file('ImagesTest/Cristiano Ronaldo.png')
imgCR=cv2.cvtColor(imgCR,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file('ImagesTest/Cristiano Ronaldo test.png')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

face_loc=face_recognition.face_locations(imgCR)[0]
encodeCR=face_recognition.face_encodings(imgCR)[0]
cv2.rectangle(imgCR,(face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]),(0,255,0),2)

face_locTest=face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(face_locTest[3],face_locTest[0]),(face_locTest[1],face_locTest[2]),(0,255,0),2)

results=face_recognition.compare_faces([encodeCR],encodeTest)
dis=face_recognition.face_distance([encodeCR],encodeTest)
print(results,dis)

cv2.imshow('Cristiano Ronaldo',imgCR)
cv2.imshow('Cristiano Ronaldo Test',imgTest)
cv2.waitKey(0)