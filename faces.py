import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
while True:

    ret, frame = cap.read()
    if not ret:
        print("Camera not accessible")
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces (THIS LINE CREATES 'faces')
    faces = detector(gray)

    i = 0
    for face in faces:
        i += 1

        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()

        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        cv2.putText(frame,
                    'Face ' + str(i),
                    (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        # Exit when 'q' is pressed



# Release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()

