import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "John", "Emma", "David"],
    "Age": [25, None, 30, 22, None],
    "Salary": [50000, 60000, None, 45000, 70000],
    "Department": ["IT", "HR", None, "IT", "Finance"]
})

print(df.info())

sns.heatmap(df.isnull(),annot=True)     #this way we can show which column/variable contains a null value in which row

#plt.show()