from bs4 import BeautifulSoup as bs
import os

directory = 'DEV'

def main():
    # a map with a token as a key and a list of its corresponding postings
    inverted_index = dict()

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)




    



if __name__ == "__main__":
    main()