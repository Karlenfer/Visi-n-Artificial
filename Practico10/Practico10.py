import cv2
import numpy as np

seleccion_terminada = False
pixeles_por_cm = 0
k = 0
x1, y1 = -1, -1
x2, y2 = -1, -1
x3, y3 = -1, -1
x4, y4 = -1, -1

def seleccion_de_puntos(event, x, y, flags, param):
    global x1, y1, x2, y2, x3, y3, x4, y4, k, imagen_seleccion_de_ptos, seleccion_terminada
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen_seleccion_de_ptos, (x, y), 3, (0, 0, 255), -1)
        if k == 0:
            x1, y1 = x, y
            k = 1
        elif k == 1:
            x2, y2 = x, y
            k = 2
        elif k == 2:
            x3, y3 = x, y
            k = 3
        else:
            x4, y4 = x, y
            k = 0
            seleccion_terminada = True

imagen = cv2.imread('Imagen.jpg', cv2.IMREAD_COLOR)
alto, ancho, _ = imagen.shape

imagen_seleccion_de_ptos = imagen
cv2.namedWindow('Seleccion de puntos')
cv2.setMouseCallback('Seleccion de puntos', seleccion_de_puntos)

cv2.imshow('Seleccion de puntos', imagen_seleccion_de_ptos)

while (seleccion_terminada == False):
    cv2.waitKey(1)
    cv2.imshow('Seleccion de puntos', imagen_seleccion_de_ptos)

if seleccion_terminada == True:
    # Obtenemos la matriz M
    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    pts2 = np.float32([[x1, y1], [x2, y1], [x2, y1 + x2 - x1], [x1, y1 + x2 - x1]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imagen_seleccion_de_ptos = cv2.imread('Imagen.jpg', cv2.IMREAD_COLOR)
    imagen_transformada = cv2.warpPerspective(imagen_seleccion_de_ptos, matrix, (ancho, alto))
    cv2.imwrite('imagen_transformada.jpg', imagen_transformada)
    imagen_seleccion_de_ptos = imagen_transformada
    seleccion_terminada = False

while (seleccion_terminada == False):
    cv2.waitKey(1)
    cv2.imshow('Seleccion de puntos', imagen_seleccion_de_ptos)

if seleccion_terminada == True:
    pixeles_por_cm = (x2 - x1) / 10
    print('Pixeles por centímetro' , pixeles_por_cm)
    imagen_seleccion_de_ptos = cv2.imread('imagen_transformada.jpg', cv2.IMREAD_COLOR)
    # Obtenemos la cantidad de pixeles por centímetro
    seleccion_terminada = False

while(1):

    while (seleccion_terminada == False):
        cv2.waitKey(1)
        cv2.imshow('Seleccion de puntos', imagen_seleccion_de_ptos)

    if seleccion_terminada == True:
        #Medimos un objeto
        print(x2 , x1 , y1 , y3)
        ancho_objeto = (x2 - x1) / pixeles_por_cm
        alto_objeto = (y3 - y1) / pixeles_por_cm
        print('El ancho es de:' , ancho_objeto , 'cm')
        print('El alto es de:' , alto_objeto , 'cm')
        seleccion_terminada = False
        imagen_seleccion_de_ptos = cv2.imread('imagen_transformada.jpg', cv2.IMREAD_COLOR)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()