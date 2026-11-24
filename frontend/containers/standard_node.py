from tkinter import *
from frontend.globals import *
from frontend.containers.node import Node
from frontend.fields.node_name import NodeName
from frontend.functionals.field_adder import FieldAdder
from frontend.fields.connector_subnodes.connection_sender import ConnectionSender


class StandardNode(Node):
    def __init__(self, master, x=0, y=0):
        super().__init__(master=master, x=x, y=y)

        self.node_name = NodeName(self)
        self.fields.append(self.node_name)
        self.node_name.pack(padx=padding, pady=padding, expand=True, fill="both")

        self.field_adder = FieldAdder(self)
        self.field_adder.bind("<<ConnectionSenderAdded>>", lambda event: self.event_generate("<<ConnectionSenderAdded>>"))
        self.field_adder.pack(padx=padding, pady=padding, expand=True, fill="both")

        self.context_menu = Menu(self, tearoff=False)
        self.bind("<ButtonPress-3>", self.show_context_menu)

        self.context_menu.add_command(label="Delete Node", command=self.delete_node)
        self.context_menu.add_command(label="print name", command=self.get_name)

    def show_context_menu(self, event):
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)

    def delete_node(self):
        self.destroy()

    def get_name(self):
        return self.node_name.get_text()

    def set_name(self, new_name):
        self.node_name.set_text(new_name)
