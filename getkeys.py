import time
import win32api as wapi


def custom_ord(a):
    if (a == '8'):
        return 0x68
    elif (a == '6'):
        return 0x66
    elif (a =='5'):
        return 0x65
    elif (a =='4'):
        return 0x64
    else:
        return ord(a)

    
keyList = ["\b"]
for _ in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(_)

    
def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(custom_ord(key)):
            keys.append(key)
    return keys
