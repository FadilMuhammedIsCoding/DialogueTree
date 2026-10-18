from tkinter import Canvas, Menu
from frontend.containers.standard_node import StandardNode


class Collection(Canvas):
    def __init__(self, master):
        super().__init__(master=master, bg="lightgrey")
        self.nodes = []

        self.scale = 1.0
        self.grid_size = 16

        self.global_initial_x = 0
        self.global_initial_y = 0

        self.last_right_click_x = 0
        self.last_right_click_y = 0

        self.bind("<MouseWheel>", self.zoom)

        self.bind("<ButtonPress-2>", self.move_press)
        self.bind("<B2-Motion>", self.move_motion)
        self.bind("<ButtonRelease-2>", self.move_release)

        self.context_menu = Menu(self, tearoff=False)
        self.bind("<ButtonPress-3>", self.show_context_menu)

        self.grid_canvas = Canvas(self, state="disabled")

        self.context_menu.add_command(label="Make New Node", command=self.make_new_node)

    def add_node(self, node):
        self.nodes.append(node)

    def make_new_node(self):
        new_node = StandardNode(self, x=self.last_right_click_x, y=self.last_right_click_y)
        self.add_node(new_node)

    def show_context_menu(self, event):
        self.last_right_click_x = event.x
        self.last_right_click_y = event.y
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)

    def draw_grid(self, offset_x=0, offset_y=0):
        self.update()

        for column in range(0, (self.winfo_width() // self.grid_size) + 1):
            self.create_line(
                column * self.grid_size, offset_y, column * self.grid_size, self.winfo_height(), fill="darkgrey", width=2
            )

        for row in range(0, (self.winfo_height() // self.grid_size) + 1):
            self.create_line(
                offset_x, row * self.grid_size, self.winfo_width(), row * self.grid_size, fill="darkgrey", width=2
            )

    def move_press(self, event):
        self.config(cursor="fleur")

        self.global_initial_x = event.x
        self.global_initial_y = event.y

    def move_motion(self, event):
        dx = event.x - self.global_initial_x
        dy = event.y - self.global_initial_y

        for node in self.nodes:
            node.x += dx
            node.y += dy
            node.place(x=node.x, y=node.y)

        self.global_initial_x = event.x
        self.global_initial_y = event.y

    def move_release(self, event):
        self.config(cursor="arrow")

    def zoom(self, event):
        if event.delta == -120:
            self.scale = max(0.5, self.scale - 0.1)
        if event.delta == 120:
            self.scale = min(3.0, self.scale + 0.1)
