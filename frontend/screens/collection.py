from tkinter import Canvas


class Collection(Canvas):
    def __init__(self, master):
        super().__init__(master=master, bg="lightgrey")

        self.grid_size = 16

        self.number_of_nodes = 0

        self.global_initial_x = 0
        self.global_initial_y = 0

        self.last_right_click_x = 0
        self.last_right_click_y = 0

        self.bind("<ButtonPress-2>", self.move_press)
        self.bind("<B2-Motion>", self.move_motion)
        self.bind("<ButtonRelease-2>", self.move_release)

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
