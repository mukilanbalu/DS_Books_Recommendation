#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 07:50:11 2023

@author: mukilanbalu
"""

import pandas as pd

df = pd.read_csv("./booksdata.csv")

df.head()

df.describe()

#dropping rows with page values nan  and 0
newdf = df[df['pages'].notna()]

newdf = newdf[newdf['pages'] != '0']

#removing 'page' string in paage column
newdf2 =newdf['pages'].map(lambda x: x.rstrip('page'))

#setting column back
newdf['pages'] = newdf2

#removing un wanted columns

newdf = newdf.drop(['isbn'], axis=1)

newdf = newdf.drop(['bbeScore','bbeVotes', 'ratingsByStars', 'publishDate','edition','characters'], axis=1)

newdf = newdf.drop(['setting','coverImg', 'bookId'], axis=1)


#replaceing nan in columns 

seris = newdf['series'].fillna('No')
newdf['language'].isna().sum()
#%%
newdf['series'] = seris



#%%
nona= newdf
nona = nona.dropna()
nona.to_csv('cleaned.csv', index=False)
#%%
#import pandas as pd
df= pd.read_csv("./cleaned.csv")

#%%
lan = pd.DataFrame( df['language'].value_counts())
#%%
lan.rename(columns = {'language':'count'}, inplace = True)

#%%
lan['rating']= df['rating'].unique()
#%%
lan=lan[lan['count'] > 10]

#%%
lan.plot(x='language', y= 'count',
        kind="pie", figsize=(20, 20))
#%%
df.rename(columns = {'firstPublishDate':'publish_year'}, inplace = True)

#%%
df.loc[1857, "publish_year"] = ' 01/01/1961 '

#%%

df['publish_year']= pd.to_datetime(df.publish_year, errors='coerce')
df['year']=df['publish_year'].dt.year

#df=df.drop(['format'], axis=1)

#%%

#re formatting price
def solve(val):
    strings = val.split('.')
    if len(strings) > 2:
        return(""+strings[0]+ "" +strings[1]+"."+strings[2])
    return( ""+strings[0]+ "." +strings[1])
    
print(solve('1.743.28'))

df['price'] = df['price'].apply(lambda x : solve(x))

df['price'] = df['price'].astype('float')
#%%

#df['year'] = df['year'].apply(lambda x : str(x).replace('.0',""))


#year = year.apply(lambda x : int(x))


#print( random.choice([16,17,18,19])+""+year[] )

#reformatting year
import random 

yearValues = [16,17,18,19]

def formatYear(yearnum):
    syear=str(yearnum)
    if int(yearnum) > 2020:
        #print(""+ str(random.choice(yearValues))+""+ syear[-2:])
        return int(""+ str(random.choice(yearValues))+""+ syear[-2:])
    #print(yearnum)
    return (yearnum)
        

df['year'] = df['year'].apply(lambda x : formatYear(x))


#%%
df.to_csv('cleaned.csv', index=False)





