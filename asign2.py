import cv2
import numpy as np
# Group member: Jérémie Perrault; Ziyi Wang; Xin Wang



#histogram stretch function
def histogram_stretch(input):       
    img_equ = cv2.equalizeHist(input)
    return img_equ

#power law transformation function
def power_law(input):
    im = input/255.0
    img_power = cv2.pow(im,1.5)
    return img_power

#log transformation function
def log_trans(input):
    img_log = (np.log(input+1)/(np.log(1+np.max(input))))*255
    img_log = np.array(img_log,dtype=np.uint8)
    return img_log

#average mask function
def average(input):
    img_average =  cv2.blur(input,(5,5))
    return img_average

#gaussian mask function
def gaussian(input):
    img_gaussian = cv2.GaussianBlur(input,(5,5),0)
    return img_gaussian

#median mask function
def median(input):
    img_median=cv2.medianBlur(input,3)
    return img_median

#sobel edge detector
def sobel(input):
    sobelx = cv2.Sobel(input,cv2.CV_8U,1,0)  
    sobely = cv2.Sobel(input,cv2.CV_8U,0,1)
    edgeX = np.uint8(np.absolute(sobelx))
    edgeY = np.uint8(np.absolute(sobely))
    img_sobel = cv2.bitwise_or(edgeX, edgeY)
    return img_sobel

#prewitt edge detector
def prewitt(input):
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(input, -1, kernelx)
    img_prewitty = cv2.filter2D(input, -1, kernely)
    edge1X = np.uint8(np.absolute(img_prewittx))
    edge1Y = np.uint8(np.absolute(img_prewitty))
    img_prewitt = cv2.bitwise_or(edge1X, edge1Y)
    return img_prewitt


#main function
def main():
    #Choose the image
    print ('Welcome! Please choose from the following images(Enter number):1, Building.pgm 2, MRI.pgm 3, peppers.pgm')
    imgnum=input()
   
    if imgnum=='1':
            res = cv2.imread('Building.pgm',0)

    if imgnum=='2':
            res = cv2.imread('MRI.pgm',0)

    if imgnum=='3':
            res = cv2.imread('peppers.pgm',0)

    #Choose the techniques
    while 1:
        
        print ('Please choose from the following techniques(Enter number): 1, Histogram Stretch 2, Power Law Transform 3, Log Transform 4, Average Mask 5, Gassian Mask 6, Median Mask 7, Sobel Detector 8, Prewitt Detector 9, Stop' )
        choice= input()

        if choice=='1':
            res=histogram_stretch(res)
        
        if choice=='2':
            res=power_law(res)

        if choice=='3':
            res=log_trans(res)

        if choice=='4':
            res=average(res)

        if choice=='5':
            res=gaussian(res)
    
        if choice=='6':
            res=median(res)

        if choice=='7':
            res=sobel(res)

        if choice=='8':
            res=prewitt(res)
        
        if choice=='9':
            cv2.imshow('Result', res)
            break
            
     
    cv2.waitKey(0)

main()