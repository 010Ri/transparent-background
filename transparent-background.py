import cv2
import numpy as np
import os
import glob

images = glob.glob('/Users/user/Desktop/pngs/*.png')
for image in images:
    file_name = os.path.splitext(os.path.basename(image))[0]

    target = cv2.imread(image)
    targetRGBA = cv2.cvtColor(target, cv2.COLOR_BGR2BGRA)
    bright = np.array([204, 204, 204, 255])
    dark = np.array([255, 255, 255, 255])
    mask_image = cv2.inRange(targetRGBA, bright, dark)
    transparented_image = cv2.bitwise_not(targetRGBA, targetRGBA, mask = mask_image)
        
    cv2.imwrite('/Users/user/Desktop/transparented/' + file_name + '_transparented.png', transparented_image)