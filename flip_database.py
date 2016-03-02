from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os

path = "C:\\Users\\dfdf\\Google Drive\\deepID_matlab\\databases\\praticard_folds\\"
path_output = "C:\\Users\\dfdf\\Google Drive\\deepID_matlab\\databases\\praticard_folds_fliped\\"

count = 0
create = False

import os
import os.path
from PIL import Image


for dirpath, dirnames, filenames in os.walk(path):
    create = False
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        count+=1
        input = dirpath+'\\'+filename
        img = Image.open(input).transpose(Image.FLIP_LEFT_RIGHT)
        
        teste = dirpath.replace("praticard_folds", "praticard_folds_fliped")
        output = teste+'\\'+filename
        
        #print dirpath+'\\'+filename
        print teste+'\\'+filename
        #print os.path.dirname(teste)
        
        if(not create):
            os.makedirs(teste)
            create = True
        
        img.save(output)
        
print count