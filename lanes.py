import cv2
import numpy as np
import matplotlib.pyplot as plt

def make_points(image, line):
    slope, intercept = line
    y1 = int(image.shape[0])# bottom of the image
    y2 = int(y1*3/5)         # slightly lower than the middle
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return [[x1, y1, x2, y2]]

def average_slope_intercept(image, lines):
    left_fit    = []
    right_fit   = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1,x2), (y1,y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0: # y is reversed in image
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    # add more weight to longer lines
    left_fit_average  = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line  = make_points(image, left_fit_average)
    right_line = make_points(image, right_fit_average)
    averaged_lines = [left_line, right_line]
    return averaged_lines

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
avg_lines = average_slope_intercept(img , lines)
line_image = display_lines(img, avg_lines)
combo_image = cv2.addWeighted(img, 0.8, line_image, 1, 1)
plt.imshow(combo_image)
plt.show()
