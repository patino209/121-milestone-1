import sys
from builtins import print as python_print


# Time complexity: O(1) or constant time. Comparisons in Python using comparators like '<=' run in constant time and the length of the input will always be 1.
def isAlphaNum(character: str) -> bool:
    '''Takes in a character and returns a boolean representing whether or not it is alphanumeric
    
    in  -> character
    out -> bool
    '''
    return ('A' <= character <= "Z" or 'a' <= character <= 'z' or '0' <= character <= '9')


# Time complexity: O(n*m) where n is the length of the input file and m is the length of the current token string. The function reads one character at a time for every character in the input file, 
    # which has a length of n. This means it would take O(n) time to iterate through every character. The process of calling .lower() on each character runs in O(1) because the size of the 
    # character is always 1. Furthermore, checking if variables are empty is also done in constant time in Python in this case. Lastly, functions such as append are also constant. 
    # However, concatenating to the end of the string must copy the entire string and create a new one which is an O(m) operation where m is the length of the current token string.
    # Because of all of this, the total runtime complexity would be O(n*m).
def tokenize(filePath: str) -> list:
    '''Reads in a text file and returns a list of the tokens in that file.
    
    in  -> TextFilePath
    out -> Token List
    '''
    # error-handling for if the file does not exist
    try:
        # opens the text file in read mode
        file = open(filePath, 'r', encoding="utf8")
        tokens = []
        cur_token = ""
        # read each character one at a time
        while True:
            character = file.read(1)
            character = character.lower()

            # if we have reached the end of the file, break out of the file loop
            if not character:
                # append the last token
                if cur_token:
                    tokens.append(cur_token)
                    cur_token = ""
                break
            elif isAlphaNum(character): # if the character is alphanumeric, append to the current token
                cur_token += character
            else: # if the character is not alphanumeric, end the previous token and prepare for the next token
                if cur_token:
                    tokens.append(cur_token)
                    cur_token = ""

        # return the accumulated tokens
        return tokens
    except FileNotFoundError: # error-handling for if the file does not exist
        file = None
        python_print('File does not exist')
        return []
    except IOError: # error-handling for any errors reading the contents of the file
        file = None
        python_print('Error reading the contents of the file')
        return []
    finally:
        # closes the file
        if file:
            file.close()


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