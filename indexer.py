from bs4 import BeautifulSoup as bs
import os
import json
from tokenizer import computeWordFrequencies
from document import Document

root = 'DEV'

def get_word_frequencies(words: list):
    word_freq = computeWordFrequencies(words)
    for k, v in word_freq.items():
        word_freq[k] += v

    return word_freq


def main():
    # a map with a token as a key and a list of its corresponding postings
    inverted_index = dict()

    # Iterate through every file in DEV
    for subdir, dirs, files in os.walk(root):
        for file in files:
            document = os.path.join(subdir, file)

            # Open each file and parse content
            with open(document, "r") as doc:
                doc_json = json.load(doc)
                content = doc_json['content']

                soup = bs(content, "html.parser")
                text = soup.get_text()
                words = text.split()
                words = [word.lower() for word in words if word.isalnum()]

                word_frequencies = get_word_frequencies(words)

                # Create a document object to store information about the document
                doc_obj = Document(word_frequencies)
                print(doc_obj.getDocId())

                




    



if __name__ == "__main__":
    main()