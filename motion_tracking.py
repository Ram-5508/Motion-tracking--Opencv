# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:55:13 2019

@author: Lenovo
"""

import cv2

cap=cv2.VideoCapture('cars.mp4')

_,img1=cap.read()
_,img2=cap.read()

while 1:
    diff=cv2.absdiff(img1,img2)
    blur=cv2.GaussianBlur(diff,(5,5),0)
    gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    _,thres=cv2.threshold(gray,25,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thres,None,3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for con in contours:
        x,y,w,h=cv2.boundingRect(con)
        
        if cv2.contourArea(con)<1000:
            continue
        cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.drawContours(img1,contours,-1,(0,255,0),2)
    
    cv2.imshow('Image',img1)
    img1=img2
    _,img2=cap.read()
    
    k=cv2.waitKey(5) &0xff
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()