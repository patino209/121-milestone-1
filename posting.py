class Posting:
    docId: int
    score: int

    def __init__(self, docId, score) -> None:
        self.docId = docId
        self.score = score

    
    def getScore(self):
        return self.score
    
    
    def getDocId(self):
        return self.docId
    
    def __str__(self) -> str:
        return str(self.docId) + ': ' + str(self.score)