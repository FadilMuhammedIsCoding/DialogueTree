from tkinter import Label


class ConnectionSender(Label):
    def __init__(self, master):
        super().__init__(master=master, width=3, text="O", relief="raised")
        self.master = master
