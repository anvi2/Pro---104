import cv2

ss = cv2.imread("solar-system.jpg")



sun = "Sun"
cv2.putText(ss , sun , (70 , 60), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL , fontScale=1.8 , color=(0,255,255))
mercury = "Mercury"
cv2.putText(ss , mercury , (120 ,180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL , fontScale=0.6 , color=(255,255,255))
venus = "Venus"
cv2.putText(ss , venus , (190 , 250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL , fontScale=0.6 , color=(255,255,255))
earth = "Earth"
cv2.putText(ss , earth , (290 , 260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL , fontScale=0.6 , color=(255,255,255))
mars = "Mars"
cv2.putText(ss , mars , (380 , 250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL , fontScale=0.6 , color=(255,255,255))
jupiter = "Jupiter"
cv2.putText(ss , jupiter , (540 , 70), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL , fontScale=1.4 , color=(182,255,209))
saturn = "Saturn"
cv2.putText(ss , saturn , (750 , 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL , fontScale=1.02 , color=(255,255,255))
uranus = "Uranus"
cv2.putText(ss , uranus, (960 , 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL , fontScale=0.7 , color=(255,255,255))
neptune = "Neptune"
cv2.putText(ss , neptune , (1120 , 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL , fontScale=0.7 , color=(255,255,255))

cv2.imshow("display image" , ss)
cv2.waitKey(0)
print(ss)
cv2.imwrite("Solar-system with name.jpg" , ss)