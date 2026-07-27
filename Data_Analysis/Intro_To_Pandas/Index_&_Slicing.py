import pandas as pd


a=['spam','hamster','rabbit','goat','tiger','Lion']

print(a[0])     #prints the first element

print(len(a))   #prints the number of elements in array a

print(a[len(a)-1])  #prints the last element

print(a[-1])    #also prints the last element (0 gives the 1st element so -1 points to the last element)

print(a[2:5])   #print elements starting from index 2 till 4 (doesn't print the 5th element)

print(a[:])     #prints all the elements in the array

print(a[-5:-2])     #acc to the above array, it prints the element at index 1 till index 3 (index 4 not included)

print(a[:4])    #prints elements from index 0 till index 3
print(a[0:4])   #same as the above instruction

print(a[2:])    #prints elements from index 2 till the last index
print(a[2:len(a)])  #same as the above instruction

print(a[0:10:2])        #prints elements starting from index 0, but doesn't print the next element but the one next to it till the end of array
                        #its syntax: a[start_ind:end_ind(not included):iterative] similar to for loop

print(a[6:0:-2])        #prints elements starting from index 6 then index 4,index 2,index 0

print(a[::-1])      #prints the array starting from the last element
print(a[::1])       #opposite of the above (equal to a[:])

