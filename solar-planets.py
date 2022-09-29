# import cv2
import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img, "Sun", (80, 400), cv2.FONT_HERSHEY_TRIPLEX, 0.9, (0, 165, 255), 2, cv2.LINE_AA)
cv2.putText(img, "Mercury", (120, 250), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.5, (191, 191, 191), 1, cv2.LINE_AA)
cv2.putText(img, "Venus", (190, 270), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.6, (128, 230, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Earth", (290, 270), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.6, (255, 166, 77), 1, cv2.LINE_AA)
cv2.putText(img, "Moon", (320, 150), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Mars", (380, 270), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.6, (0, 128, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Jupiter", (500, 380), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (51, 173, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Saturn", (730, 290), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.7, (229, 255, 249), 1, cv2.LINE_AA)
cv2.putText(img, "Uranus", (970, 300), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.6, (255, 224, 179), 1, cv2.LINE_AA)
cv2.putText(img, "Neptune", (1120, 300), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.6, (255, 133, 51), 1, cv2.LINE_AA)
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)