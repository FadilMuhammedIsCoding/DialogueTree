from tkinter import *
from frontend.globals import *
from frontend.fields.text_field import TextField
from frontend.functionals.drag_bar import DragBar


class Node(Frame):
    def __init__(self, master, x=0, y=0):
        super().__init__(master=master, bg="red")
        self.fields = []

        self.x = x
        self.y = y

        self.initial_x = 0
        self.initial_y = 0

        self.drag_bar = DragBar(self)
        self.drag_bar.pack(padx=padding, pady=padding, expand=True, fill=X)

    def add_field(self, field):
        self.fields.append(field)
        field.pack(padx=padding, pady=padding)
