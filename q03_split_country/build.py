# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    
    df['country name'] = df['country name'].str.split('(',1).apply(lambda x :x[0])
    df.set_index('country name',inplace = True)
    df.dropna(inplace = True)
    df.drop(['Totals'],axis=0,inplace = True)
    print(df.shape)
    print(df.columns)
    
    return df


q03_summer_gold_medals('./data/olympics.csv')     

