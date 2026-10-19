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

        self.original_width = 100
        self.original_height = 100

        self.initial_x = 0
        self.initial_y = 0

        self.drag_bar = DragBar(self)
        self.drag_bar.pack(padx=padding, pady=padding, expand=True, fill="both")
        self.drag_bar.bind("<<Moving>>", self.signal_change)

    def add_field(self, field):
        self.fields.append(field)
        if type(field) is Connector: field.bind("<<SearchingForNode>>", self.signal_change)
        field.pack(padx=padding, pady=padding, expand=True, fill="both")

    def signal_change(self, event):
        self.event_generate("<<Moving>>")
