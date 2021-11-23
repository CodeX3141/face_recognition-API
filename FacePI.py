import face_recognition
import os
import numpy as np
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cv2
import main
import random


def rgbValue(arr):
    return [arr[0],arr[1],arr[2]]

def nothing():
    return 0
def borderFaces(filename,thickness,color):

    image = face_recognition.load_image_file(filename)
    face_loc = face_recognition.face_locations(image)

    h,w = PIL.Image.open(filename).size
    thickness = int(((h+w)/2) * 0.005)


    img = PIL.Image.open(filename)

    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)

    # draw.text((x, y),"Sample Text",(r,g,b))


    for i in range(len(face_loc)):
        y,x,y2,x2 = face_loc[i]

        size = max(x2 - x,y2 - y)

        for i2 in range(x - x2):
            try:

                for z in range(thickness):
                    img.putpixel((x-i2,y+z),color)
            except Exception:
                nothing()

        for i2 in range(y2 - y):
            try:
                for z in range(thickness):
                    img.putpixel((x+z, y + i2), color)
            except Exception:
                nothing()

        for i2 in range(y2 - y):
            try:
                for z in range(thickness):
                    img.putpixel((x - size + z, y + i2), color)
            except Exception:
                nothing()

        for i2 in range(x - x2 - thickness):
            try:
                for z in range(thickness):
                    img.putpixel((x - i2, y + size + z - thickness), color)
            except Exception:
                nothing()
        font = ImageFont.truetype('Game Of Squids.ttf', int((x-x2)*0.17))
        draw.text((x2, y2), "Person " + str(i + 1), color, font=font)




    return img

def highlightFaces(filename):

    image = face_recognition.load_image_file(filename)
    face_loc = face_recognition.face_locations(image)



    img = PIL.Image.open(filename)
    for i in face_loc:
        x = i[1]
        y = i[0]
        x2 = i[3]
        y2 = i[2]



        arr = main.AllComb(x-x2,y2-y)
        for i in arr:
            dx = i[0]
            dy = i[1]
            [r,g,b] = rgbValue(img.getpixel((x-dx,y+dy)))
            img.putpixel((x-dx,y+dy),(r,0,0))



    return img
def findperson(filename,filename2):
    image = face_recognition.load_image_file(filename)
    face_encoding =  face_recognition.face_encodings(image)[0]

    #TBC = to be compared
    imageTBC = face_recognition.load_image_file(filename2)
    faceEncodings = face_recognition.face_encodings(imageTBC)

    tbr = False

    for i in faceEncodings:
        result = face_recognition.compare_faces([face_encoding],i)

        if result[0]:
            tbr = True

    return tbr

def findpersonEnc(face_encoding,filename2):


    #TBC = to be compared
    imageTBC = face_recognition.load_image_file(filename2)
    faceEncodings = face_recognition.face_encodings(imageTBC)

    tbr = False

    for i in faceEncodings:
        result = face_recognition.compare_faces([face_encoding],i)

        if result[0]:
            tbr = True

    return tbr

def pullFaces(filename):
    image = face_recognition.load_image_file(filename)
    face_loc = face_recognition.face_locations(image)
    images = []



    img = PIL.Image.open(filename)
    for i in face_loc:

        y,x,y2,x2 = i



        im = PIL.Image.new(mode='RGB',size = (x - x2,y2 - y))


        arr = main.AllComb(x - x2, y2 - y)
        for i in arr:
            dx = i[0]
            dy = i[1]
            [r, g, b] = rgbValue(img.getpixel((x - dx, y + dy)))
            im.putpixel((x - x2 - dx - 1, dy), (r, g, b))

        images.append(im)

    return images

def massPullFaces(image_dir,result_dir):

    dir = image_dir
    dir2 = result_dir

    files = os.listdir(dir)


    for i2 in files:

        try:
            arr = pullFaces(dir + i2)
            os.mkdir(dir2 + i2 + '_')
            for i in range(len(arr)):

                arr[i].save(dir2 + i2 + '_' + '/' + i2 + str(i+1)+'.jpg')

        except Exception:
            nothing()




























