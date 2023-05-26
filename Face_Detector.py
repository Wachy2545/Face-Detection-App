import cv2
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('R.jfif')
webcam = cv2.VideoCapture(0)

while True:
  succesful_frame_read, frame = webcam.read()
  grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #cv2.imshow('Clever Face Detector', grayscaled_img)
  #cv2.waitKey(1)
  face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


  for (x,y,w,h) in face_coordinates:
    cv2.rectangle(frame,(x,y),(x+w,y+h) , (0, 255, 0), 3)

    #print(face_coordinates)
  cv2.imshow('Clever Programmer Face Detector', frame)
  key = cv2.waitKey(1)

  if key==81 or key==113:
    break  
webcam.release()
"""""
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

for (x,y,w,h) in face_coordinates:
  cv2.rectangle(img,(x,y),(x+w,y+h) , (0, 255, 0), 3)

#print(face_coordinates)
cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()
"""""
print("Code Complete")