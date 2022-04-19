from tkinter import *
#from chatbot import Botler
#
BG_COLOR = "#272727"
TEXT_COLOR = "#FAFAFA"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:
    """Runs application """

    def __init__(self):
        """Generates window GUI an initializes Chatbot"""
        self._init_window()

    def _init_window(self):
        """Initializes window with corresponding settings"""
        self.window = Tk()

        """Runs main loop for window"""
        self.window.mainloop()

    # TODO: Widgets that can replace other Widgets -> Changing pages.
    
    
    # TODO: Settings butten -> Settings page
    # TODO: Content Widgets
    # TODO: Content Book Page -> displays a link web of chapters, and related ideas.
    # TODO: Content Chapter Page -> displays web of NoteCards -> add Note button
    # TODO: Content Display page
    # TODO: Tabs for chapters -> for granularity

   

newApp = ChatApplication()
newApp.run()