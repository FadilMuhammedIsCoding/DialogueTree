from tkinter import *
from frontend.fields.field import Field


class TextField(Frame, Field):
    def __init__(self, master):
        super().__init__(master=master, bg="blue")

        self.id_label = Label(self, text="ID: ")
        self.id_label.pack(side=LEFT, expand=True, fill=BOTH)

        self.id = Entry(self, width=10)
        self.id.pack(side=LEFT, expand=True, fill=BOTH)

        self.data_label = Label(self, text="Label: ")
        self.data_label.pack(side=LEFT, expand=True, fill=BOTH)

        self.data = Text(self, width=20, height=1, wrap="word")
        self.data.pack(side=LEFT, expand=True, fill=BOTH)

        self.data.bind("<<Modified>>", self.resize_containers)

    def get_id(self):
        return self.id.get()

    def get_data(self):
        return self.data.get("1.0", "end-1c")

    def resize_containers(self, event):
        line_count = self.data.count("1.0", "end", "displaylines")[0]
        self.data.config(height=line_count)

        self.id_label.pack(side=LEFT, expand=True, fill=BOTH)
        self.id.pack(side=LEFT, expand=True, fill=BOTH)
        self.data_label.pack(side=LEFT, expand=True, fill=BOTH)
        self.data.pack(side=LEFT, expand=True, fill=BOTH)

        self.data.edit_modified(False)
