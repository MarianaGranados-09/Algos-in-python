#Arrays and linked lists

#using an array means all elements are stored contigously in memory

#linked lists can be anywhere in memory, each item stores the address of
#the next item in the list, a bunch of random memory addresses are linked together
#adding an item to a linked list is easy: you stick it anywhere in memory
#and store the address with the previous item

#cons of using linked lists: dont know the address of the last item in a 
#linked list, you have to go to the address for item #2 and so on, until
#the last item

#linked lists are great if youre going to read all the items one at a time

#pros or arrays: you know the item in your arrary, 00, 01, 02, 03...
#arrays are great elements for reading random elements

#run times for common operations on arrays and lists
        #arrays   lists
#reading: o(1)      o(n)
#insertion: o(n)   o(1)
#deleting: o(n)   o(1)

#lots of inserts and few readings: linked lists
#inserting into the middle of a list: changing what the previous
#element points to

#Deleting elements: lists

#Two different types of access: random access and sequential access

#Selection sort algorithm
#Sorting a list from most to least played to rank fav artists
#Check each item in the list to find the artist with the highest play count
#which takes o(n) time. This process must be done n times

#The process overall takes o(n^2) time
#Selection sort:


def findSmallest(arr):
    smallest = arr[0] #element in index 0 in arrray
    smallest_index = 0 #initializing smallest index
    for i in range(1, len(arr)):
        if arr[i] < smallest: #if smallest is bigger than arr[1]
            smallest = arr[i] #smalles is now arr[i]
            smallest_index = i #smallest_index is now i
    return smallest_index

#print(findSmallest([10,2,3,4]))

def selectionSort(arr): #sorts an array
    newArr=[]
    for i in range(len(arr)):
        smallest = findSmallest(arr) #finds the smallest element in the
        #array, and adds it to the new array until no more elements 
        newArr.append(arr.pop(smallest)) #extracts smallest from arr and 
        #adds it to newArr with append
    return newArr

print(selectionSort([5,3,6,2,10]))


