#Dijkstra's algorithm

#BSF will find the path with the fewest segments
#Finding the fastest path however, is with a different algo: Dijkstra's

#1. find the "cheapest" node 
#2. update the costs of the neighbors of this node
#3. repeat until done for every node
#4. calculate the final path

#takes 2 min to get to node B, 5 min to get to node A, 6 min to the finish

#number associated with edge: weights
#a graph with weights is called a weighted graph - Dijkstra's algorithm
#a graph without weights is called an unweighted graph -breadth first search

#graphs can also have cycles
#Dijkstra's algo only works with directed acyclic graphs, called DAGs

#Bellman-Ford algorithm to find shortest path in a graph with negative
#weight edges

