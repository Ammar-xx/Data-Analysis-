import pandas as pd
import seaborn as sns

data=sns.load_dataset('titanic')

#iloc = Integer Location → access data by position.

print(data['pclass'][0])    #gives the first row element of column pclass

print(data.iloc[0])     #iloc is used for index based data access. This gives the first element of each column in the data
                        #this is used as we cannot directly do this: data[0]

print(data.iloc[:,4])   #this prints all rows of the column at index 4 (5th column)

print(data.iloc[:3,4])  #this prints rows from 0-2 of the column at index 4

print(data.iloc[[0,2,4],[2,3]])     #prints the 0,2 and 4th rows of the columns at index 2 and 3

print(data.iloc[0,2:4])         #prints the first row of columns at index 2 and 3 (4 excluded)


#loc = Label Location → access data by row and column labels.

print(data.loc[1,'pclass'])     #prints the 2nd row (row at index 1) of pclass column

print(data.loc[:,['survived','age','sibsp']])   #prints all the rows of columns survived,age and sibsp

#we can also retrieve data using conditions

print(data.loc[data.survived==1])

print(data.loc[data.embarked.isin(['S','C'])])     #prints only those rows where the value of embarked column is either S or C

print(data.loc[data.age.between(20,25)])    #prints only those rows where age is b/w 20-25 (included)

#Reshaping Data

print(data.groupby(['sex','pclass'])[['age','survived']].mean())    #prints the mean of ages and survived grouped by gender and pclass