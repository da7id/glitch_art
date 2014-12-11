import numpy
import cv2

image_to_edit = '5.jpg'
save_name = '5_edit.jpg'
black_value = 100;

img = cv2.imread(image_to_edit)
height = img.shape[0]
width = img.shape[1]
row = 0
column = 0

def sortByRow(img):
    return numpy.sort(img, axis=1)

def invert(img, file_name):
    img = (255-img)
    return img

def sortByColumn(img):
    return numpy.sort(img, axis=0)

def getLuminance(pixel):
    R = pixel[2]
    G = pixel[1]
    B = pixel[0]
    return (0.2126*R + 0.7152*G + 0.0722*B)

def blotDarkPixels(img):
    for row in range(0, img.shape[0]):
        for column in range(0, img.shape[1]):
            pixel = img[row][column]
            if getLuminance(pixel) < 150:
                img[row][column] = [0, 0, 0]
    return img

def sortColumn():
    x = column
    y = 0
    y_end = 0
    unsorted_pixels = numpy.array([0,0,0])

    while y_end < height-1:
        y = getFirstNonBlackY(x, y)
        y_end = getNextBlackY(x,y)

        if (y < 0):
            break

        sort_length = y_end - y
        
        for i in range (0, sort_length):
            unsorted_pixels = numpy.vstack((unsorted_pixels, img[y+i][x]))

        #print unsorted_pixels
        #unsorted_pixels.sort()
        numpy.sort(unsorted_pixels)
        sorted_pixels = unsorted_pixels

        for i in range(0, sort_length):
            # POTENTIALLY WRONG
            img[y+i][x] = sorted_pixels[i]

        y = y_end + 1
    #print sorted_pixels.shape



def getFirstNonBlackY(_x, _y):
    x = _x
    y = _y
    if y < height:
        while (getLuminance(img[y][x]) < black_value):
            y += 1
            if y >= height:
                return -1
    return y

def getNextBlackY(_x, _y):
    x = _x
    y = _y + 1
    if y < height:
        while (getLuminance(img[y][x]) > black_value):
            y += 1
            if y >= height:
                return height-1
    return y-1

while column <= width-1:
#while column <= 0:
    sortColumn()
    column += 1

cv2.imwrite(save_name, img)
