import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re

x=re.match('Python',"Python programming language")   #used when you want to verify that a string begins with a specific pattern
                                                            #re.match can only search at the start of the string

x.string    #this gives the string (in the above case: Python is a programming language)

print(x.span()[1])     #it returns the starting and ending index of the matched text as a tuple (0 gives start index and 1 gives ending index)

print(x.group())       #gives the pattern (Python)

prog=re.compile("Python")   #this create an object of the pattern
prog.match("It is easier to code using Python language",pos=20)     #this is the same as above
                                                                    #pos makes the re start searching from that index

prog.search("It is easier to code using Python language")   #.search searches the whole string for the pattern

prog.findall("Python is a very good language. Python allows for easier coding")     #this is like .search, just that it finds all the occurence of the pattern

data=sns.load_dataset('titanic')

data['embarked']=data['embarked'].astype('category')        #changes the data type of embarked from str to category

