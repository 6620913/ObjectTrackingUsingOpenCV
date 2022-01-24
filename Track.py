import cv2 as cv
import numpy as np

def nothing(x):
    pass
cv.namedWindow('image')
cv.createTrackbar('lh','image',110,255,nothing)
cv.createTrackbar('ls','image',50,255,nothing)
cv.createTrackbar('lv','image',50,255,nothing)

cv.createTrackbar('hh','image',130,255,nothing)
cv.createTrackbar('hs','image',255,255,nothing)
cv.createTrackbar('hv','image',255,255,nothing)

lh=10
ls=10
lv=10
hh=20
hs=20
hv=20


cap = cv.VideoCapture(0)

while(1):
    lh = cv.getTrackbarPos('lh','image')
    ls = cv.getTrackbarPos('ls','image')
    lv = cv.getTrackbarPos('lv','image')
    hh = cv.getTrackbarPos('hh','image')
    hs = cv.getTrackbarPos('hs','image')
    hv = cv.getTrackbarPos('hv','image')
    ret ,frame = cap.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_detect = np.array([lh,ls,lv])
    upper_detect = np.array([hh,hs,hv])

    mask = cv.inRange(hsv,lower_detect,upper_detect)

    res = cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k=cv.waitKey(5)&0xFF
    if k==27:
        break
cv.destroyAllWindows()
