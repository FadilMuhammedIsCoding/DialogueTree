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
        self.drag_bar.pack(padx=padding, pady=padding, expand=True, fill="both")
        self.drag_bar.bind("<<Moving>>", self.moving)

    def get_identifier(self):
        return self.identifier

    def add_field(self, field):
        self.fields.append(field)
        if type(field) is Connector:
            field.bind("<<SearchingForNode>>", self.searching_for_node)
            field.bind("<<SearchingAborted>>", self.searching_aborted)
            field.bind("<<SearchingSuccessful>>", self.searching_successful)

        field.pack(padx=padding, pady=padding, expand=True, fill="both")

    def moving(self, event):
        self.event_generate("<<Moving>>")

    def searching_for_node(self, event):
        self.event_generate("<<SearchingForNode>>", x=event.x, y=event.y)

    def searching_aborted(self, event):
        self.event_generate("<<SearchingAborted>>")

    def searching_successful(self, event):
        self.event_generate("<<SearchingSuccessful>>")
