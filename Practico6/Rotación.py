import numpy as np
import cv2

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w/2, h/2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

img = cv2.imread('transportador.jpg', cv2.IMREAD_COLOR)

# cv2.imwrite('Imagen_rotada.jpg', rotate(img, 180))

cv2.imshow('Imagen_rotada', rotate(img, 90))

while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2 . destroyAllWindows()