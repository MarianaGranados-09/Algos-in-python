#graphs- first graph algo called breadth-first search (BFS)

#Allows you to find the shortest distance between two things, the algo can
#be used for:

#Write a checkers AI that calculates the fewest moves to victory
#Write a spell checker
#Find the doctor closest to you in your network

#shortest-path problem
#1. model the problem as a graph
#2. solve the problem using breadth-first search

#What is a graph? A graph models a set of connections, each node is made
#up of nodes and edges, a node can be connected to many other nodes called 
#neighbors. 

#Breadth-first search:
#1. is there a path from node A to node B?
#2. What is the shortest path from node A to node B?

#Queues: are similar to stacks, you can't access random elements
#in the queue, instead, there are only 2 operations: enqueue and dequeue

#enqueue: add an item to the queue, dequeue: take an item off the queue

#queue: FIFO ds - first in, first out
#stack: LIFO ds - last in, first out

#graphs- first graph algo called breadth-first search (BFS)

#Allows you to find the shortest distance between two things, the algo can
#be used for:

#Write a checkers AI that calculates the fewest moves to victory
#Write a spell checker
#Find the doctor closest to you in your network

#shortest-path problem
#1. model the problem as a graph
#2. solve the problem using breadth-first search

#What is a graph? A graph models a set of connections, each node is made
#up of nodes and edges, a node can be connected to many other nodes called 
#neighbors. 

#Breadth-first search:
#1. is there a path from node A to node B?
#2. What is the shortest path from node A to node B?

#Queues: are similar to stacks, you can't access random elements
#in the queue, instead, there are only 2 operations: enqueue and dequeue

#enqueue: add an item to the queue, dequeue: take an item off the queue

#queue: FIFO ds - first in, first out
#stack: LIFO ds - last in, first out

#IMPLEMENTING THE GRAPH with hash tables to express relationships
graph = {}
graph["you"] = ["alice", "bob", "claire"] #"you" is mapped to and array, so
#graph["you"] will give you an array of all the neighbors of "you"

#directed graph - the relationship is only one way

def person_is_seller(name):
    return name[-1] == 'm'

#queue function
from collections import deque
search_queue = deque() #creates a new queue
search_queue += graph["you"]  #adds all of your neighbors to the search queue
 
 #then keep checking while the queue isnt empty
while search_queue:
    person = search_queue.popleft() #grabs the first person off the queue
    if person_is_seller(person):    #checks whether person is mango seller
        print(person + " is a mango seller") #yes theyre a mango seller
        #return True
    else:
        search_queue += graph[person] #no they aren't, add all of this person's
        #friends to the search queue

#the algorithm wil keep going until either:
#1. a mango seller is found or
#2. the queue becomes empty, in which case there is no mango seller

#running time
#each edge(arrow or connection from one person to another) so running
#time is at least o(number of edges). Breadth-first search takes 
#o(number of people + number of edges) or o(v+e) v for vertices, 
#e for number of edges

#a tree is a special type of graph, where no edges ever point back


