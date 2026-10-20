from tkinter import Frame, Label
from frontend.fields.connector_subnodes.connection_receiver import ConnectionReceiver
from frontend.fields.connector_subnodes.connection_sender import ConnectionSender


class Connector(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.master = master

        self.current_connected_connection_receiver = None
        self.current_connected_connection_sender = None

        self.connection_receiver = ConnectionReceiver(self, self.master)
        self.connection_receiver.pack(expand=True, side="left")

        self.label = Label(self, text="Connected to: ")
        self.label.pack(expand=True, side="left")

        self.connected_node_text = Label(self, width=10, text="null")
        self.connected_node_text.pack(expand=True, side="left")

        self.connection_sender = ConnectionSender(self)
        self.connection_sender.pack(expand=True, side="left")

        self.connection_sender.bind("<ButtonPress-1>", self.mouse_pressed)
        self.connection_sender.bind("<B1-Motion>", self.mouse_motion, add='+')
        self.connection_sender.bind("<B1-Motion>", self.search_event_generate, add='+')
        self.connection_sender.bind("<ButtonRelease-1>", self.mouse_release)

    def get_currently_connected_connection_receiver(self):
        return self.current_connected_connection_receiver

    def set_currently_connected_connection_receiver(self, new_connection_receiver):
        self.current_connected_connection_receiver = new_connection_receiver

    def get_currently_connected_connection_sender(self):
        return self.current_connected_connection_sender

    def set_currently_connected_connection_sender(self, new_connection_sender):
        self.current_connected_connection_sender = new_connection_sender

    def get_local_connection_sender(self):
        return self.connection_sender

    def mouse_pressed(self, event):
        pass

    def search_event_generate(self, event):
        self.event_generate("<<SearchingForNode>>", x=event.x_root, y=event.y_root)

    def mouse_motion(self, event):
        self.event_generate("<<ChangingConnectedNode>>")

        detected_widget = self.winfo_containing(event.x_root, event.y_root)
        self.current_connected_connection_receiver = None

        if type(detected_widget) is not ConnectionReceiver or self.master == detected_widget.master:
            self.set_invalid_connected_node()
            return

        self.set_currently_connected_connection_receiver(detected_widget)
        connector = detected_widget.master
        connector.set_currently_connected_connection_sender(self.connection_sender)
        self.bind("<<ChangingConnectedNode>>", connector.reset)

        self.set_valid_connected_node()
        self.update_text_to_connected_node(None)

    def mouse_release(self, event):
        if self.current_connected_connection_receiver is None:
            self.event_generate("<<SearchingAborted>>")
            return

        self.event_generate("<<SearchingSuccessful>>")

    def reset(self, event):
        self.current_connected_connection_sender = None

    def update_text_to_connected_node(self, event):
        connector = self.current_connected_connection_receiver.master
        self.connected_node_text.config(text=connector.master.get_name())

    def set_valid_connected_node(self):
        connector = self.current_connected_connection_receiver.master
        connector.master.bind("<<NameChanged>>", self.update_text_to_connected_node)

    def set_invalid_connected_node(self):
        self.connected_node_text.config(text="null")
