import os
import cv2
import time
import numpy as np
from getkeys import key_check
from screengrab import grab_screen


def keys_to_output(keys):
    '''Convert keys to a multi-hot array boolean values.
             [W,S,A,D,8,4,5,6]'''
    
    output = [0,0,0,0,0,0,0,0]

    if 'W' in keys:
        output[0] = 1
    if 'A' in keys:
        output[1] = 1
    if 'S' in keys:
        output[2] = 1
    if 'D' in keys:
        output[3] = 1
    if "8" in keys:
        output[4] = 1
    if "4" in keys:
        output[5] = 1
    if "5" in keys:
        output[6] = 1
    if "6" in keys:
        output[7] = 1
    return output


def load_data(file_name):
    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        training_data = list(np.load(file_name))
    else:
        print('File does not exist, starting fresh!')
        training_data = []
    return training_data


def countdown():
    for i in list(range(5))[::-1]:
        print(f'Value of i is : {si+1}')
        time.sleep(1)

        
def main():
    file_name = 'training_data_takeoff'
    training_data = load_data(file_name)
    
    paused = False
    
    print('Initialising Data Collection in:')
    countdown()
    while True:
        if not paused:
            try:
                screen = grab_screen()
                screen = cv2.resize(screen, (240,135), interpolation = cv2.INTER_AREA)
                output = keys_to_output(key_check())
                print (f'Output is : {output}')
                training_data.append([screen,output])
                if len(training_data) % 1000 == 0:
                    print(f'Length of training data is : {len(training_data)}')
                    np.save(file_name,training_data)
            except:
                print ("Window not available. Please try again")

        keys = key_check()
        if 'T' in keys:
            if paused:
                countdown()
                paused = False
                print('Unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


if __name__ == '__main__':
    main()
