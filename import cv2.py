import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap= cv2.VideoCapture(0)

while True:
    red , img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale( gray, 1.1 ,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y) , (x+w,y+h) , (255,0,0), 2)
        roy_gray = gray [y:y+h , x:x+w]
        ray_color = img[y:y+h , x:x+w]
        
    cv2.imwrite('face detectada.jpg',img)
    
cap.release()
cv2.destroyAllWindows()