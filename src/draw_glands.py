import matplotlib.pyplot as plt
from skimage.draw import random_shapes
import numpy as np
import random
import matplotlib
import os

size = 728
num_images = 1
outpath = "C:/Users/Srijay/Desktop/Warwick/Datasets/CRAG/glands"

for k in range(0,num_images):
    gland_mask, _ = random_shapes((size, size),
                              min_shapes=10,
                              max_shapes=30,
                              min_size=70,
                              max_size=100,
                              num_channels=3,
                              shape='ellipse',
                              multichannel=True,
                              intensity_range=((128, 128),))

    random_mask = gland_mask
    '''
    random_mask = np.empty([size,size,3])

    w,h,d = random_mask.shape

    for i in range(0,w):
        for j in range(0,h):
            if(gland_mask[i][j][0]==128):
                random_mask[i][j] = [0, 255, 0]
            elif(random.randint(0, 10)==0):
                random_mask[i][j] = [0,0,255] #blue background
            else:
                random_mask[i][j] = [255,0,0] #stroma
    '''
    print("Done")
    random_mask = random_mask/255.0
    print("Done")
    imname = "synthetic_"+str(k)
    matplotlib.image.imsave(os.path.join(outpath,imname), random_mask)