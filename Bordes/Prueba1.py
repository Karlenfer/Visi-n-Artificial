import cv2
import numpy as np

img = cv2.imread('Original.png')

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (1, 1), 1)
#cv2.imshow('Gaussian', gray)

edged = cv2.Canny(img, 0, 255)
cv2.imshow('edged', edged)
cv2.imwrite('edged.png', edged)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])



k = 0

for c in contours:
    b = np.asarray(contours[k])
    k = k+1
    e = 0

    if ((len(b)) > 1000):
        tl_x = 99999
        tl_y = 99999
        tr_x = 0
        tr_y = 99999
        br_x = 0
        br_y = 0
        bl_x = 99999
        bl_y = 0
        while ((len(b)) > e):
            x, y = np.hsplit(b[e], 2)
            e = e+1
            if(tl_x > x):
                if(tl_y > y):
                    tl_x = x
                    tl_y = y
            if(tr_x < x):
                if(tr_y > y):
                    tr_x = x
                    tr_y = y
            if(br_x < x):
                if(br_y < y):
                    br_x = x
                    br_y = y
            if(bl_x > x):
                if(bl_y < y):
                    bl_x = x
                    bl_y = y
            #print(x)
            #print(y)
        cv2.circle(img, (tl_x, tl_y), 3, (0, 0, 255), -1)
        cv2.circle(img, (tr_x, tr_y), 3, (0, 0, 255), -1)
        cv2.circle(img, (br_x, br_y), 3, (0, 0, 255), -1)
        cv2.circle(img, (bl_x, bl_y), 3, (0, 0, 255), -1)

cv2.imshow('edged2', img)
cv2.imwrite('edged2.png', img)







laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('laplacian', laplacian)
cv2.imwrite('laplacian.png', laplacian)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
cv2.imshow('sobelx', sobelx)
cv2.imwrite('sobelx.png', sobelx)


while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()