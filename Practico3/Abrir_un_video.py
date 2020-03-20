import cv2
import sys
import numpy as nppytho

if(len(sys.argv) > 1):                                  # Si escribo en Terminal --> (venv) C:\Users\Fernando\Desktop\UTN\2020\Visión artificial\Practicos\Practico3y4>python Abrir_un_video.py Video1.avi
    filename = sys.argv[1]                              # Me va a detectar que tengo un argumento en la posicion [1], que es el nombre del video y se lo va a pasar a la función para que lo abra
else:
    print('Pass a filename as first argument')
    #sys.exit(0)

#cap = cv2.VideoCapture(filename)                        # Tambien podría abrir el video dandole directamente el nombre en el programa --> cap = cv2.VideoCapture('Video1.avi')
cap = cv2.VideoCapture('Video1.avi')

fps = int(cv2.VideoCapture.get(cap, cv2.CAP_PROP_FPS))   # Ejemplo de como usar los identificadores

# Algunos parámetros importantes

print(cap.get(3))       # CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream

print(cap.get(4))       # CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream

print(cap.get(5))       # CV_CAP_PROP_FPS Frame rate

# Para ver todos los parámetros:
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#cv2.VideoCapture.get

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    if((cv2.waitKey(fps) & 0xFF) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()