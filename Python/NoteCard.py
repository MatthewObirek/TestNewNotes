


class NoteCard:

    def __init__(self, Idea: str, Explanation: str) -> None:
        self.idea = Idea
        self.explanation = Explanation


    # * getters and Setters
    def getIdea(self, Idea: str):
        self.idea = Idea

    def getIdea(self):
        return self.idea

    def setExplanation(self, Explanation: str):
        self.explanation = Explanation

    def getExplanation(self):
        return self.explanation

    # ! may be moved to Chapter.py
    def getLinks(self):
        # TODO: go through and read markdown links.
        links = 'TODO'
        return links


        # TODO: get 

    