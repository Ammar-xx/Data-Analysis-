import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


age=[20,22,25,35,40,50,60]

salary_1=[18000,20000,30000,30500,43000,44000,51000]
salary_2=[12000,25000,29000,32300,50000,60000,61000]


plt.style.use('dark_background') ##to change the style of the graph

plt.figure(figsize=(10,20))
plt.subplot(3,1,1)  #to make multiple plots in 1 fig: [rows, columns, panel number]
plt.plot(age,salary_1) #1st plot

plt.subplot(3,1,2)  #2nd plot
plt.plot(age,salary_2)

plt.show()