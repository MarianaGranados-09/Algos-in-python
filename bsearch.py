import math
#Searching algorithms

#Binary search is a quick and effective method for searching for an element in a sorted list in (O(log(n)) time.

#We start by defining upper and lower bounds for what location a file can occupy in a filing cabinet. The lower bound will be 0, and the upper bound will be the length of the cabinet
# looking_for = 4

# sorted_cabinet = [1,2,3,4,5]
# upper = len(sorted_cabinet)
# lower = 0

# #Then we will guess thar the file is in the middle of the cabinet
# #print(upper)
# guess = math.floor(len(sorted_cabinet)/2) #1

# #next we check if our guess is too low or too high
# if(sorted_cabinet[guess] > looking_for):
#     upper = guess
#     guess = math.floor((guess + lower) / 2)

# if(sorted_cabinet[guess] < looking_for):
#     lower = guess
#     guess = math.floor((guess + upper) / 2)

#binarySearch() function
sorted_cabinet = [1,2,3,4,5,6,7,8]
def binarySearch(sorted_cabinet, looking_for):
    guess = math.floor(len(sorted_cabinet)/2)
    upper = len(sorted_cabinet)
    lower = 0
    while(abs(sorted_cabinet[guess] - looking_for) > 0.0001):
        if(sorted_cabinet[guess] > looking_for):
            upper = guess
            guess = math.floor((guess + lower) / 2)
        if(sorted_cabinet[guess] < looking_for):
            lower = guess
            guess = math.floor((guess + upper) / 2)
    return(guess)

guess = binarySearch(sorted_cabinet, 8)
print(sorted_cabinet[guess])

#Binary search runs in logarithmic time or log time
#Sorted list of 128 names: 7 guesses
