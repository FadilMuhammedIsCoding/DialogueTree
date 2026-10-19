import tkinter
from tkinter import Button, Menu
from frontend.fields.text_field import TextField
from frontend.functionals.functional import Functional
from frontend.fields.connector import Connector


class FieldAdder(Button, Functional):
    def __init__(self, master):
        super().__init__(master=master, width=10, height=1, text="+Add Field")
        self.add_event_string = "<<AddedWidget>>"
        self.last_added_field = None

        self.config(command=self.show_context_menu)

        self.context_menu = Menu(self, tearoff=False)
        self.context_menu.add_command(label="Add Text Field", command=self.add_text_field)
        self.context_menu.add_command(label="Add Connector Field", command=self.add_connector_field)

    def get_last_added_field(self):
        return self.last_added_field

    def show_context_menu(self):
        self.context_menu.tk_popup(x=self.winfo_rootx(), y=self.winfo_rooty() + self.winfo_height())

    def add_text_field(self):
        text_field = TextField(self.master)
        self.master.add_field(text_field)

    def add_connector_field(self):
        connector_field = Connector(self.master)
        self.master.add_field(connector_field)
