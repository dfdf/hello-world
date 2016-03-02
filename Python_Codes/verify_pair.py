from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os
import numpy as np


path = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\BENCHMARK\\faces\\BENCHMARK_1\\HIT\\"
path_dest = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\BENCHMARK\\faces\\BENCHMARK_1\\HIT_POSITIVO_1\\"
path_dest_2 = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\BENCHMARK\\faces\\BENCHMARK_1\\HIT_POSITIVO_2\\"
aux = listdir(path)
counter = 0
for mypath in aux:
    match = False
    src = path+mypath
    #Se o arquivo ja foi copiado, pule
    if(not os.path.isfile(path+mypath)):
        continue
        
    
    list = mypath.split("_")
    
    if(list[0] == "CADASTRO"):
            continue
             
    aux_2 = listdir(path)
    for i in aux_2:
        
        i = i.split("_")
        if(i[0] == "CADASTRO"):
            continue
        counter+=1
        
        #Copie a imagem
        dest = path_dest + "_".join(list)
        if(list[1] == i[1] and list[2] != i[2]):
            #copyfile(src, dest)
            print(src)
            print(dest)
            os.rename(src, dest)
            
            src = path+"_".join(i)
            dest = path_dest_2 + "_".join(i)
            print(src)
            print(dest)
            os.rename(src, dest)
            match = True
            
    
    if(match):
        print("OK");
    else:
        counter +=1
        os.remove(path+"_".join(list))
        aux_2 = listdir(path)
        print("FALSE")
        
    print list
    
print counter
        