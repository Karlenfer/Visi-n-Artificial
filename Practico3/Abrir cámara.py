import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print(cap.isOpened())                                       # Indica si se pudo abrir la cámara o no

while(True):
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          # Convierte el video de color BGR a escala de grises

    cv2.imshow('frame', gray)

    if((cv2.waitKey(1) & 0xFF) == ord('q')):                # Si se tipea una "q" se termina el bucle y finaliza el programa
        break


cap.release()                                               # Liberamos la cámara
cv2.destroyAllWindows()