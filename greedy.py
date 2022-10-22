#greedy algorithms

#The classroom scheduling problem
#1. pick the class that ends the soonest, this is the first class
#you'll hold in this classroom
#2. Pick a class that starts after the first class. then again pick the
#class that ends the soonest. This is the second class youll hold

#a greedy algorithm is simple: at each step, pick the optimal move
#and then youre left with the globally optimal solution

#The knapsack problem
#1. pick the most expensive thing that will fit in your knapsack
#2. pick the next most expensive thing that will fit, and so on

#except this time, it doesnt work
#greedy algorithms shine by solving a problem pretty well, although not perfect

#Approximation algorithms
#judged by how fast they are and how close they are to the optimal solution


#Set-covering problem
states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca","az"])
#using set to avoid duplicates
#list of stations:
stations = {}
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca","az"])
#something to hold the final set of stations you'll use

#calculating the answer: you need to go through every station and
#pick the one that covers the most uncovered states
best_station = None
states_covered = set()
#states_covered is a set of all the states that havent been covered yet
#the for loop allows you to loop over every station to see which one is 
#the best station
for station, states_for_station in stations.items():
    #set interseccion
    covered = states_needed & states_for_station
    if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered


#operations on sets: union, intersection, difference


#NP-completeness: problems famously hard to solve like the traveling
#salesperson and the set-covering problem

#if you have a NP-complete problem, your best bet is to use an approx. algo


