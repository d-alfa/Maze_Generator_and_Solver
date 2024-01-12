
from tkinter import Tk, BOTH, Canvas

class WINDOW:

    def __init__(self, width, height, title):
        self.__root = Tk() # Creates the new root widget
        self.__root.geometry(f"{width}x{height}") # Sets the size of the window using the width and height parameters
        self.__root.title(title) # Set the window title

        self.__canvas = Canvas(self.__root) # Create the Canvas
        self.__canvas.pack(fill=BOTH, expand=1) # Make the Canvas fill the window

        self.__isRunning = False # Running state attribute

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()