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

inpFcs = "/home/mate/code/umap-katamarii/src/data/MR2016-03-28A1.0002.fcs"



metaDf, dataDf = fcsparser.parse(inpFcs, meta_data_only=False, reformat_meta=True)

print(type(metaDf))
print(type(dataDf))

print(dataDf)
# print()
# 
for metaK,metaV in metaDf.items():
  print(metaK)
  print(metaV)
  print("---")
   
  

reducer = umap.UMAP()

reducer.fit(dataDf.values)

embeddingO = reducer.transform(dataDf.values)

print(embeddingO.shape)


plt.scatter(embeddingO[:, 0], embeddingO[:, 1], c=np.log(dataDf["FSC-A"].values), cmap='Spectral', s=5)
plt.gca().set_aspect('equal', 'datalim')
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.title('UMAP projection of .FCS file', fontsize=24);

plt.show()

print("fcs converter completed")
