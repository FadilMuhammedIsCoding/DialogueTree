from tkinter import *


class TextField(Frame):
    def __init__(self, master):
        super().__init__(master=master, bg="blue")

        self.id = Entry(self, width=10)
        self.id.pack(side=LEFT, expand=True, fill=BOTH)

        self.data = Entry(self, width=10)
        self.data.pack(side=LEFT, expand=True, fill=BOTH)
