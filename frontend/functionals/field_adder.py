import tkinter
from tkinter import Button, Menu
from frontend.fields.text_field import TextField
from frontend.globals import *


class FieldAdder(Button):
    def __init__(self, master):
        super().__init__(master=master, width=10, height=1, text="+Add Field")
        self.master = master

        self.config(command=self.show_context_menu)

        self.context_menu = Menu(self, tearoff=False)
        self.context_menu.add_command(label="Add Text Field", command=self.add_text_field)

    def show_context_menu(self):
        self.context_menu.tk_popup(x=self.winfo_rootx(), y=self.winfo_rooty() + self.winfo_height())

    def add_text_field(self):
        text_field = TextField(self.master)
        text_field.pack(padx=padding, pady=padding)
