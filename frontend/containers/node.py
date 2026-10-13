from tkinter import Frame, Menu


class Node(Frame):
    def __init__(self, master, x=0, y=0):
        super().__init__(master=master, width=125, height=100, bg="red")

        self.x = x
        self.y = y

        self.initial_x = 0
        self.initial_y = 0

        self.bind("<ButtonPress-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_motion)
        self.bind("<ButtonRelease-1>", self.drag_stop)

        self.context_menu = Menu(master, tearoff=False)
        self.context_menu.add_command(label="Add Text Field", command=self.add_text_field)
        self.bind("<ButtonPress-3>", self.show_context_menu)

        self.place(x=self.x, y=self.y)

    def drag_start(self, event):
        self.initial_x = event.x
        self.initial_y = event.y

    def drag_motion(self, event):
        self.x = self.winfo_x() - self.initial_x + event.x
        self.y = self.winfo_y() - self.initial_y + event.y
        self.place(x=self.x, y=self.y)

    def drag_stop(self, event):
        pass

    def show_context_menu(self, event):
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)

    def add_text_field(self):
        print(True)
