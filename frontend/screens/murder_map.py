from tkinter import Canvas, Menu
from frontend.screens.collection import Collection
from frontend.containers.standard_node import StandardNode


class MurderMap(Collection):
    def __init__(self, master):
        super().__init__(master=master)
        self.nodes = {}
        self.connecting_line_ids = {}

        self.context_menu = Menu(self, tearoff=False)
        self.bind("<ButtonPress-3>", self.show_context_menu)

        self.grid_canvas = Canvas(self, state="disabled")

        self.context_menu.add_command(label="Make New Node", command=self.make_new_node)

    def add_node(self, node):
        self.number_of_nodes += 1
        node.identifier = str(self.number_of_nodes)

        self.nodes[node.identifier] = node
        self.connecting_line_ids[node.identifier] = []

        node.bind("<<Moving>>", self.draw_moved_connector_lines)
        node.bind("<<SearchingForNode>>", self.draw_searching_lines)
        node.bind("<<SearchingSuccessful>>", self.draw_moved_connector_lines)
        node.bind("<<SearchingAborted>>", self.clear_node_lines)

    def make_new_node(self):
        new_node = StandardNode(self, x=self.last_right_click_x, y=self.last_right_click_y,)
        self.add_node(new_node)

    def show_context_menu(self, event):
        self.last_right_click_x = event.x
        self.last_right_click_y = event.y
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)

    def clear_lines(self, node_identifier):
        for line_id in self.connecting_line_ids[node_identifier]:
            self.delete(line_id)

        self.connecting_line_ids[node_identifier].clear()

    def clear_node_lines(self, event):
        current_identifier = event.widget.identifier
        self.clear_lines(current_identifier)

    def draw_connector_lines(self, widget):
        current_identifier = widget.identifier
        current_connector = widget.get_connector()
        self.clear_lines(current_identifier)

        if current_connector is None: return

        sender = current_connector.get_local_connection_sender()
        receiver = current_connector.get_currently_connected_connection_receiver()

        if receiver is None: return

        x0 = (sender.winfo_rootx() + (sender.winfo_width() // 2)) - self.winfo_rootx()
        y0 = (sender.winfo_rooty() + (sender.winfo_height() // 2)) - self.winfo_rooty()
        x1 = (receiver.winfo_rootx() + (receiver.winfo_width() // 2)) - self.winfo_rootx()
        y1 = (receiver.winfo_rooty() + (receiver.winfo_height() // 2)) - self.winfo_rooty()

        line_id = self.create_line(x0, y0, x1, y1, width=3, fill="red")
        self.connecting_line_ids[current_identifier].append(line_id)

    def draw_moved_connector_lines(self, event):
        current_widget = event.widget
        self.draw_connector_lines(current_widget)

        current_connector_connection_sender = current_widget.get_connector().get_currently_connected_connection_sender()
        if current_connector_connection_sender is not None:
            self.draw_connector_lines(current_connector_connection_sender.master.master)

    def draw_searching_lines(self, event):
        current_identifier = event.widget.identifier
        current_connector = event.widget.get_connector()
        self.clear_lines(current_identifier)

        if current_connector is None: return

        sender = current_connector.get_local_connection_sender()

        x0 = (sender.winfo_rootx() + (sender.winfo_width() // 2)) - self.winfo_rootx()
        y0 = (sender.winfo_rooty() + (sender.winfo_height() // 2)) - self.winfo_rooty()
        x1 = event.x - self.winfo_rootx()
        y1 = event.y - self.winfo_rooty()

        line_id = self.create_line(x0, y0, x1, y1, width=3, fill="red")
        self.connecting_line_ids[current_identifier].append(line_id)
