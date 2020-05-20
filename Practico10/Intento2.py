import cv2
import numpy as np

img = cv2.imread('Imagen.jpg', 0)

# Aplicamos un filtro Gaussiano
img = cv2.GaussianBlur(img, (3, 3), 1)

# Buscamos bordes
edges = cv2.Canny(img, 130, 200)
cv2.imshow('Bordes', edges)

# Guardamos cada borde
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dibujamos los bordes de interés
img = cv2.drawContours(img, [contours[2]], 0, (0,255,0), 3)
img = cv2.drawContours(img, [contours[4]], 0, (0,255,0), 3)
img = cv2.drawContours(img, [contours[5]], 0, (0,255,0), 3)
img = cv2.drawContours(img, [contours[36]], 0, (0,255,0), 3)
img = cv2.drawContours(img, [contours[37]], 0, (0,255,0), 3)

# Obtenes las esquinas del borde del papel glacé y la dibujamos
bl = tuple(contours[37][contours[37][:, :, 0].argmin()][0])
tr = tuple(contours[37][contours[37][:, :, 0].argmax()][0])
tl = tuple(contours[37][contours[37][:, :, 1].argmin()][0])
br = tuple(contours[37][contours[37][:, :, 1].argmax()][0])
img = cv2.circle(img, bl, 3, (0, 0, 255), 10)
img = cv2.circle(img, tr, 3, (0, 0, 255), 10)
img = cv2.circle(img, tl, 3, (0, 0, 255), 10)
img = cv2.circle(img, br, 3, (0, 0, 255), 10)
cv2.imshow('Contornos y esquinas del papel', img)

# Transformamos la imagen
pts1 = np.float32([tl, tr, br, bl])
pts2 = np.float32([[tl[0],tl[1]], [tr[0],tl[1]], [tr[0],bl[1]], [tl[0],bl[1]]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imagen = cv2.imread('Imagen.jpg', 1)
imagen_transformada = cv2.warpPerspective(imagen, matrix, (imagen.shape[1], imagen.shape[0]))

# Calculamos pixeles por centímetro
pixeles_por_cm = (tr[0]-tl[0])/10

# Buscamos los bordes nuevamente
# Aplicamos un filtro Gaussiano
imagen_transformada = cv2.GaussianBlur(imagen_transformada, (9, 9), 1)

# Buscamos bordes
bordes = cv2.Canny(imagen_transformada, 110, 250)
cv2.imshow('BordeS', bordes)

# Guardamos cada borde
contours2, hierarchy2 = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dibujamos los bordes de interés
imagen_transformada = cv2.drawContours(imagen_transformada, [contours2[3]], 0, (0,255,0), 3)
imagen_transformada = cv2.drawContours(imagen_transformada, [contours2[4]], 0, (0,255,0), 3)
imagen_transformada = cv2.drawContours(imagen_transformada, [contours2[5]], 0, (0,255,0), 3)
imagen_transformada = cv2.drawContours(imagen_transformada, [contours2[27]], 0, (0,255,0), 3)
imagen_transformada = cv2.drawContours(imagen_transformada, [contours2[28]], 0, (0,255,0), 3)

# Obtenes las esquinas del papel glacé, la dibujamos y calculamos sus medidas
tr_papel = tuple(contours2[28][contours2[28][:, :, 1].argmin()][0])
bl_papel = tuple(contours2[28][contours2[28][:, :, 1].argmax()][0])
imagen_transformada = cv2.circle(imagen_transformada, tr_papel, 3, (0, 0, 255), 10)
imagen_transformada = cv2.circle(imagen_transformada, bl_papel, 3, (0, 0, 255), 10)
alto_papel = (bl_papel[1]-tr_papel[1])/pixeles_por_cm
ancho_papel = (tr_papel[0]-bl_papel[0])/pixeles_por_cm
print('El alto del papel es:', alto_papel, 'cm')
print('El ancho del papel es:', ancho_papel, 'cm')

# Obtenes las esquinas de la tarjeta y la dibujamos
tr_tarjeta = tuple(contours2[27][contours2[27][:, :, 0].argmax()][0])
bl_tarjeta = tuple(contours2[27][contours2[27][:, :, 1].argmax()][0])
imagen_transformada = cv2.circle(imagen_transformada, tr_tarjeta, 3, (0, 0, 255), 10)
imagen_transformada = cv2.circle(imagen_transformada, bl_tarjeta, 3, (0, 0, 255), 10)
alto_tarjeta = (bl_tarjeta[1]-tr_tarjeta[1])/pixeles_por_cm
ancho_tarjeta = (tr_tarjeta[0]-bl_tarjeta[0])/pixeles_por_cm
print('El alto de la tarjeta es:', alto_tarjeta, 'cm')
print('El ancho de la tarjeta es:', ancho_tarjeta, 'cm')

# Obtenes las esquinas de la goma y la dibujamos
tr_goma = tuple(contours2[3][contours2[3][:, :, 0].argmax()][0])
bl_goma = tuple(contours2[3][contours2[3][:, :, 1].argmax()][0])
imagen_transformada = cv2.circle(imagen_transformada, tr_goma, 3, (0, 0, 255), 10)
imagen_transformada = cv2.circle(imagen_transformada, bl_goma, 3, (0, 0, 255), 10)
alto_goma = (bl_goma[1]-tr_goma[1])/pixeles_por_cm
ancho_goma = (tr_goma[0]-bl_goma[0])/pixeles_por_cm
print('El alto de la goma es:', alto_goma, 'cm')
print('El ancho de la goma es:', ancho_goma, 'cm')

# Obtenes los extremos de la moneda de $1 y la dibujamos
bl_1 = tuple(contours2[4][contours2[4][:, :, 0].argmin()][0])
tr_1 = tuple(contours2[4][contours2[4][:, :, 0].argmax()][0])
imagen_transformada = cv2.circle(imagen_transformada, bl_1, 3, (0, 0, 255), 10)
imagen_transformada = cv2.circle(imagen_transformada, tr_1, 3, (0, 0, 255), 10)
diametro_1 = (tr_1[0]-bl_1[0])/pixeles_por_cm
print('El diámetro de la moneda de $1 es:', diametro_1, 'cm')

# Obtenes los extremos de la moneda de $0.5 y la dibujamos
bl_50 = tuple(contours2[5][contours2[5][:, :, 0].argmin()][0])
tr_50 = tuple(contours2[5][contours2[5][:, :, 0].argmax()][0])
imagen_transformada = cv2.circle(imagen_transformada, bl_50, 3, (0, 0, 255), 10)
imagen_transformada = cv2.circle(imagen_transformada, tr_50, 3, (0, 0, 255), 10)
diametro_50 = (tr_50[0]-bl_50[0])/pixeles_por_cm
print('El diámetro de la moneda de $0.50 es:', diametro_50, 'cm')

# Mostramos la imagen transformada y los puntos de interés
cv2.imshow('Contornos2', imagen_transformada)

while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()