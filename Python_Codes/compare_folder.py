from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os
import numpy as np

path_1 = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\BENCHMARK\\faces\\BENCHMARK_2\\STEP 2\\STEP 3\HIT_2\\"
path_2 = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\BENCHMARK\\faces\\BENCHMARK_2\\STEP 2\\STEP 3\HIT_1\\"


for i in listdir(path_1):
    match = False
    list = i.split("_")
    
    
    for j in listdir(path_2):
        list_2 = j.split("_")
        
        if(list_2[1] == list[1]):
            match = True
            
    if(not match):
        print("FILE NOT FOUND " + "_".join(list))
        os.remove(path_1+i)
        