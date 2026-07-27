import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": [
        "Alice", "Bob", None, "David", "Emma",
        None, "Frank", "Grace", None, "Henry"
    ],
    "Age": [
        25, None, 30, 28, 22,
        None, None, 35, None, 40
    ],
    "City": [
        "New York", "Chicago", "Los Angeles", None, "Houston",
        "Miami", None, "Seattle", None, "Boston"
    ],
    "Email": [
        "alice@example.com",
        "bob@example.com",
        "charlie@example.com",
        "david@example.com",
        None,
        "emma2@example.com",
        "frank@example.com",
        None,
        None,
        None
    ]
})

data['Age'].fillna(23)      #replaces the null values in age column with 23

data['Age'].fillna(data['Age'].mean())  #replaces with mean of age

data['Age'].fillna(method='ffill')      #this would replace the null value with the non-null value before it

for col in data:
    data[col].fillna(data[col].mean())  #easy loop to fill every column's null values with its mean


data.replace(to_replace=np.nan,value=99)    #replaces every null value with 99

