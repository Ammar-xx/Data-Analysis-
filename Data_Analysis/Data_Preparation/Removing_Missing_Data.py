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

print(f"Original Data:{data}")

df=data.dropna()        #this drops all the rows that contain atleast one null value

print(f"Data without rows that contain atleast one null value:\n{df}")

df=data['Email'].dropna()        #this command removes the null values only from the email column.(NOT RECOMMENDED AT ALL)
                            #for eg: if in the 2nd row age value is non-null and email is null, it would only remove the email

df = data.dropna(subset=["Email"])    #this command removes the rows in which email is null
                                    #for eg: if in the 2nd row age value is non-null and email is null, it would remove the whole row

print(f"Data without rows that contained null in email column:{df}")


df=data.dropna(axis='rows',thresh=4)   #this would drop only those rows that contain less than 4 non-null values

df=data.dropna(axis="columns")          #this would drop those columns that contain atleast one null value

df = data.dropna(subset=['Email','City'],how="all")   #this drops only those rows in which both city and email are null.
                                            #if in a rows one of them isn't null, then it wouldn't drop the rows.

df=data.dropna(axis="columns",how="all")    #would drop the columns that only contain null values

