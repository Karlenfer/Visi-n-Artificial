import cv2
import numpy as np

MIN_MATCH_COUNT = 10

img1 = cv2.imread('ojota1.jpg')
cv2.imshow('img1', img1)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('ojota2.jpg')
cv2.imshow('img2', img2)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Inicializamos el detector y el descriptor
sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

img1=cv2.drawKeypoints(gray1,kp1,img1)
cv2.imwrite('sift_keypoints.jpg',img1)

matcher = cv2.BFMatcher (cv2.NORM_L2)

matches = matcher.knnMatch(des1, des2, k=2)

# Guardamos los buenos matches usando el test de razón de Lowe
good = [ ]
for m, n in matches :
    if m.distance < 0.70*n.distance:
        good.append(m)

if(len(good) > MIN_MATCH_COUNT):
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0) # Computamos la homografía con RANSAC

wimg2 = cv2.warpPerspective(img2, H, (img1.shape[1], img1.shape[0]))

# Mezclamos ambas imágenes
alpha = 0.5
blend = np.array(wimg2 * alpha + img1 * (1 - alpha), dtype=np.uint8)

cv2.imshow('blend', blend)

while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()