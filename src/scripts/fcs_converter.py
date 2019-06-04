'''
Created on 13 Nov 2018

@author: mate

open and parse fcs file using fcs parser, then analyze with umap
'''


import umap
import pandas as pd
import fcsparser
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.expand_frame_repr", False) # this prevents the splitting of dataframes to multiple rows upon printing
pd.set_option("display.max_columns", 50)

print("running fcs converter")

inpFcs = "/home/mate/code/umap-katamarii/src/data/MR2016-03-28A1.0002.fcs" #  full path of fcs file to analyze

metaD, dataDf = fcsparser.parse(inpFcs, meta_data_only=False, reformat_meta=True) 
# the magic one liner to convert fcs files to a dataframe. metaD is a dict with various metadata information, dataDF is a dataframe with rows as events and columns as channels.

# print(type(metaD))
print("\nChannels found:")
for channelN in metaD["_channel_names_"]:
  if channelN == metaD["_channel_names_"][-1]:
    print(channelN + "\n")
  else:
    print(channelN + ", ", end="")
    
print("events found:\n")
for metaK, metaV in metaD.items():
  print (metaK, ": ", metaV)

print()
print(dataDf)

# print(type(dataDf))
# 
# print(dataDf)
# print()
#
# for metaK,metaV in metaD.items():
#   print(metaK)
#   print(metaV)
#   print("---")
   
  
# the following 3 lines are what's needed for the umap calculation. 
reducer = umap.UMAP()
reducer.fit(dataDf.values) # dataDf needs to be converted to a numpy array so it can be fed scikit learn. Note that all channels are used as is (no gating, no log transformation etc)
embeddingO = reducer.transform(dataDf.values)

# print(embeddingO.shape)

colName = "PercP-A"
colourCode = np.log(dataDf[colName].values) # colour code to use for 2d plot. Column name can be changed easily to change colour of plot

plt.scatter(embeddingO[:, 0], embeddingO[:, 1], c=colourCode, cmap='Spectral', s=5) # 
plt.gca().set_aspect('equal', 'datalim') # set axes equal and limit data to fit into resulting box
plt.colorbar().set_label(colName, rotation=270, labelpad = 20) # add colour bar with label on the right
plt.title('UMAP projection of .FCS file', fontsize=16)

plt.show()