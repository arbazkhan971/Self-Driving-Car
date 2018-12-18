import cv2
import numpy as np
import matplotlib.pyplot as plt

def edge_detection(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    canny = cv2.Canny(blur,50,150)
    return canny
def roi(img):   #region of interest which is triangle here which may be dfferent in your case depends on images which you take for finding edges using canny
    bottom = img.shape[0]
    triangle = np.array([[(220,bottom),(1020,bottom),(570,250)]])    #size of traingle with vertices
    mask = np.zeros_like(img)                      #mask which is completely blacked
    cv2.fillPoly(mask , triangle,255)
    return mask



img = cv2.imread("images/road.jpg",0)
canny = edge_detection(img)
roi=roi(canny)
plt.imshow(roi)
plt.show()
