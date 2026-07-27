import pandas as pd
import numpy as np
import seaborn as sns

df=sns.load_dataset('titanic')

print(df['age'].isnull())       #returns true if the variable is null, can add .sum() to count null values
                                #.notnull is its reverse

print(df.age[df['age'].notnull()])  #to print not null values with index no.

#converting a dataframe to csv can convert (using .to_csv("filename.csv")) most of the false data into nan values





