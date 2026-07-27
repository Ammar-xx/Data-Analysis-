import pandas as pd
import seaborn as sns

#Sub Setting Columns

data=sns.load_dataset('titanic')
print(data.head())

data1=data[['pclass','age']]    #data1 now contains the pclass and age column data
print(data1.head())

print(data['age']>30)       #this checks each row and returns true if the each is gt 30, else false
print(data[data['age']>30])     #this prints only those rows in which age>30

data['Family']=data['sibsp']+data['parch']  #this makes a new column that is the addition of sibsp and parch column

#Summary Statistics

print(data['age'].mean())   #gives the mean of age col

print(data['age','survived'].median())     #gives the mid value of age and survived col

print(data['age','survived'].describe())    #gives count,std,mean,median,lower,middle,upper quartile etc

print(data['age','survived'].agg(['min','max','median']))   #if you want specific aggregates

