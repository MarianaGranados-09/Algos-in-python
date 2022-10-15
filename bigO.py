#Big O Notation theory

# In the case of insertion sort, when we look at our expression for the max number of steps required to perform the algorithm, we find that its a sum of two terms: one is a multiple of n^2 and the other is a multiple of n.
# the term that is a multiple of n will matter less and
# less as n grows, and the n2 term will come to be the only one that we are
# concerned with. So the worst case of insertion sort is that it is a O(n^2) 

#We can use big O notation to talk about time but also about space

#The worst-case (and average-case) complexity of the insertion sort algorithm is O(n^2). 
#Meaning that, in the worst case,  the time taken to sort a list is proportional to the
#square of the number of elements in the list
