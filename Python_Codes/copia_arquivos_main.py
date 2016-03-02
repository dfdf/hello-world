from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os
import numpy as np

path = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\ORIGINAL\\processed\\"
path_train = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\ORIGINAL\\PROCESSED_TEST\\"


if not os.path.exists(path_train):
    os.makedirs(path_train)
    
name = "NEGATIVO_"
aux = listdir(path)
#aux = [path]
#copyfile(src, dst)
for mypath in aux:
    onlyfiles = [f for f in listdir(path+mypath) if isfile(join(path+mypath, f))]
    print(path+mypath)
    #print(onlyfiles)
    
    #onlyfiles = np.random.choice(onlyfiles, 500)
    print(len(onlyfiles))
    #if not os.path.exists(path_train+mypath):
    #    os.makedirs(path_train+mypath)
    count = 1
    for i in onlyfiles:
        print(count)
        if not os.path.exists(path_train+"\\"+name+mypath+"_"+str(count)+".jpg"):
        
            copyfile(path+mypath+"\\"+i, path_train+"\\"+name+mypath+"_"+str(count)+".jpg")
            print()
        else:
            print("Found...")
        count+=1
    
    
    
print("TOTAL PAIRS:")
print(count) 
    


