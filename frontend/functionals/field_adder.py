import tkinter
from tkinter import Button, Menu
from frontend.fields.text_field import TextField
from frontend.globals import *
from frontend.functionals.functional import Functional


class FieldAdder(Button, Functional):
    def __init__(self, master):
        super().__init__(master=master, width=10, height=1, text="+Add Field")
        self.add_event_string = "<<AddedWidget>>"
        self.last_added_field = None

        self.config(command=self.show_context_menu)

        self.context_menu = Menu(self, tearoff=False)
        self.context_menu.add_command(label="Add Text Field", command=self.add_text_field)

    def get_last_added_field(self):
        return self.last_added_field

    def show_context_menu(self):
        self.context_menu.tk_popup(x=self.winfo_rootx(), y=self.winfo_rooty() + self.winfo_height())

    def add_text_field(self):
        text_field = TextField(self.master)
        self.master.add_field(text_field)
