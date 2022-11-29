#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:36:53 2022

@author: jason
"""

import glob
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

fn='/Users/jason/Dropbox/Nanok_snow_profiles/raw/Nanok.xlsx'
df=pd.read_excel(fn)

#%%
print(df)

pits=np.arange(6,11)

SWE=[]
elev=[]

for pit in pits:
    v=np.where(df.site==pit)
    v=v[0][0]
    
    temp=pd.read_excel(fn,sheet_name=str(pit).zfill(2))
    print(pit,v,temp.SWE[0])
    SWE.append(temp.SWE[0])
    elev.append(df.elev[v])
    # print(str(pit).zfill(2))

plt.scatter(elev,SWE)
# plt.scatter(-df.lon,df.lat)