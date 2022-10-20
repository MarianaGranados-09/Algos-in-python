#recursion
#coding technique used in many algos, recursion is where a function
#calls itself. When u write a recursive function, you have to tell
#it when to stop, that's why it has 2 parts: the base case and the
#recursive case

#countdown function 
# def countdown(i):
#     print(i)
#     if i <= 0:
#         return
#     else:
#         countdown(i-1)

# countdown(1)

#the call stack with recursion
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x*fact(x-1)

# print(fact(4))

#  QUICKSORT algo

#faster than selection sort, uses divide and conquer method
#empty arrays and arrays with one element dont need to be sorted
def quicksort(array):
    if len(array) < 2:
        return array    #base case 
    else:
        pivot = array[0] #recursive case
        less = [i for i in array[1:] if i <= pivot]
        #sub-array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot]
        #sub-array of all the elements greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,3]))

#quicksort's speed depends on the pivot that we choose, in the worst case 
#quicksort takes o(n^2) time. In average, quicksort takes o(n log n) time.



