import json

data = None
doc_map = None

# ANDs two lists of document ids
def merge_ids(ids1: list, ids2: list):
    token1_index = 0
    token2_index = 0
    merged_did = []

    # Merge the two postings by intersecting the document sets
    while token1_index < len(ids1) and token2_index < len(ids2):
        if ids1[token1_index] == ids2[token2_index]:
            merged_did.append(ids1[token1_index])
            token1_index += 1
            token2_index += 1
        elif ids1[token1_index] < ids2[token2_index]:
            token1_index += 1
        else:
            token2_index += 1

    return merged_did

# Retrieve all docs in which a token appeared
def retrieve_ids(token: str):
    dids = []
    for info in data[token]:
        dids.append(info["docId"])
    return dids

# Perform AND boolean search on list of tokens
def and_search(tokens: list):
    all_dids = []
    # Merge all docIds using the AND boolean operator
    for index, token in enumerate(tokens):
        if index == 0:
            all_dids = retrieve_ids(token.lower())
        else:
            all_dids = merge_ids(all_dids, retrieve_ids(token.lower()))

    urls = []
    # With the intersections, retrieve the urls
    for did in all_dids:
        # Retrieve the urls associated with that docId
        urls.append(doc_map[str(did)])

    return urls[:5]

# Loads the index and document maps into memory
def load_index():
    global data
    global doc_map

    # Load index from disk to memory
    with open("backend/index.txt", "r") as file:
        data = file.read()
        data = json.loads(data)

    # Load the dictionary that maps docIds to their respective urls in memory
    with open("backend/document_map.txt", "r") as file:
        doc_map = file.read()
        doc_map = json.loads(doc_map)

if __name__ == "__main__":
    urls = and_search(["cristina", "lopes"])
    print(urls)