from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os
import numpy as np



fname = "ERROR_ENROLL_OTHER.txt"
path = "C:\\Users\\dfdf\\Documents\\Imagens_DATABASE\\BENCHMARK\\faces\\BENCHMARK_1\\HIT_2_ENROLL\\HIT_2\\"
count = 0

aux = listdir(path)

with open(fname) as f:
    content = f.readlines()
    
for i in content:
    i = i.split("HIT_1\\")
    i = i[-1]
    print(count)
    count+=1
    rem = i.replace("_1.jpg","_2.jpg")
    print rem
    os.remove((path+rem).rstrip())
    #print i
    
    
#for j in aux:
#    print j
    
    
