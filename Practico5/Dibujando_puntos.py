import cv2
import numpy as np

# mouse callback
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
    elif event == cv2.EVENT_RBUTTONUP:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

# Creamos una imagen en blanco, una ventana y capturamos los eventos del mouse en esa ventana

img = np.ones((512, 512, 3), np.uint8) * 255
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2 . destroyAllWindows ( )