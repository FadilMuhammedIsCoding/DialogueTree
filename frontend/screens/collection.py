from tkinter import Canvas, Menu
from frontend.containers.standard_node import StandardNode
from frontend import globals


class Collection(Canvas):
    def __init__(self, master):
        super().__init__(master=master, bg="lightgrey")
        self.nodes = []
        self.connecting_line_ids = []

        self.grid_size = 16

        self.last_right_click_x = 0
        self.last_right_click_y = 0

        self.bind("<ButtonPress-2>", self.move_press)
        self.bind("<B2-Motion>", self.move_motion)
        self.bind("<ButtonRelease-2>", self.move_release)

        self.context_menu = Menu(self, tearoff=False)
        self.bind("<ButtonPress-3>", self.show_context_menu)

        self.grid_canvas = Canvas(self, state="disabled")

        self.context_menu.add_command(label="Make New Node", command=self.make_new_node)

        self.bind("<ButtonPress-1>", self.draw_connecting_lines)

    def add_node(self, node):
        node.bind("<<Changed>>", self.draw_connecting_lines)
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

        self.draw_connecting_lines(None)

        self.global_initial_x = event.x
        self.global_initial_y = event.y

    def move_release(self, event):
        self.config(cursor="arrow")

    def draw_connecting_lines(self, event):
        self.update()

        for line_id in self.connecting_line_ids:
            self.delete(line_id)

        self.connecting_line_ids.clear()

        for node in self.nodes:
            current_connector = node.get_connector()
            if current_connector is None: break

            sender = current_connector.get_local_connection_sender()
            receiver = current_connector.get_currently_connected_connection_receiver()

            x0 = (sender.winfo_rootx() + (sender.winfo_width() // 2)) - self.winfo_rootx()
            y0 = (sender.winfo_rooty() + (sender.winfo_height() // 2)) - self.winfo_rooty()

            if receiver is None:
                x1 = event.x_root
                y1 = event.y_root
                print(x1, y1)
            else:
                x1 = (receiver.winfo_rootx() + (receiver.winfo_width() // 2)) - self.winfo_rootx()
                y1 = (receiver.winfo_rooty() + (receiver.winfo_height() // 2)) - self.winfo_rooty()

            line_id = self.create_line(x0, y0, x1, y1, width=3, fill="red")
            self.connecting_line_ids.append(line_id)
