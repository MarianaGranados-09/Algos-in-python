#implementing RPM in python
import math
import pandas as pd
#pandas enables us to work with tables easily, in this case we used the zip command which joins halving and doubling together => converted into a pandas dataframe, and stored in a table as two aligned columns

#two numbers
n1 = 89
n2 = 18

#column

halving = [n1]

#next halving/2 ignoring the remainder
#print(math.floor(halving[0]/2))

while(min(halving) > 1):
    halving.append(math.floor(min(halving)/2))
    #append() method for concatenation, at each iteration of the while loop, it concatenates the halving vector with the half of its value

#Doubling the column
doubling = [n2]
while(len(doubling) < len(halving)):
    doubling.append(max(doubling) * 2)
    #in each iteration, we add double the prev. entry to the doubling column, and we stop afyer the column is the same length as the having column

#union of columns through a dataframe:
half_double = pd.DataFrame(zip(halving, doubling))

#the following line will keep only the rows of the table whose entry in the halving column is odd
half_double = half_double.loc[half_double[0]%2 == 1, :]
#we use the loc functionality in the pandas moduleto select only the rows we want, the format is [row, column]
#for example: row with index 4 and the column with index 1 half_double.loc[4,1].

#Sum of the remaining doubling entries:
#all rows, only column 1
answer = sum(half_double.loc[:,1])

print(answer)
