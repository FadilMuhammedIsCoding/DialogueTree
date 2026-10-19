from tkinter import Label
from frontend.fields.connector_subnodes.connection_receiver import ConnectionReceiver


class ConnectionSender(Label):
    def __init__(self, master):
        super().__init__(master=master, width=3, text="O", relief="raised")
        self.master = master

        self.current_connection_receiver = None

        self.bind("<ButtonPress-1>", self.mouse_pressed)
        self.bind("<B1-Motion>", self.mouse_motion)
        self.bind("<ButtonRelease-1>", self.mouse_release)

    def get_current_connection_receiver(self):
        return self.current_connection_receiver

    def mouse_pressed(self, event):
        pass

    def mouse_motion(self, event):
        detected_widget = self.winfo_containing(event.x_root, event.y_root)
        self.current_connection_receiver = None

        if type(detected_widget) is not ConnectionReceiver or self.master == detected_widget.master:
            self.event_generate("<<InvalidConnection>>")
            return

        self.current_connection_receiver = detected_widget
        self.event_generate("<<ValidConnection>>")

    def mouse_release(self, event):
        pass
