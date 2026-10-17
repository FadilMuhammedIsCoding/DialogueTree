from tkinter import Entry, StringVar
from frontend.fields.field import Field


class NodeName(Entry, Field):
    def __init__(self, master):
        super().__init__(master=master, width=12, justify="center")

        self.text = StringVar()
        self.config(textvariable=self.text)

        self.text.set("Node")

    def get_text(self):
        return self.text.get()
