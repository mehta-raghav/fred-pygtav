import numpy as np
from PIL import ImageGrab
import time
import cv2
from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib as mpl
import matplotlib.animation as anim

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
arr = [[0 for n in range(1)] for m in range(100)]

def screen_record(i): 
    last_time = time.time()
    printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    z = 0
    x = 1
    arr[z].append(x)
    arr[z].append(time.time()-last_time)
    z = z + 1
    ex = []
    y = []
    for line in arr :
        #printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('{}'.format(time.time()-last_time))

        ex.append(x)
        y.append(time.time()-last_time)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
        x = x + 1
    ax.clear()
    ax.plot(ex,y,color='red')
    font = {'weight' : 'bold', 'size' : 18}
    mpl.rc('font',**font)
    plt.title('Time Analysis Graph for PIL')
    mpl.rcParams.update({'font.size': 17})
    plt.xlabel('Iteration')
    plt.ylabel('Grab time')
    #ax.legend(['Win32', 'PIL'], loc = 'upper right')
ani = anim.FuncAnimation(fig,screen_record,interval=50)
plt.show()
