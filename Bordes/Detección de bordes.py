import cv2
import numpy as np

imagen = cv2.imread('j.png', cv2.IMREAD_COLOR)
cv2.imshow('J', imagen)

# Se define el tamaño del kernel
kernel = np.ones((5, 5), np.uint8)

# Se erosiona la imagen original
eroded = cv2.erode(imagen, kernel, iterations=1)
cv2.imshow('J eroded', eroded)

# Se invierten los valores de los bits de la imagen erosionada
eroded_inv = cv2.bitwise_not(eroded, eroded)
cv2.imshow('J eroded_inv', eroded_inv)

# Se dilata la imagen original
dilated = cv2.dilate(imagen, kernel, iterations=1)
cv2.imshow('J dilated', dilated)

# Se combinan la imagen erosionada e invertida con la imagen dilatada
gradiente_morfologico = cv2.bitwise_and(eroded_inv, dilated)
cv2.imshow('J gradiente_morfológico', gradiente_morfologico)
cv2.imwrite('J_gradiente_morfologico.jpg', gradiente_morfologico)


while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()