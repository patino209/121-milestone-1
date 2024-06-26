from bs4 import BeautifulSoup as bs
import os
import json
import sys
import nltk
from collections import defaultdict
from tokenizer import computeWordFrequencies
from posting import Posting

root = 'DEV'
docId = 0
document_map = defaultdict(str)

def get_word_frequencies(words: list):
    word_freq = computeWordFrequencies(words)
    for k, v in word_freq.items():
        word_freq[k] += v

    return word_freq

def to_json(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__)

def sort_by_docId(index: dict) -> dict:
    for _, value in index.items():
        value.sort(key = lambda x : x.docId)
    return index

def main():
    # a map with a token as a key and a list of its corresponding postings
    inverted_index = dict()
    global docId

    # Iterate through every file in DEV
    for subdir, dirs, files in os.walk(root):
        for file in files:
            document = os.path.join(subdir, file)

            # Open each file and parse content
            with open(document, "r") as doc:
                docId += 1
                
                doc_json = json.load(doc)
                content = doc_json['content']

                # Map Document ID to Document URL
                document_map[docId] = doc_json['url']

                soup = bs(content, "html.parser")
                text = soup.get_text()
                words = nltk.tokenize.word_tokenize(text)
                words = [word.lower() for word in words if word.isalnum()]

                word_frequencies = get_word_frequencies(words)

                for key, value in word_frequencies.items():
                    if key not in inverted_index.keys():
                        inverted_index[key] = []
                    # Append the posting to the inverted index
                    inverted_index[key].append(Posting(docId, value))
                
    return sort_by_docId(inverted_index)



if __name__ == "__main__":
    nltk.download('punkt')
    with open ("document_map.txt", "w") as document_map_file:
        with open ("index.txt", "w") as index:
            with open("report.txt", "w") as report:
                inv_index = main()
                count_docs = docId
                count_unique = len(inv_index.keys())
                report.write("Number of indexed documents: " + str(count_docs) + "\n")
                report.write("Number of unique words: " + str(count_unique) + "\n")
                report.write("The size of the inverted index: " + str(sys.getsizeof(inv_index) / 1000) + " KB.")

                index.write(to_json(inv_index))

                document_map_file.write(to_json(document_map))