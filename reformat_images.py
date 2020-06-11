 #!/usr/bin/env python3
from PIL import Image
import os
import sys
source_folder = "/home/student-04-fc2745a2c9db/images/"
destination_folder = "/opt/icons/"

def reformat():
    for item in os.listdir(source_folder):
        if os.path.isfile(source_folder+item):
            im.convert("RGB")
            im = Image.open(source_folder+item)
            f, e = os.path.splitext(item)
 
            #reformat image by resizing it to 128x128 and rotating it by 90 degrees
            imResize = im.rotate(90).resize((128,128), Image.ANTIALIAS)

            #Save the reformated image to another folder in JPEG format
            imResize.save(destination_folder + f , 'JPEG', quality=90)

reformat()

