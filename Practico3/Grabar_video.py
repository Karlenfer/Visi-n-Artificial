import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('Video1.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if((cv2.waitKey(1) & 0xFF) == ord('q')):                        # Hacemos la operacion and para quedarnos con los 8 bits menos significativos que nos devuelve la funcion
            break
    else:
        break

cap.release()                       # Liberamos la cámara
out.release()                       # Terminamos de grabar el video
cv2.destroyAllWindows()             # Destruimos todas las ventanas que creamos