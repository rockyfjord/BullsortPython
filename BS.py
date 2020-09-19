# Script will read image and generate barcodes"""
import cv2 as cv
import numpy as np
from pytesseract import image_to_string
from PIL import Image
import re
from barcode import EAN13
from barcode.writer import ImageWriter


def main():
    print("Hello, Dr. Han!!!!!!!")
    img = Image.open('Images/ocrtest.jpg').convert('L')
    ret, img = cv.threshold(np.array(img), 125, 255, cv.THRESH_BINARY)
    img = Image.fromarray(img.astype(np.uint8))

    """here we are extracting 13 digit numbers that begin with 0108.
    We'll need an option to enter store number for beginning of string."""
    containerIDs = re.findall('0108[0-9]{9}', image_to_string(img))
    for id in containerIDs:
        print(id)
    for count, container in enumerate(containerIDs):
        ean = EAN13(container, writer=ImageWriter())
        ean.save('Images/Barcodes/{}'.format(count))


if (__name__ == '__main__'):
    main()
