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
    masked_image = cv2.bitwise_and(img,mask)
    return masked_image
def display_lines(img,lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image


img = cv2.imread("images/road.jpg")
gray_img = cv2.imread("images/road.jpg",0)
canny = edge_detection(img)
roi = roi(canny)
lines = cv2.HoughLinesP(roi, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
line_image = display_lines(img, lines)
combo_image = cv2.addWeighted(img, 0.8, line_image, 1, 1)
plt.imshow(combo_image)
plt.show()
