from tkinter import *
from frontend.globals import *
from frontend.fields.connector import Connector
from frontend.functionals.drag_bar import DragBar


class Node(Frame):
    def __init__(self, master, x=0, y=0):
        super().__init__(master=master, bg="darkgrey", width=100, height=100)
        self.fields = []

        self.x = x
        self.y = y

        self.identifier = ""

        self.original_width = 100
        self.original_height = 100

        self.initial_x = 0
        self.initial_y = 0

        self.drag_bar = DragBar(self)
        self.drag_bar.bind("<<Moving>>", lambda event: self.event_generate("<<Moving>>"))
        self.drag_bar.pack(padx=padding, pady=padding, expand=True, fill="both")

    def get_identifier(self):
        return self.identifier

    def add_field(self, field):
        self.fields.append(field)
        field.pack(padx=padding, pady=padding, expand=True, fill="both")

    def get_connecting_position(self):
        x = self.winfo_rootx() + (self.winfo_width() // 2)
        y = self.winfo_rooty() + (self.winfo_height() // 2)
        return x, y
