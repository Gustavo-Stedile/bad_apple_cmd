import cv2 as cv
import numpy as np
import os
import time

video = cv.VideoCapture('bad_apple.mp4')
while True:
    isTrue, frame = video.read()
    os.system('cls')

    frame = cv.resize(frame, (int(frame.shape[1] * .20), int(frame.shape[0] * .10)), interpolation=cv.INTER_AREA)
    
    for row in frame:
        print('                                                        ', end='', sep='')

        for column in row:
            if np.array_equal(column, [255, 255, 255]): print('*', end='', sep='')
            else: print(' ', end='', sep='')
        print('')

    time.sleep(0.01)