import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df=sns.load_dataset('titanic')

#print(df.duplicated())      #is used to check which rows are duplicated

#print(df.duplicated().sum())    #gives the total amount of duplicated rows

print(df[df.duplicated(subset=['sibsp','survived'])])     #finds and prints rows that are duplicates based only on the PassengerId and Survived columns


data=df.drop_duplicates()   #drops duplicated rows

data=df.drop_duplicates(subset=['age','pclass'])    #removes duplicate rows based only on the age and pclass columns

