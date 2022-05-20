# PIC 16A HW1
# Name: Joanne Qiu
# Collaborators: N/A
# Date: 01/14/2021

import random # This is only needed in Problem 5

# Problem 1

def print_s(s):
    ''' Prints a given string.
    Args:
        s: A string.
    Returns:
        None
    '''
    print(s)

# you do not have to add docstrings for the rest of these print_s_* functions.

def print_s_lines(s):
    l = s.split(": ")
    for i in range(len(l)):
        print(l[i])

def print_s_parts(s):
    l = s.split("\n")
    for i in range(len(l)):
        print(l[i][:9])

def print_s_some(s):
    l = s.split("\n")
    for i, value in enumerate(l): 
        if len(l[i]) != max(len(l[0]), len(l[1]), len(l[2])): print(value)


def print_s_change(s):
    a = s.replace("math", "data science")
    b = a.replace("long division", "machine learning")
    print(b)


# Problem 2 

def make_count_dictionary(L):
    ''' Counts how many times each element in a list appears.
    Args:
        L: A list. Elements may be of different types.
    Returns:
        A dict of counts. A key is a unique element of L,
        and its corresponding value is how many times
        that element is in L.
    Example:
        L = ["a", "a", "b", "c"]
        returns {"a" : 2, "b" : 1, "c" : 1}
    '''
    D = {} # create the dictionary that needs to be returned

    keys = [] # create a new list to save the keys
    [keys.append(item) for item in L if item not in keys] # make sure each element in L appears only once in the keys

    # for each key in the keys,
    # count the number of times it appears in L and add the pair to D
    for i, value in enumerate(keys): 
        D[keys[i]] = L.count(keys[i]) 
    
    return D # return the dictionary


# Problem 3

def gimme_an_odd_number():
    ''' Waits for an odd number.
    Repeatedly prompts user with 'Please enter an integer.'  
    until given an odd number.
    Assume the user will only type in non-negative integers.

    Args:
        None
    Returns:
        At termination, prints and returns a list of 
        all numbers that the user has given so far.
    '''
    x = int(input("Please enter an integer."))
    num = [x] # intialize the list with the first integer
    
    # ask for an integer input until the input is an odd number
    while x % 2 == 0: 
        x = int(input("Please enter an integer."))
        num.append(x) # add the input to the list
    print(num)
    return(num)

# Problem 4

def get_triangular_numbers(k):
    ''' Finds the first k triangular numbers. 
    Args:
        k: A positive integer.  
    Returns:
        A list of the first k triangular numbers,
        in order. Each element is an integer.
    Example:
        k = 6
        returns [1, 3, 6, 10, 15, 21]
    '''
    list = [i + 1 for i in range(k)] # create a list that contains the consecutive positive integer
    sums = [sum(list[:j + 1]) for j in range(len(list))] # sum up the first j integers to get the triangular numbers
    return sums


def get_consonants(s):
    ''' Finds only the consonant letters in a string.
    Args:
        s: A string that contains only lowercase alphabet letters,
        vowels, spaces, commas, and periods.
    Returns:
        A list of strings. Each element
            - is one character long,
            - is not a vowel, space, comma, nor period,
            - is in s, and
            - may appear multiple times.
        The elements appear in the same order as the letters in s.
    Example:
        s = "make it so, number one."
        returns ["m", "k", "t", "s", "n", "m", "b", "r", "n"]    
    '''
    l = ["a", "e", "i", "o", "u", " ", ",", "."] # Create a list that contains vowels, space, comma, and period
    letter = [s[i] for i in range(len(s)) if s[i] not in l]
    return letter


def get_list_of_powers(X, k):
    ''' Raise elements of a list to its powers.
    Args:
        X: A list of non-negative integers.
        k: A non-negative integer.
    Returns:
        A list of lists. The ith element is a list
        of the powers of X[i] from 0 to (and including) k, 
        in increasing order.
    Example:
        X = [5,6,7], k = 2
        returns [[1, 5, 25], [1, 6, 36], [1, 7, 49]]
    '''
    # The first half of the list comprehension creates a list of the powers,
    # The second half creates the list of the lists
    L = [[x ** y for y in range(k + 1)] for x in X] 
    return L


def get_list_of_even_powers(X, k):
    ''' Raise elements of a list to its even powers.
    Args:
        X: A list of non-negative integers.
        k: A non-negative integer. May or may not be even.
    Returns:
        A list of lists. The ith element is a list
        of the EVEN powers of X[i] from 0 to (and including) k, 
        in increasing order.
    Example:
        X = [5,6,7], k = 2
        returns [[1, 25], [1, 36], [1, 49]]
    '''
    # same format as get_list_of_powers but the first list only contains the even powers
    L = [[x ** (y * 2) for y in range(int(k / 2) + 1)] for x in X]
    return L



# Problem 5

def random_walk(ub, lb):
    ''' Simulates a simple, unbiased random walk.
    Terminates when the walk's position reaches
    the upper bound or lower bound. Initial position is 0.

    Args:
        ub: An integer. Upper bound of the walk.
        lb: An integer. Lower bound of the walk.
        You can assume ub >= lb.
    Returns:
        pos: An integer. The walk's final position.
        positions: A list of integers. A log of the walk's positions, 
        including initial but excluding final position.
        steps: A list of -1s and 1s. A log of the coin flips.
    '''
    pos = 0
    positions = [0]
    steps = []
    bound = [ub, lb]

    # keep moving until pos reaches the upper bound or the lower bound
    while pos not in bound:
        x = random.choice([-1, 1]) # randomize the direction
        steps.append(x)

        # move one step forward if the direction is 1
        # move one step backword if the direction is -1
        if x == -1: pos -= 1
        elif x == 1: pos += 1
        
        # when the pos reaches the bound, print the respective sentence and break
        if pos == ub:
            print("Upper bound at " + str(ub) + " reached")
            break
        elif pos == lb:
            print("Lower bound at " + str(lb) + " reached")
            break

        # if the pos doesn't reach the bound, add the current pos to the list
        positions.append(pos)
    return pos, positions, steps



# If you uncomment these two lines, you can run 
# the gimme_an_odd_number() function by
# running this script on your IDE or terminal. 
# Of course you can run the function in notebook as well. 
# Make sure this stays commented when you submit
# your code.
#
# if __name__ == "__main__":
#     gimme_an_odd_number()