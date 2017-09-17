# import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
import time

hwin = win32gui.FindWindow(None,'Grand Theft Auto V') #it gets the process ID or as microsoft calls it 'window handle'

def grab_screen(region=None):
    # last_time = time.time()
    while(True):
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
        # This is image show which uses openCV
        # cv2.imshow('window',img)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(hwin, hwindc)
        win32gui.DeleteObject(bmp.GetHandle())
        # print('loop took {} seconds'.format(time.time()-last_time))
        # last_time = time.time()


grab_screen()
