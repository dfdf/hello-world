from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os
import numpy as np



fname = "RESULT_ONE_TO_MANY.txt"
count = 0
match = 0

with open(fname) as f:
    content = f.readlines()
    
for i in content:
    i = i.split(";")
    
    #print("----")
    if(i[1] == i[2].split(',')[0]):
        match+=1
    else:
        print(i[0])
        print(i[2].split(',')[0])
        print(i[1])
    count+=1
    
print(match)
print(count)
print("FINAL :"+ str(((1.0*match)/count)*100) + "%")
    