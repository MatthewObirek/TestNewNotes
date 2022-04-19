

from Python.NoteCard import NoteCard


class Chapter:

    def __init__(self, FileName: str, ChapterName) -> None:
        self.fileName = FileName
        self.openChapter()

    # TODO: write a ceateNewChapter function. and then create a button for it.

    def openChapter(self):
        # TODO: write C code for reading and writing files
        # ? NoteCardArray = CReadFunciton(self.FileName) 
        # TODO: learn Markdown
        return None


    # ! Need to Figure out how to pass in array. Maybe I dont need to, Maybe just Initalize Array in constructor, then call it.
    def saveChapter(self):
        # TODO: Import C func for writing markDown sheets
        return None 

    def exportPDF(self):
        # TODO: format for PDF, Probably do in C.
        return None

    