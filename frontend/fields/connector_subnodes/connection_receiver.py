from tkinter import Label, Frame


class ConnectionReceiver(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.master = master

        self.connector = Label(self, text=" * ")
        self.connector.pack(expand=True, side="left")

        self.info_label = Label(self)
        self.info_label.pack(expand=True, side="left")

    def get_parent_node_name(self):
        return self.master.get_name()

    def get_connecting_position(self):
        x = self.winfo_rootx() + (self.winfo_width() // 2)
        y = self.winfo_rooty() + (self.winfo_height() // 2)
        return x, y
