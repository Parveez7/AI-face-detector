import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam=cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cordinataes = trained_face_data.detectMultiScale(gray_img)
    for (x, y, w, h) in face_cordinataes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow('Face detector', frame)
    cv2.waitKey(1)
