from tkinter import Entry, StringVar


class NodeName(Entry):
    def __init__(self, master):
        super().__init__(master=master, width=12, justify="center")

        self.text = StringVar()
        self.config(textvariable=self.text)

        self.text.set("Node")
