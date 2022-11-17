# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:16:25 2022

@author: minhp
"""
import pandas as pd

file_path = r'C:\Users\minhp\Per_projects\Aupair\aupaircom\aupaircom\spiders\result2110.csv'
df = pd.read_csv(file_path)
check_null = df.isnull().any()
count_null_in_enfants_column = df['enfants'].isnull().sum()

rows_with_nan = [index for index, row in df.iterrows() if row.isnull().any()]