from tkinter import Label


class ConnectionReceiver(Label):
    def __init__(self, master, parent_node):
        super().__init__(master=master, width=3, text="*", relief="raised")
        self.master = master
        self.parent_node = parent_node

    def get_parent_node(self):
        return self.parent_node
