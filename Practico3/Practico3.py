import cv2
import sys
import numpy as nppytho

if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print('Pass a filename as first argument')
    sys.exit(0)

cap = cv2.VideoCapture(filename)

#fps = int(cap.get(5))                                       # Me indica el frame rate del video (la funcion devuelve un float por eso lo convierte)
fps = int(cv2.VideoCapture.get(cap, cv2.CAP_PROP_FPS))       # Otra forma de leer el frame rate

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    if((cv2.waitKey(fps) & 0xFF) == ord('q')):              # Le hacemos esperar el frame rate
        break

cap.release()
cv2.destroyAllWindows()