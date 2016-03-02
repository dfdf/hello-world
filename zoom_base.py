from PIL import Image, ImageOps
from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os

path = "E:\\webface_expanded\\100\\"

#IN = -5
#OUT = 5
mode = -5
count = 0
size = 100,100
create = False
output_folder = "praticard_folds_fliped_zoom_out"
format_file = ".jpg"
origin_folder = "praticard_folds_fliped"

#0000045/007-r.jpg 0
import os
import os.path
from PIL import Image


for dirpath, dirnames, filenames in os.walk(path):
    create = False
    for filename in [f for f in filenames if f.endswith(format_file)]:
        count+=1
        input = dirpath+'\\'+filename
       
        print(input)
        
        img = Image.open(input)
        
        img_with_border_1 = ImageOps.expand(img,border=-5,fill='black')
        img_with_border_2 = ImageOps.expand(img,border=5,fill='black')
        
        #Opcao pro futuro
        #img_with_border = ImageOps.solarize(img_with_border, threshold=128) 
        #if(mode > 0):
        img_with_border_1.thumbnail(size, Image.ANTIALIAS)
        #else:
        img_with_border_2 = img_with_border_2.resize(size, Image.ANTIALIAS)
            

        #print("Image 1:",img.size)
        #print("Image 2:",img_with_border.size)

    
        #img_with_border.save('imaged-with-border.png')
        
        #teste = dirpath.replace(origin_folder, output_folder)
        #output = teste+'\\'+filename
        
        #print dirpath+'\\'+filename
        #print teste+'\\'+filename
        #print os.path.dirname(teste)
        
        #if(not create):
        #    os.makedirs(teste)
        #    create = True
        
        list = filename.split(".")
        
        img_with_border_1.save(dirpath+'\\'+list[0]+"-i.jpg")
        img_with_border_2.save(dirpath+'\\'+list[0]+"-o.jpg")

#with open("Output.txt", "w") as text_file:
#    text_file.write(aux_output)           
print count



