import cv2
import numpy as np

umbral1 = 220
umbral2 = 60
umbral3 = 5

# Primera forma

img = cv2.imread ('siempre_verde.png', 0)                   # Abre la imagen y la convierte a escala de grises
cv2.imwrite('siempre_verde_W&B.png', img)

print(img.shape)                                            # Devuelve el tamaño de la imagen en pixeles

for i in range(0, 625):
    for j in range(0, 625):
        px = img[i][j]                                      # Devuelve un valor entre 0 y 255 dependiendo el color del pixel, si fuera una imagen en color te devuelve tres valores (RGB)
        if px >= umbral1:
            img[i][j] = 255
        else:
            img[i][j] = 0

cv2.imwrite('resultado.png', img)                           # Guarda la imagen



# Segunda forma

img2 = cv2.imread ('hoja_verde.png', 0)                     # Abre la imagen y la convierte a escala de grises
cv2.imwrite('hoja_verde_W&B.png', img2)

for i, row in enumerate(img2):
    for j, col in enumerate(row):                           # Estos for son utilizados para determinar la cantidad de filas y comlumnas que tiene la imagen
        if img2[i][j] >= umbral2:
            img2[i][j] = 0
        else:
            img2[i][j] = 255

cv2.imwrite('resultado2.png', img2)                         # Guarda la imagen

# Tercera forma

img3 = cv2.imread ('hoja_seca.png', 0)                      # Abre la imagen y la convierte a escala de grises
cv2.imwrite('hoja_seca_W&B.png', img3)

for i, arreglo in enumerate(img3):                          # Devuelve una numeraión de la cantidad de filas y un arreglo que tiene el valor de color en esacala de grises de cada columna de esa fila
    for j, valor in enumerate(arreglo):                     # Separo cada valor del arreglo
        if valor >= umbral3:
            img3[i][j] = 0
        else:
            img3[i][j] = 255

cv2.imwrite('resultado3.png', img3)                         # Guarda la imagen