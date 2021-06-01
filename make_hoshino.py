#wordcloudで適用するために、星野源さん上半身画像の背景をopencvで消す
import cv2
import numpy as np
import matplotlib.pyplot as plt

BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 100
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (1.0,0.0,0.0) 

img = cv2.imread('hoshino2.jpg') #グレイにしたい画像(肖像権のため載せない)
img1 = img[0 : 2100, 0: 2650]
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)  #グレースケールの画像を用意

#エッジを見つける
edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2) #グレースケール
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)
contour_info = []
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#輪郭を見つける
for c in contours:
        contour_info.append((
        c,
        cv2.isContourConvex(c),
        cv2.contourArea(c),
    ))
contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
max_contour = contour_info[0]

#一番大きい輪郭を使ってマスクを作る
mask = np.zeros(edges.shape)
cv2.fillConvexPoly(mask, max_contour[0], (255))

mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
mask_stack = np.dstack([mask]*3) 
mask_stack = mask_stack.astype('float32') / 255.0    
img1 = img1.astype('float32') / 255.0   

masked = (mask_stack * img1) + ((1-mask_stack) * MASK_COLOR) 
masked = (masked*255).astype('uint8')  
plt.imshow(img_a)
plt.axis("off")
plt.show()
