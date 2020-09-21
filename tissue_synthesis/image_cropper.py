import glob
import os
from PIL import Image
import numpy as np

cmask_path = "C:/Users/Srijay/Desktop/Warwick/Datasets/CRAG/Texture_Synthesis/color_mask.png"
mask_path = "C:/Users/Srijay/Desktop/Warwick/Datasets/CRAG/Texture_Synthesis/mask.png"

output_dir = "C:/Users/Srijay/Desktop/Warwick/Datasets/CRAG/Texture_Synthesis/color_mask_patches"

if not os.path.exists(output_dir):
        os.makedirs(output_dir)

patch_size = 256
stride = 200

def CropImage(cmask_path,mask_path):

    image_initial = os.path.split(cmask_path)[1]

    cmask = Image.open(cmask_path).convert('RGB')
    mask = Image.open(mask_path)

    width, height = cmask.size

    x = 0
    y = 0
    right = 0

    while (y < height):
        while (right < width):
            left = x
            top = y
            right = left + patch_size
            bottom = top + patch_size
            if (right > width):
                offset = right - width
                right -= offset
                left -= offset
            if (bottom > height):
                offset = bottom - height
                bottom -= offset
                top -= offset

            mask_crop = mask.crop((left, top, right, bottom))
            mask_crop_np = np.asarray(mask_crop)

            if(np.mean(mask_crop_np) == 0):
                crop_name = image_initial + "_" + str(x) + "_" + str(y) + ".png"
                output_path = os.path.join(output_dir, crop_name)
                cmask_crop = cmask.crop((left, top, right, bottom))
                cmask_crop.save(output_path)

            x += stride

        x = 0
        right = 0
        y += stride

CropImage(cmask_path,mask_path)