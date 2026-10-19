from tkinter import *
from frontend.globals import *
from frontend.containers.node import Node
from frontend.fields.node_name import NodeName
from frontend.functionals.field_adder import FieldAdder
from frontend.fields.connector import Connector


class StandardNode(Node):
    def __init__(self, master, x=0, y=0):
        super().__init__(master=master, x=x, y=y)

        self.node_name = NodeName(self)
        self.fields.append(self.node_name)
        self.node_name.bind("<KeyRelease>", self.name_updated)
        self.node_name.pack(padx=padding, pady=padding, expand=True, fill="both")

        self.field_adder = FieldAdder(self)
        self.field_adder.pack(padx=padding, pady=padding, expand=True, fill="both")

        self.context_menu = Menu(self, tearoff=False)
        self.bind("<ButtonPress-3>", self.show_context_menu)

        self.context_menu.add_command(label="Delete Node", command=self.destroy)
        self.context_menu.add_command(label="print name", command=self.get_name)

    def get_connector(self):
        for field in self.fields:
            if type(field) is Connector: return field

        return None

    def get_name(self):
        return self.node_name.get_text()

    def name_updated(self, event):
        self.event_generate("<<NameChanged>>")

    def show_context_menu(self, event):
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)
