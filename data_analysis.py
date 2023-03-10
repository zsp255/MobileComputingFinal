import pytesseract
from PIL import Image
from PIL import ImageEnhance, ImageFilter
import numpy as np
import os
import glob

list = sorted(glob.glob("*.png"))


for pic in list:

    ## open image and make it larger
    image = Image.open(pic)
    (width, height) = (image.width * 3, image.height * 3)
    image = image.resize((width, height))

    ## apply black and white filter
    # image = image.convert('L')

    ## apply image enhancement
    # image = image.filter(ImageFilter.MinFilter)
    
    # sharpness = ImageEnhance.Sharpness(image)    
    # image = sharpness.enhance(15)

    # contrast = ImageEnhance.Contrast(image)
    # image = contrast.enhance(1.2)
    # image = image.convert('L')

   
    
    # dispaly image if necessary
    #image.show()
    
    # recognize text in the image using pytesseract
    text = pytesseract.image_to_string(image)

    # print the text
    print(text)
