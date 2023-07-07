#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 17:57:39 2023

@author: mukilanbalu
"""

import pandas as pd
import matplotlib as mb


df= pd.read_csv("./booksdata.csv")

df.head()

df.describe()

df.series.value_counts() 

seriesList = df.series.value_counts().rename_axis('series').reset_index(name='counts')

seriesList = seriesList[seriesList.counts > 1]


