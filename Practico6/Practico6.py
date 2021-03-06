import numpy as np
import cv2

def trans_euclidiana(image, angle, tx, ty):
    (h, w) = (image.shape[0], image.shape[1])
    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])
    img_shifted = cv2.warpAffine(image, M, (w, h))
    center = (w / 2, h / 2)
    scale = 1.0
    M = cv2.getRotationMatrix2D(center, angle, scale)
    img_shifted_and_rotated = cv2.warpAffine(img_shifted, M, (w, h))
    return img_shifted_and_rotated

img = cv2.imread('transportador.jpg', cv2.IMREAD_COLOR)

# cv2.imwrite('Imagen_trasladada_y_rotada.jpg', trans_euclidiana(img, 90, 100, 100))

cv2.imshow('Imagen_trasladada_y_rotada', trans_euclidiana(img, 90, 100, 100))

while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2 . destroyAllWindows()