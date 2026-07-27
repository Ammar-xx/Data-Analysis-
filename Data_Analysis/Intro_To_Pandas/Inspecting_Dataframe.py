import pandas as pd

pd.DataFrame({             #this creates a type of table with individual arrays as columns containing data
    'names':['Ammar','Rayyan','Ali','Huzaifa'],
    'age':[20,18,21,21],
})

pd.Series([1,2,3,5])    #this creates an array

Sales=pd.Series([20,30,40],index=['day 1','day 2','day 3'],name='Product A')    #this creates an array with user-based indexes and also adds a column name
print(Sales)

Sales_toFrame=Sales.to_frame()    #this converts the series into a dataframe

data=pd.read_csv('titanic.csv')     #this is needed to load a csv file (the file needs to be present in the folder to be loaded)

print(data.shape())     #this gives the numbers of rows and columns in the dataframe

print(data.head())  #prints the first five rows of the data

print(data.tail())  #this gives you the last 5 rows of the data

print(Sales.info())    #gives info about each column of the data

print(Sales.describe()) #this prints the count,mean,std,min,max etc of the data

print(data.values)          #this prints all the rows

print(data.Age.value_counts())      #this gives the amount of times each Age column value occurs

print(data.Age.value_counts(sort=True,normalize=True))      #normalize=true gives data in percentage and sort=true sorts the data in desc order

print(data.columns())   #prints the columns

print(data.index())     #prints the start and ending index and steps

print(data.sort_values('Age',ascending=True))    #prints the data, with age col sorted in asc order (for desc, make asc=false)
      
