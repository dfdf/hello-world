from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os
import numpy as np

path = "E:\\webface_expanded\\100\\"
    
aux = listdir(path)
for mypath in aux:
    onlyfiles = [f for f in listdir(path+mypath) if isfile(join(path+mypath, f))]
    print(path+mypath) #E:\webface_expanded\100\0000045
    print(onlyfiles) #['001-l-i.jpg', '001-l-o.jpg', '001-l.jpg', '001-r-i.jpg'
    
    for files in onlyfiles:
        aux_output += mypath+str(count)+".jpg"
        aux_output += "\n"
    #if not os.path.exists(path_train+mypath):
    #    os.makedirs(path_train+mypath)
   
    
    
with open("Output.txt", "w") as text_file:
    text_file.write(aux_output)    
print("TOTAL PAIRS:")
print(count) 
    


