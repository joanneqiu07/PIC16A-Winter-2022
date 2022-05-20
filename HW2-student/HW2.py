# HW2
# Name: Joanne Qiu
# Collaborators: N/A
# Date: 01/20/2021

from queue import Empty
import random

def count_characters(s):
    """Count the number of occurrences of each character in a string. 
    Args:
        s: str, the string in which to count. 
    Returns:
        a dict keyed by characters whose values are the number of occurrences in s
    """
    D = {} # create the dictionary that needs to be returned

    for i in range(len(s)):
        D[s[i]] = 0 # initialize the argument names
    
    for i in range(len(s)):
        D[s[i]] += 1 # update the argument values

    return D


def count_ngrams(s, n = 1):
    """Count the number of occurrences of n-grams in a string. 
    Args:
        s: str.
        n: positive int. should have default value 1.
    Returns:
        a dict keyed by n-grams whose values are the number of occurrences in s
    """
    D = {} # create the dictionary that needs to be returned

    for i in range(len(s) - n + 1):
        D[s[i:(n + i)]] = 0 # initialize the argument names
    
    for i in range(len(s) - n + 1):
        D[s[i:(n + i)]] += 1 # update the argument values

    return D


def markov_text(s, n, length = 100, seed = "Emma Woodhouse"):
    """Generate fake text according to an n-th order Markov model, with data from a user-supplied corpus. 
    Args:
        s: str. the text from which to learn grams.
        n: positive int. the order of the Markov model. 
        length: positive int. the number of synthetic characters to generate. should have a default value. 
        seed: str. should have a default value.
    Returns:
        The output string fake_text. fake_text starts with the seed. 
        length of fake_text = length of seed + argument 'length'
    """
    ngrams = count_ngrams(s, n + 1) # compute the (n+1)-grams' frequencies

    fake_text = seed # initialize the string fake_text with the seed

    rct_chr = seed[(len(seed) - n):len(seed)] # find the n most recent character from the seed

    for i in range(length):
        options = [i[n] for i in ngrams if i[0:n] == rct_chr] # the list contains the last character of the n+1-grams that have rct_chr as the foremost part
        
        if len(options) == 0: 
            print("The text doesn't have " + str(n+1) + "-gram that contains " + rct_chr + " as the foremost part\n")
            print("The final generated text is " + fake_text)
            break

        total = sum(ngrams[i] for i in ngrams if i[0:n] == rct_chr) # the total number of (n+1)-grams that have rct_chr as the foremost part
        weights = [ngrams[i] / total for i in ngrams if i[0:n] == rct_chr] # the list contains the weight of each of the character in options
        fake_text = fake_text + random.choices(options, weights)[0] # add the randomized choice of the character to the fake_text
        rct_chr = fake_text[(len(fake_text) - n):len(fake_text)] # find the n most recent character from the updated fake_text
    
    return fake_text




