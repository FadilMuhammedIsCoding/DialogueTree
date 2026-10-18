from tkinter import *
from frontend.fields.field import Field


class TextField(Frame, Field):
    def __init__(self, master):
        super().__init__(master=master, bg="blue")

        self.id_label = Label(self, text="ID: ")
        self.id_label.pack(side=LEFT, expand=True, fill=BOTH)

        self.id = Entry(self, width=5)
        self.id.pack(side=LEFT, expand=True, fill=BOTH)
        self.id.bind("<KeyRelease>", self.resize_horizontal)

        self.data_label = Label(self, text="Label: ")
        self.data_label.pack(side=LEFT, expand=True, fill=BOTH)

        self.data = Text(self, width=10, height=1, wrap="word")
        self.data.pack(side=LEFT, expand=True, fill=BOTH)
        self.data.bind("<<Modified>>", self.resize_vertical)

    def get_id(self):
        return self.id.get()

    def get_data(self):
        return self.data.get("1.0", "end-1c")

    def update_widgets(self):
        self.id_label.pack(side=LEFT, expand=True, fill=BOTH)
        self.id.pack(side=LEFT, expand=True, fill=BOTH)
        self.data_label.pack(side=LEFT, expand=True, fill=BOTH)
        self.data.pack(side=LEFT, expand=True, fill=BOTH)

    def resize_horizontal(self, event):
        column_count = max(len(self.id.get()) + 1, 5)
        self.id.config(width=column_count)
        self.update_widgets()

    def resize_vertical(self, event):
        line_count = self.data.count("1.0", "end", "displaylines")[0]
        column_count = min(max(self.data.count("1.0", "end", "displaychars")[0], 10), 20)
        self.data.config(width=column_count, height=line_count)
        self.update_widgets()
        self.data.edit_modified(False)
