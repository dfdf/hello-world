from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os
import numpy as np

path = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\ORIGINAL\\cert_negativo\\"
path_train = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\ORIGINAL\\processed\\"


if not os.path.exists(path_train):
    os.makedirs(path_train)
    
aux_output = ""
aux = listdir(path)

for mypath in aux:
    onlyfiles = [f for f in listdir(path+mypath) if isfile(join(path+mypath, f))]
    print(path+mypath)
    print(onlyfiles)
    
    #if not os.path.exists(path_train+mypath):
    #    os.makedirs(path_train+mypath)
    
    count = 1
    if(len(onlyfiles) > 2):
        print("MAIS QUE 2")
        continue
    for i in onlyfiles:
        aux_output += mypath+str(count)+".jpg"
        aux_output += "\n"
        #print(count)
        if(count >= 3):
            break
        if not os.path.exists(path_train+"\\"+mypath+"\\"+str(count)+".jpg"):
            if not os.path.exists(path_train+"\\"+mypath+"\\"):
                os.makedirs(path_train+"\\"+mypath+"\\")
            copyfile(path+mypath+"\\"+i, path_train+"\\"+mypath+"\\"+str(count)+".jpg")
            print()
        else:
            print("Found...")
        count+=1
    
    
with open("Output.txt", "w") as text_file:
    text_file.write(aux_output)    
print("TOTAL PAIRS:")
print(count) 
    


