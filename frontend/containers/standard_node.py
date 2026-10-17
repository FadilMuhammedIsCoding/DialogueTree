from tkinter import *
from frontend.globals import *
from frontend.containers.node import Node
from frontend.functionals.drag_bar import DragBar
from frontend.fields.node_name import NodeName
from frontend.functionals.field_adder import FieldAdder


class StandardNode(Node):
    def __init__(self, master, x=0, y=0):
        super().__init__(master=master, x=x, y=y)

        self.node_name = NodeName(self)
        self.add_field(self.node_name)

        self.field_adder = FieldAdder(self)
        self.field_adder.pack(padx=padding, pady=padding)

        self.context_menu = Menu(self, tearoff=False)
        self.bind("<ButtonPress-3>", self.show_context_menu)

        self.context_menu.add_command(label="Delete Node", command=self.destroy)

    def show_context_menu(self, event):
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)
