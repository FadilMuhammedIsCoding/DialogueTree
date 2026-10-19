from tkinter import Frame, Label
from frontend.fields.connector_subnodes.connection_receiver import ConnectionReceiver
from frontend.fields.connector_subnodes.connection_sender import ConnectionSender


class Connector(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.master = master

        self.connection_receiver = ConnectionReceiver(self, self.master)
        self.connection_receiver.pack(expand=True, side="left")

        self.label = Label(self, text="Connected to: ")
        self.label.pack(expand=True, side="left")

        self.connected_node_text = Label(self, width=10, text="null")
        self.connected_node_text.pack(expand=True, side="left")

        self.connection_sender = ConnectionSender(self)
        self.connection_sender.pack(expand=True, side="left")

        self.connection_sender.bind("<<ValidConnection>>", self.set_valid_connected_node)
        self.connection_sender.bind("<<InvalidConnection>>", self.set_invalid_connected_node)
        self.connection_sender.bind("<B1-Motion>", self.connection_deciding)

    def get_currently_connected_connection_receiver(self):
        return self.connection_sender.get_current_connection_receiver()

    def get_local_connection_sender(self):
        return self.connection_sender

    def connection_deciding(self, event):
        self.event_generate("<<SearchingForNode>>")

    def update_connected_node(self, event):
        node = self.get_currently_connected_connection_receiver().get_parent_node()
        self.connected_node_text.config(text=node.get_name())
        return node

    def set_valid_connected_node(self, event):
        node = self.update_connected_node(None)
        node.bind("<<NameChanged>>", self.update_connected_node)

    def set_invalid_connected_node(self, event):
        self.connected_node_text.config(text="null")
