import math
#Merge sort contains 2 parts: a part that merges two lists and a part that repeatedly uses merging to accomplish the actual sorting

#Merging part
# To merge, we can take the first file in both of the original cabinets simultaneously. Whichever file is lower is inserted into the new cabinet as its first file. 

# When either the leftcabinet or the right cabinet is empty, take the remaining files in the non-empty cabinet and place them all together at the end of the new cabinet

# newCabinet = []

# left = [1,3,4,4,5,7,8,9]
# right = [2,4,6,7,8,8,10,12,13,14]

# #this process need to continue as long as both of the cabinets still have at least one file
# while (min(len(left),len(right)) > 0):
#     if left[0] > right[0]:
#         to_insert = right.pop(0)
#         newCabinet.append(to_insert)
#     elif left[0] <= right[0]:
#         to_insert = left.pop(0)
#         newCabinet.append(to_insert)
# #check to see what list still has files
# if(len(left) > 0):
#     for i in left:
#         newCabinet.append(i)
# if(len(right) > 0):
#     for i in right:
#         newCabinet.append(i)

#Combination of snippets:
def merging(left, right):
    newCabinet = []
    while (min(len(left),len(right)) > 0):
        if left[0] > right[0]:
            to_insert = right.pop(0)
            newCabinet.append(to_insert)
        elif left[0] <= right[0]:
            to_insert = left.pop(0)
            newCabinet.append(to_insert)
    #check to see what list still has files
    if(len(left) > 0):
        for i in left:
            newCabinet.append(i)
    if(len(right) > 0):
        for i in right:
            newCabinet.append(i)
    return(newCabinet)

# left = [1,3,4,4,5,7,8,9]
# right = [2,4,6,7,8,8,10,12,13,14]

# newcab = merging(left, right)
# print(newcab)

#From merging to sorting 
def mergesort(cabinet):
    newCabinet = []
    if(len(cabinet) == 1):
        newCabinet = cabinet
    else:
        left = mergesort(cabinet[:math.floor(len(cabinet)/2)])
        right = mergesort(cabinet[math.floor(len(cabinet)/2):])
        newCabinet = merging(left, right)
    return(newCabinet)


cabinet = [4,1,3,2,6,3,18,2,9,7,3,1,2.5,-9]
newcabinet = mergesort(cabinet) 
print(newcabinet)
#Merge sort is a divide and conquer algorithm, hence the previous code can be collapsed by using recursion.

# The merge sort process consists of successively splitting the initial cabinet into sublists and then merging those sublists back together, preserving the sorting order.

# Every time we split a list, we're cutting it in half, the number of times a list of length n can be split in half before each sublist has only one element is about log(n) and the number of comparisons we make at each merge is at most n.
#  n or fewer comparisons for each
#of log(n) comparisons means that merge sort is O(n×log(n))

#python's built in sorting function sorted is as follows:
print(sorted(cabinet)) 
#Which uses a hybrid version of merge sort and insertion sort
