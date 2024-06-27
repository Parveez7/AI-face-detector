import cv2
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('sample_face.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cordinataes = trained_face_data.detectMultiScale(gray_img)
for (x, y, w, h) in face_cordinataes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    break
cv2.imshow('Face detector', img)
cv2.waitKey(0)
