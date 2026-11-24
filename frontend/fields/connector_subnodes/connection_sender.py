from tkinter import Frame, Label


class ConnectionSender(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.master = master

        self.current_connected_node = None

        self.info_text = Label(self, text="Connected to: ")
        self.info_text.pack(expand=True, side="left")

        self.connected_node_name = Label(self, text="None")
        self.connected_node_name.pack(expand=True, side="left")

        self.connector = Label(self, text=" O ")
        self.connector.pack(expand=True, side="left")

        self.connector.bind("<ButtonPress-1>", self.mouse_pressed)
        self.connector.bind("<B1-Motion>", self.mouse_motion)
        self.connector.bind("<ButtonRelease-1>", self.mouse_release)

    def reset(self):
        self.current_connected_node = None
        self.connected_node_name.config(text="None")

    def belongs_to_receiver(self, widget):
        current_widget = widget

        from frontend.containers.standard_node import StandardNode
        if type(current_widget) is StandardNode:
            return current_widget
        if current_widget == self.winfo_toplevel() or current_widget is None:
            return None

        return self.belongs_to_receiver(current_widget.master)

    def get_connecting_position(self):
        x = self.connector.winfo_rootx() + (self.connector.winfo_width() // 2)
        y = self.connector.winfo_rooty() + (self.connector.winfo_height() // 2)
        return x, y

    def mouse_pressed(self, event):
        self.event_generate("<<SearchStarted>>")
        self.reset()

    def mouse_motion(self, event):
        self.event_generate("<<Searching>>", x=event.x_root, y=event.y_root)
        self.reset()

        detected_widget = self.winfo_containing(event.x_root, event.y_root)
        connection_receiver = self.belongs_to_receiver(detected_widget)
        if connection_receiver is None: return

        self.current_connected_node = connection_receiver
        self.connected_node_name.config(text=connection_receiver.get_name())

    def mouse_release(self, event):
        self.event_generate("<<SearchEnded>>")
        if self.current_connected_node is None: return
        self.current_connected_node.bind("<<Deleted>>", self.on_connecting_node_deleted)

    def on_connecting_node_deleted(self, event):
        self.current_connected_node = None

    def get_connector_name(self):
        if self.current_connected_node is None: return "end"
        else: return self.current_connected_node.get_name()
