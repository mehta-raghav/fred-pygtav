import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
import time
from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib as mpl
import matplotlib.animation as anim


'''def save_file(arr,z): #saves numpy array of bitmaps in files of ~1.6 MB(10 bmps)
    file = "training_data"
    file = file + str(z)
    np.save(file,arr)'''
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
arr = [[0 for n in range(1)] for m in range(100)]

def screen_record(region=None):
    last_time = time.time()
    np_arr = np.zeros(shape=(10,120,160))
    z = 0
    count = 0
    x = 1
    arr[z].append(x)
    arr[z].append(time.time()-last_time) 
    ex = []
    y = []
    for line in arr:
        #currently hardcoding the values for 800x600, have to find another way to get the values
        top = 0
        left = 40
        height = 600
        width = 800

        #shell=win32com.client.Dispatch("Wscript.Shell")
        #success = shell.AppActivate('Grand Theft Auto V')
        hwin = win32gui.FindWindow(None,'Grand Theft Auto V')
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
        '''dim = (160,120)
        res = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        res = cv2.cvtColor( res, cv2.COLOR_RGB2GRAY )'''
        #print (res.shape)

        #np_arr[z] = res
        z = z + 1
        '''if (z==9):
            save_file(np_arr,count)
            count = count + 1'''
        
        cv2.imshow('window',img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(hwin, hwindc)
        win32gui.DeleteObject(bmp.GetHandle())
        print('loop took {} seconds'.format(time.time()-last_time))

        ex.append(x)
        y.append(time.time()-last_time)
        last_time = time.time()
        x = x + 1
    ax.clear()
    ax.plot(ex,y,color='red')
    font = {'weight' : 'bold', 'size' : 18}
    mpl.rc('font',**font)
    plt.title('Time Analysis Graph for Win32')
    mpl.rcParams.update({'font.size': 17})
    plt.xlabel('Iteration')
    plt.ylabel('Grab time')

ani = anim.FuncAnimation(fig,screen_record,interval=50)
plt.show()
#screen_record()

