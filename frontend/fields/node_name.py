from tkinter import Entry, StringVar
from frontend.fields.field import Field


class NodeName(Entry, Field):
    def __init__(self, master):
        super().__init__(master=master, width=12, justify="center", state="readonly")

        self.text = StringVar()
        self.config(textvariable=self.text)

        self.text.set("Node")
        self.bind("<Return>", self.hide_cursor)
        self.bind("<ButtonPress-1>", self.show_cursor)

    def get_text(self):
        return self.text.get()

    def set_text(self, new_text):
        self.text.set(new_text)

    def hide_cursor(self, event):
        self.config(state="readonly")

    def show_cursor(self, event):
        self.config(state="normal")
