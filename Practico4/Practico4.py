import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

width = int(cv2.VideoCapture.get(cap, cv2.CAP_PROP_FRAME_WIDTH))        # Obtengo el ancho de la imagen
Height = int(cv2.VideoCapture.get(cap, cv2.CAP_PROP_FRAME_HEIGHT))      # Obtengo el alto de la imagen

out = cv2.VideoWriter('Video1.avi', fourcc, 20.0, (width, Height))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if((cv2.waitKey(1) & 0xFF) == ord('q')):
            break
    else:
        break

cap.release()                       # Liberamos la cámara
out.release()                       # Terminamos de grabar el video
cv2.destroyAllWindows()             # Destruimos todas las ventanas que creamos