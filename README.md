#USE : Install the repo in your folder via 'git clone' command . 
import using import FacePI.
Use the desired function with FacePI.function(parameters)

#List of functions:

1.borderFaces - highlights the faces in an image by creating a frame around the faces .
parameters - filename , color(color of border),label (boolean , wether faces should have label)
returns - PIL image

2.highlightFaces - makes part of images with faces negative . parameters - filename 
return - PIL image

3.findperson - Locates wether a person is in a photo or not 
parameters - filename(file of photo containing only the persons face) , filename2(image in which person is to be found)
returns - boolean

4.findpersonEnc - Same as above .
parameters - face_encoding(face encoding of person to be found),filename2(image in which person is to be found) 
returns - boolean

5.pullFaces - Creates separate images of the faces found in the photo
parameters - filename(photo to be analysed)
returns - List containing PIL image objects

