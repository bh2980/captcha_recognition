import cv2
import numpy as np
import glob
import os

img_list = glob.glob(r'D:\Github\captcha_recognition\captcha\unlabled\*.png')

count = 1

kernel = np.ones((3, 3), np.uint8)

w = 28

index = 0

for i in img_list:

    img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)

    th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    dilation_image = cv2.dilate(th1, kernel, iterations=1)

    # cv2.imwrite('./'+ i.split('\\')[6] + '/' + str(1) + '.png', dilation_image)

    start = 5

    for count in range(4):
        gap = 8
        
        first = dilation_image[0:50, start:start+w].copy()
        cv2.imwrite(r'D:\Github\captcha_recognition\character\unlabeled\\' + str(index) +'.png', first)
        # cv2.imwrite('./' + i.split('\\')[6][count] + '_' + str(index) +'.png', first)

        # if i.split('\\')[6][count] == 'w' or i.split('\\')[6][count] == 'm' or i.split('\\')[6][count] == 'p':
        #     gap = 0
        
        # if i.split('\\')[6][count] == 'f':
        #     gap = 10

        # start = start + w - gap
        index += 1