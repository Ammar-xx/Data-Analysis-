import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

age=[20,22,25,35,40,50,60]

salary=[18000,20000,30000,30500,43000,44000,51000]

years_of_service=[5,6,7,8,9,10,11]

plt.figure(figsize=(10,20)) #to set figure width and height

plt.plot(age,salary) #1st line plot

plt.plot(age,years_of_service,color='green') #2nd line plot in a single graph of green line

plt.legend(['Employee Salary Info','Employee Timeline']) #to show which line belongs to which 

plt.title('Employee Info')
##plt.xlabel('Age')       #to set labels for the axis and the title of the graph
##plt.ylabel('Salary')

##plt.xlim(20,30)     #to focus on a specific part of the x axis
##plt.ylim(20000,30000) #to focus on a specific part of the y axis


plt.plot(age,salary,'4-.r') ##the string shows the line formatting: 4=marker, -.=line type, r=line color

plt.show() ## to view the final graph