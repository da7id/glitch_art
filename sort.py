import numpy
import cv2

def sort_by_row(image):
    return numpy.sort(image, axis=1)

def invert(image, file_name):
    image = (255-image)
    cv2.imwrite(file_name, image)

def sort_by_column(image):
    return numpy.sort(image, axis=0)

def get_luminance(pixel):
    R = pixel[2]
    G = pixel[1]
    B = pixel[0]
    return (0.2126*R + 0.7152*G + 0.0722*B)

image = cv2.imread('image12.png')

for row in range(0, image.shape[0]):
    for column in range(0, image.shape[1]):
        pixel = image[row][column]
        if get_luminance(pixel) < 150:
            image[row][column] = [0, 0, 0]

cv2.imwrite('test.png', image)
