import sys

# Time complexity: O(n) where n is the size of the input token list. This function simply iterates over every token in the token list and increments a counter, which happens in constant time.
    # Because of this, O(n) is the bound for the function.
def computeWordFrequencies(tokens: list) -> dict:
    '''Counts the number of occurrences of each token in the token list.
    
    in  -> Tokens
    out -> Map of tokens to their respective count
    '''
    # create a dictionary for the mappings
    frequencies = {}

    # iterate over every token and increment its counter in the dictionary
    for token in tokens:
        if token not in frequencies:
            frequencies[token] = 1
        else:
            frequencies[token] += 1

    # return the token frequencies dictionary
    return frequencies