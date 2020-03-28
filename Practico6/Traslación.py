import numpy as np
import cv2

def translate(image, x, y):
    (h, w) = (image.shape[0], image.shape[1])
    M = np.float32([[1, 0, x],
                    [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (w, h))
    return shifted

img = cv2.imread('transportador.jpg', cv2.IMREAD_COLOR)

# cv2.imwrite('Imagen_trasladada.jpg', translate(img, 100, 100))

cv2.imshow('Imagen_trasladada', translate(img, 100, 100))

while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2 . destroyAllWindows()