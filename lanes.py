import cv2

img = cv2.imread("images/1258603797_preview_Road.jpg",0)

blur = cv2.GaussianBlur(img,(5,5),0)
canny = cv2.Canny(blur,50,150)
cv2.imshow("Real line images",canny)
cv2.waitKey(0)
cv2.destroyAllwindows()
