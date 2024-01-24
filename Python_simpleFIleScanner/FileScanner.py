import os
import tkinter as tk
from tkinter import filedialog
#Get how many files of each exst i have in any given


dir = filedialog.askdirectory()
#os.path.normpath(r"D:\myFolders\Documents\CodeReps\Python_simpleFIleScanner\TestFile")
print(dir)

exstList = {}

for files in os.listdir(dir):
    exst =os.path.splitext(files)[1]
    #print(exst)
    #Fill up the dictonnaries with existing file types.
    if exst not in exstList:
        exstList[exst] = 1
    else :
        value =  exstList[exst] + 1
        exstList[exst] = value
        
for x in exstList.items():
    print(x[0], " : ", x[1])

#Get every file with os.listdir
#Find all exst types and add them in a dict. 
#Display all



