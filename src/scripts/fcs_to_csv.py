'''
Created on 16 Oct 2019

@author: mate

take in a path to a .fcs file from user input, and output a .txt file with metdata and a .csv with the flow data
'''
import fcsparser
import os.path
import sys
import pandas as pd

pd.set_option("display.expand_frame_repr", False) # this prevents the splitting of dataframes to multiple rows upon printing
pd.set_option("display.max_columns", 50)

while True:
  inpFcs = input("Enter the filename of an .fcs file with its full path to covert it to a .txt with the metadata, and a .csv with the flow data. Or just type 'Exit' to exit:")
  
  # inpFcs = "/home/mate/code/umap-katamarii/src/data/MR2016-03-28A1.0002.fcs" #  full path of fcs file to analyze
  
  if inpFcs.lower() == "exit": sys.exit(0)
  elif os.path.isfile(inpFcs):
    metaD, dataDf = fcsparser.parse(inpFcs, meta_data_only=False, reformat_meta=True) 
    # the magic one liner to convert fcs files to a dataframe. metaD is a dict with various metadata information, dataDF is a dataframe with rows as events and columns as channels.
    break
    
  else: print(inpFcs, " was not found. Check if you typed the correct path, like /home/Myuser/Documents/myfile.fcs or something similar.\n")

fileNameS = "".join(metaD["$FIL"].split(".")[:-1])

dataDf.to_csv("/".join(inpFcs.split("/")[:-1]) + "/" + fileNameS + ".csv")

with open("/".join(inpFcs.split("/")[:-1]) +  "/" +fileNameS + ".txt","w") as outF:
  for metaK, metaV in metaD.items():
    outLine = str(metaK) + ": " + str(metaV) + "\n"
    outF.write(outLine)
    
print("Done!\n")


