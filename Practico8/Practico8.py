import cv2
import numpy as np

seleccion_terminada = False
k = 0
x1, y1 = -1, -1
x2, y2 = -1, -1
x3, y3 = -1, -1

def seleccion_de_puntos(event, x, y, flags, param):
    global x1, y1, x2, y2, x3, y3, k, imagen_ventana_seleccion_de_ptos, seleccion_terminada
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen_ventana_seleccion_de_ptos, (x, y), 3, (0, 0, 255), -1)
        if k == 0:
            x1, y1 = x, y
            k = 1
        elif k == 1:
            x2, y2 = x, y
            k = 2
        else:
            x3, y3 = x, y
            k = 0
            imagen_ventana_seleccion_de_ptos = cv2.imread('ventana.jpg', cv2.IMREAD_COLOR)
            seleccion_terminada = True

imagen_ventana_seleccion_de_ptos = cv2.imread('ventana.jpg', cv2.IMREAD_COLOR)
imagen_campo = cv2.imread('fondowin.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('imagen_ventana_seleccion_de_ptos')
cv2.setMouseCallback('imagen_ventana_seleccion_de_ptos', seleccion_de_puntos)


while(1):
    cv2.imshow('imagen_ventana_seleccion_de_ptos', imagen_ventana_seleccion_de_ptos)

    if seleccion_terminada == True:

        # Transformo la imagen del campo para que tome el tamaño de la ventana
        rows, cols, ch = imagen_campo.shape
        pts1 = np.float32([[0, 0], [cols, 0], [cols, rows]])
        pts2 = np.float32([[x1, y1], [x2, y2], [x3, y3]])
        matrix = cv2.getAffineTransform(pts1, pts2)
        imagen_recortada = cv2.warpAffine(imagen_campo, matrix, (cols, rows))

        # Acá se juntan las imágenes
        imagen_ventana = cv2.imread('ventana.jpg', cv2.IMREAD_COLOR)
        filas, columnas, ch1 = imagen_ventana.shape
        campo_recortado_a_colocar = imagen_recortada[0:filas, 0:columnas]
        paisaje_recortado_gray = cv2.cvtColor(campo_recortado_a_colocar, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(paisaje_recortado_gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        imagen_ventana = cv2.bitwise_and(imagen_ventana, imagen_ventana, mask=mask_inv)
        imagen_final = cv2.add(imagen_ventana, campo_recortado_a_colocar)
        cv2.imshow('imagen_final', imagen_final)
        cv2.imwrite('imagen_final.jpg', imagen_final)

        seleccion_terminada = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2 . destroyAllWindows()