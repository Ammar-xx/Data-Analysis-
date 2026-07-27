import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
print(df.head())

#sns.scatterplot(data=df,x='age',y='pclass') #seaborn is used in case the data is complex or you need to add visualization

#sns.countplot(df['pclass'].dropna()) #this is a seaborn count plot
#plt.xlim(0,10)


fig,ax=plt.subplots(1,2) #to make multiple subplots using seaborn of 1 row and 2 columns
plt.tight_layout()
sns.lineplot(data=df,x='age',y='pclass',ax=ax[0])   #plot at [0][0]
sns.countplot(df['pclass'].dropna(),ax=ax[1])       #plot at [0][1]

plt.show()