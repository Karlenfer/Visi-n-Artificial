import cv2
import numpy as np

drawing = False # true if mouse is pressed
ix, iy = -1, -1
fx, fy = -1, -1

def draw_circle(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, img_mostrar
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img_mostrar = cv2.imread('auto.jpg', cv2.IMREAD_COLOR)
            cv2.rectangle(img_mostrar, (ix, iy), (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx, fy = x, y
        img_mostrar = cv2.imread('auto.jpg', cv2.IMREAD_COLOR)
        cv2.rectangle(img_mostrar, (ix, iy), (x, y), (0, 255, 0), 2)


crop_img = cv2.imread('auto.jpg', cv2.IMREAD_COLOR)
img_mostrar = cv2.imread('auto.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img_mostrar)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('r'):
        crop_img = cv2.imread('auto.jpg', cv2.IMREAD_COLOR)
        img_mostrar = cv2.imread('auto.jpg', cv2.IMREAD_COLOR)
    if k == ord('g'):
        print(ix, fx, iy, fy)
        crop_img = crop_img[iy:fy, ix:fx]
        cv2.imwrite('Imagen_recortada.jpg', crop_img)
    elif k == ord('q'):
        break

cv2 . destroyAllWindows()