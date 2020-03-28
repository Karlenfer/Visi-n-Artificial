import numpy as np
import cv2


modes = {'x':0, 'y':1, 'b':-1}

def flip(img, mode):
    if(mode not in modes.keys()):
        return img
    flipped = cv2.flip(img, modes[mode])
    return flipped

img = cv2.imread('transportador.jpg', cv2.IMREAD_COLOR)

# cv2.imwrite('Imagen_espejada.jpg', flip(img, x))

cv2.imshow('Imagen_espejada', flip(img, 'y'))

while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2 . destroyAllWindows()