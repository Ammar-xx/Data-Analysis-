import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

age=[20,22,25,35,40,50,60]

salary_1=[18000,20000,30000,30500,43000,44000,51000]
salary_2=[12000,25000,29000,32300,50000,60000,61000]

fig,ax=plt.subplots(4,2)       #to create multiple sub plots: (rows,columns)
plt.tight_layout()

ax[0][0].plot(age,salary_1)     #1st subplot at (0,0)
ax[2][1].plot(age,salary_2)     #subplot at (2,1)

ax[0][0].set_xlabel('Age')
ax[0][0].set_ylabel('salary')

plt.show()