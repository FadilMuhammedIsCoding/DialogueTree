from tkinter import Label
from frontend.functionals.functional import Functional


class DragBar(Label, Functional):
    def __init__(self, master):
        super().__init__(master=master, text="==", height=1, cursor="hand2")

        self.bind("<ButtonPress-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_motion)
        self.bind("<ButtonRelease-1>", self.drag_stop)

        self.master.place(x=self.master.x, y=self.master.y)

    def drag_start(self, event):
        self.master.initial_x = event.x
        self.master.initial_y = event.y

    def drag_motion(self, event):
        self.master.x = self.master.winfo_x() - self.master.initial_x + event.x
        self.master.y = self.master.winfo_y() - self.master.initial_y + event.y
        self.master.place(x=self.master.x, y=self.master.y)

    def drag_stop(self, event):
        pass
