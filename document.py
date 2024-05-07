class Document:
    personal_docId: int
    docId: int
    token_frequency: dict

    def __init__(self, token_frequency) -> None:
        Document.docId += 1
        self.personal_docId = Document.docId
        self.token_frequency = token_frequency

    def getDocId(self):
        return self.personal_docId