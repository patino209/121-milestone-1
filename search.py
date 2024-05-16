import json

data = None

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
    
    if token1_index < len(ids1):
        merged_did += ids1[token1_index:]
    elif token2_index < len(ids2):
        merged_did += ids2[token2_index:]

    return merged_did


def retrieve_ids(token: str):
    dids = []
    for info in data[token]:
        dids.append(info["docId"])
    return dids

def and_search(tokens: list):
    global data
    with open("index.txt", "r") as file:
        data = file.read()
    data = json.loads(data)
    # Retrieve the dictionary that maps docIds to their respective urls
    with open("document_map.txt", "r") as file:
        doc_map = file.read()
    doc_map = json.loads(doc_map)

    all_dids = []

    # Merge all docIds using the AND boolean operator
    for token in tokens:
        all_dids = merge_ids(all_dids, retrieve_ids(token.lower()))

    urls = []

    # With the intersections, retrieve the urls
    for did in all_dids:
        # Retrieve the urls associated with that docId
        urls.append(doc_map[str(did)])

    return urls

if __name__ == "__main__":

    urls = and_search(["cristina", "lopes"])
    print(urls)