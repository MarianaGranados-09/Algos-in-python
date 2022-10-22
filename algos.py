#brief overview of algorithms

#trees
#Searching for an element in a binary search tree takes o(log n)
# time on average and o(n) time in the worst case

#a binary search tree is a lot faster for insertions and deletions on average

            #array      #binary search tree
#search     o(log n)        o(log n)
#insert     o(n)            o(log n)
#delete     o(n)            o(log n)

#b-trees, a special type of binary tree is commonly used to store data in databases
#B-trees, Red-black trees, Heaps, Splay trees

#Inverted index: a hash that maps words to places where they appear
#commonly used to build search engines

#Parallel algos for theoretical side of performance and scalability

#MapReduce, a special type of parallel algorithm: the distributed algorithm
#it can be used through the open source tool Apache Hadoop

#Why are distributed algorithms useful?
#Distributed algorithms are great when you have a lot of work to do 
#and want to speed up the time required to do it
# 2 parts: the map function and the reduce function

#the map function is simple: it takes an array and applies the same function to each
#item in the array:
from functools import reduce


arr1 = [1,2,3,4,5]
arr2 = map(lambda x: 2 * x, arr1) #2,4,6,8,10

#the reduce function is to "reduce" a whole list of items down to one item
#with map, you go from one array to another
#with reduce, you transform an array to a single item
arr12 = [1,2,3,4,5]
arr21 = reduce(lambda x,y: x+y, arr12) #15

#Bloom filters are probabilistic data structures
#false positives are posible, false negatives aren't.
#Bloom filters are great when you dont need an exact answer


#Linear programming is used to maximize something given constraints
#linear programming uses the simplex algorithm

