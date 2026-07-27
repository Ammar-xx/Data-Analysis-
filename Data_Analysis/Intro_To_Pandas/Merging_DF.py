import pandas as pd
import numpy as np
import seaborn as sns


#Indexing and Reindexing

data=pd.read_csv("monthly-writing-paper-sales.csv",index_col="Month")  #loads the named csv file and marks the column month as the index

data.index = pd.to_datetime(data.index, format="%d-%m").strftime("%B")      #converts the month column from numerical into alphabetical

print(data.head())

data_c=data.copy()    #saves a copy of dataset with index as month

print(data_c.sort_index())  #prints the data in alphabetical order in terms of month

print(data_c.sort_index(ascending=False))   #prints in descending order

print(data_c.sort_values('Sales',ascending=False))  #prints data sorted by Sales col in desc order

ordered=['June','July','January','August','October','September']    #new order you want
#data.reindex(ordered)       #orders data according to the above order
#print(data.head())

#data.reindex(['July','June','March']).dropna()  #reindexes data based on the given order and drops rows with null values

data.reset_index(inplace=True)  #resets the index. (removes month as the index)

data.set_index('Month')     #setting the col manually


data2=pd.read_csv('monthly-sunspots.csv',index_col='Month')
data2.index = pd.to_datetime(data2.index, format="%Y-%m").strftime("%B")

data_merged=pd.merge(data,data2,left_index=True,right_index=True)   #merges the two dataframe with the same index name

print(data_merged.head())


#Concatenating Series

data=pd.read_csv("monthly-writing-paper-sales.csv")

half = len(data) // 2
d1 = data.iloc[:half]
d2 = data.iloc[half:]

df=pd.concat([d1,d2])   #joins the two dataframes. This will work the best if they have the same columns
#print(df.loc[0])        #if you join two dataframes then it is possible that it would have repeating indexes

df.reset_index(drop=True)    #this would fix the repeating index problem

data2=pd.read_csv('monthly-sunspots.csv')

df=pd.concat([data,data2],join='inner',axis='rows')     #row-wise inner join in which it adds all the rows but only the common columns
print(df.head())

df=pd.concat([data,data2],join='outer',axis='rows')     #same as the above simple concat
print(df.head())

#if joining row wise, it will stack rows of the 2nd df after the first one vertically
#if joining column wise, it will put the cols of 2nd df beside the 1st df

df=pd.concat([data,data2],join='inner',axis='columns')     #row-wise inner join in which it adds all the rows but only the common columns
print(df.head())

df=pd.concat([data,data2],join='outer',axis='columns')     #same as the above simple concat
print(df.head())

#merge syntax: pd.merge(left,right,how='inner',on=None,left_on=None,right_on=None,left_index=False,right_index=False,sort=False)
#ON=based on which col we are merging; left_on/right_on can be used to specified manually each df

df=pd.merge(data,data2,how='left',on='Month')   #left join on Month column (adds only the common and all the left dataframe)
print(f"Left join:\n {df.head()}")

df=pd.merge(data,data2,how='right',on='Month')   #right join on Month column (adds only the common and all the right dataframe)
print(f"Left join:\n {df.head()}")

