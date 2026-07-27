import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('iris')
#print(df.head())

sns.lineplot(data=df.drop(columns='species'))       #how to make mutiple line plots easily on a single graph
                                                    #it is used to show the trend of something overtime

plt.show()

sns.countplot(df['petal_length'])       #bar/count plot using seaborn is used when to
                                        #represent a single categorical data and barplot when to
                                        #show one categorical and one numerical

plt.show()

sns.scatterplot(data=df,x='sepal_length',y='sepal_width',hue='species')     #scatterplot for every in which every specie has a diff color due to hue
                                                                            #it is used to represent 2 numerical data
                                                                            
plt.show()

sns.histplot(x=df['petal_length'],bins=10,kde=True)         #histogram plot using seaborn. KDE is used to show a curve that shows where are the most values
                                                            #histogram is used when to represent a single numerical data

plt.show()