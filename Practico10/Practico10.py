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
        cv2.circle(imagen_seleccion_de_ptos, (x, y), 3, (0, 0, 255), -1) # Dibujo un círculo y guardo la posición
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

imagen_seleccion_de_ptos = imagen       # imagen_selección_de_ptos es la imagen que se mostrará y en la que seleccionaré todos los puntos
cv2.namedWindow('Seleccion de puntos')
cv2.setMouseCallback('Seleccion de puntos', seleccion_de_puntos)
cv2.imshow('Seleccion de puntos', imagen_seleccion_de_ptos)

# Se pide ingresar el ancho del objeto conocido
ancho_del_objeto = float(input('Ingrese el ancho del objeto conocido (cm): '))
alto_del_objeto = float(input('Ingrese el alto del objeto conocido (cm): '))
proporcion = alto_del_objeto/ancho_del_objeto

print('Seleccione las esquinas del objeto que conoce las dimensiones')

while (seleccion_terminada == False): # Refresco la imagen de selección de puntos hasta que termine de seleccionar los mismos
    cv2.waitKey(1)
    cv2.imshow('Seleccion de puntos', imagen_seleccion_de_ptos)

if seleccion_terminada == True:
    # Obtenemos la matriz M
    print(x1, y1)
    print(x2, y2)
    print(x3, y3)
    print(x4, y4)
    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    pts2 = np.float32([[x1, y1], [x2, y1], [x2, y1 + ((x2 - x1)*proporcion)], [x1, y1 + ((x2 - x1)*proporcion)]]) # Le doy estos valores para que la imagen transformada quede centrada con respecto a la imagen original
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imagen_seleccion_de_ptos = cv2.imread('Imagen.jpg', cv2.IMREAD_COLOR) # Vuelvo a cargar la imagen para que se borren los puntos dibujados
    imagen_transformada = cv2.warpPerspective(imagen_seleccion_de_ptos, matrix, (ancho, alto)) # Se transforma la imagen completa
    cv2.imwrite('imagen_transformada.jpg', imagen_transformada) # guardo la imagen
    imagen_seleccion_de_ptos = imagen_transformada # hago que la imagen de selección de puntos sea ahora la imagen transformada
    seleccion_terminada = False

print('Seleccione las esquinas del objeto nuevamente')
while (seleccion_terminada == False): # Ahora refresco la imagen transformada para que se vayan mostrando los puntos seleccionados
    cv2.waitKey(1)
    cv2.imshow('Seleccion de puntos', imagen_seleccion_de_ptos)

if seleccion_terminada == True:
    # Obtenemos la cantidad de pixeles por centímetro
    pixeles_por_cm = (x2 - x1) / ancho_del_objeto     # x2-x1, es un lado del papel glacé y este mide 10cm
    imagen_seleccion_de_ptos = cv2.imread('imagen_transformada.jpg', cv2.IMREAD_COLOR)  # Vuelvo a cargar la imagen para que se borren los puntos dibujados
    # Obtenemos la cantidad de pixeles por centímetro
    seleccion_terminada = False

# Ahora que ya hemos transformado la imagen para eliminar la perspectiva y ya hemos obtenido la cantidad de pixeles por centímetro, entramos en un bucle infinito en el que podremos medir las dimensiones de un objeto por cada vez que se ejecute el bucle
while(1):

    print('Seleccione las esquinas del objeto que desee medir')
    while (seleccion_terminada == False): # Refrescamos la imagen mientras se selccionan los puntos extremos del objeto a medir
        cv2.waitKey(1)
        cv2.imshow('Seleccion de puntos', imagen_seleccion_de_ptos)

    if seleccion_terminada == True:
        #Medimos un objeto
        ancho_objeto = (x2 - x1) / pixeles_por_cm
        alto_objeto = (y3 - y1) / pixeles_por_cm
        print('El ancho es de:' , ancho_objeto , 'cm')
        print('El alto es de:' , alto_objeto , 'cm')
        seleccion_terminada = False
        imagen_seleccion_de_ptos = cv2.imread('imagen_transformada.jpg', cv2.IMREAD_COLOR)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()