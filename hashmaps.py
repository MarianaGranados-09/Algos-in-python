#hash tables

#a hash function is a function where you put ina string and get back
#a number, a hash function maps strings to numbers

#also known as hash maps, maps, dictionaries and associative arrays
#python has hash tables: dictionaries dict function

book = dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book["avocado"])

#python's shortcut for making a new hash table:
phone_book = {}
#the get function returns the value if "tom" is in the hash table
#otherwise it returns None

#collision: two keys have been asigned the same slot. Dealing with
#collisions: if multiple keys map to the same slot, start a linked list
#at that slot

#Performance: hash tables take o(1) for everything -constant time
#time taken will stay the same, regardless of how big the hash table is

