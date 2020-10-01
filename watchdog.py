import cv2
import numpy as np
import pandas as pd
from collections import Counter

train_data = np.load('training_data_takeoff.npy')
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

for data in train_data:
    img = data[0]
    print (img.shape)
    choice = data[1]
    cv2.imshow('test',img)
    print (choice)
    if cv2.waitKey(25) & 0XFF == ord('q'):
        cv2.destroyAllWindows()
        break
