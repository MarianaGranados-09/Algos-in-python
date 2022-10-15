#insertion sort relies on looking at each item in a list one at a time and inserting it into a new list that ends up being correctly sorted 

#Insertion in insertion sort 

# cabinet = [1,2,3,3,4,6,8,12]
# #file we want to insert into our cabinet
# to_insert = 5

# check_location = len(cabinet)-1 #6
# insert_location = 0

# #check whether the file to insert is higher than the file at the check_location. As soon as we encounter a number that lower than the number to insert, we use its location to decide where to insert our new number. We add 1 because our insertion takes place just behind the lower number we found
# if to_insert > cabinet[check_location]:
#     insert_location = check_location + 1

#list of numbers, number to insert
def insert_cabinet(cabinet, to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    #mientras que check sea mayor o igual a 0
    while(check_location >= 0):
        #si el numero a insertar es mayor al ultimo numero de la lista
        #entonces la locacion para insertar es la ultima pos + 1
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            #posicion a check es la ultima posicion de la lista
            check_location = -1
        #si el numero a insertar no es mayor al ultimo numero en la lista, entonces locacion a revisar es locacion a revisar menos 1, es decir, el penultimo numero de la lista
        check_location = check_location -1
    #built in python method for list manipulation called insert to put the file into the cabinet
    cabinet.insert(insert_location, to_insert)
    return(cabinet)

# cabinet = [1,2,3,3,4,6,8,12]
# newCabinet = insert_cabinet(cabinet, 5)
# print(newCabinet)

#Sorting via insertion
#1. Remove the first element of our old unsorted cabinet and add it to our new empty cabinet, using insertion algo.
#2. We do the same with the second element of the old cabinet, then the third, and so on until we insert every element of old cabinet into the new cabinet.
#3. Forget about old cabinet, focuse on new
#4. Since we've been inserting using our insertion algo, it always returns a sorted list

# cabinet = [8,4,6,1,2,5,3,7]
# newCabinet = []
# #get pos 0 from cabinet
# to_insert = cabinet.pop(0);
# newCabinet = insert_cabinet(newCabinet, to_insert)

cabinet = [8,4,6,1,2,5,3,7]
def insertion_sort(cabinet):
    newCabinet = []
    #while there is an element in the list cabinet
    while len(cabinet) > 0:
        to_insert = cabinet.pop(0)
        newCabinet = insert_cabinet(newCabinet, to_insert)
    return(newCabinet)

sortedCabinet = insertion_sort(cabinet)
print(sortedCabinet)
