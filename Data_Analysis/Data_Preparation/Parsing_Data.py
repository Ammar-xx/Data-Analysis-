import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Name": ["Ali", "Sara", "John", "Emma", "David"],
    "Purchase_Date": [
        "2024-01-15",
        "2024-02-20",
        "2024-03-05",
        "2024-04-12",
        "2024-05-30"
    ],
    "Amount": [250, 450, 300, 150, 500]
})

print(data.dtypes)

data['Formatted_Date']=pd.to_datetime(data['Purchase_Date'],format="%Y-%m-%d")  #Converts a string-based date column (YYYY-MM-DD) into a pandas datetime format
                                                                                #the format tells the lib how to interpret the string

data['year']=data['Formatted_Date'].dt.year     #this can be used to extract year or month or day
                                                #works only if the data type is Date


