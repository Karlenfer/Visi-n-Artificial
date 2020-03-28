import cv2
import numpy as np

seleccion_terminada = False
k = 0
x1, y1 = -1, -1
x2, y2 = -1, -1
x3, y3 = -1, -1
x4, y4 = -1, -1

def seleccion_de_puntos(event, x, y, flags, param):
    global x1, y1, x2, y2, x3, y3, x4, y4, k, imagen_casa_seleccion_de_ptos, seleccion_terminada
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen_casa_seleccion_de_ptos, (x, y), 3, (0, 0, 255), -1)
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
            imagen_casa_seleccion_de_ptos = cv2.imread('casa.jpg', cv2.IMREAD_COLOR)
            seleccion_terminada = True

imagen_casa_seleccion_de_ptos = cv2.imread('casa.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('imagen_casa_seleccion_de_ptos')
cv2.setMouseCallback('imagen_casa_seleccion_de_ptos', seleccion_de_puntos)

while(1):
    cv2.imshow('imagen_casa_seleccion_de_ptos', imagen_casa_seleccion_de_ptos)

    if seleccion_terminada == True:
        # Transformo la imagen de la casa
        pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
        pts2 = np.float32([[0, 0], [500, 0], [500, 400], [0, 400]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imagen_transformada = cv2.warpPerspective(imagen_casa_seleccion_de_ptos, matrix, (500, 400))
        cv2.imshow('imagen_transformada', imagen_transformada)
        cv2.imwrite('imagen_transformada.jpg', imagen_transformada)

        seleccion_terminada = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cv2.destroyAllWindows()