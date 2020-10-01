import cv2
import time
import numpy as np
import win32gui, win32ui, win32con, win32api


hwin = win32gui.FindWindow(None,'Grand Theft Auto V')#it gets the process ID or as microsoft calls it 'window handle'
rect = win32gui.GetWindowRect(hwin)


def grab_screen():
    while(True):
        x = rect[0]
        y = rect[1]
        left = 0
        top = 40
        height = rect[3] - y - top
        width = rect[2] - x   
        hwindc = win32gui.GetWindowDC(hwin)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, width, height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY) 
        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (height,width,4)
        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(hwin, hwindc)
        win32gui.DeleteObject(bmp.GetHandle())
        #print('loop took {} seconds'.format(time.time()-last_time))
        #last_time = time.time()
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
