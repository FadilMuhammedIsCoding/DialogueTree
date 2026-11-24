from tkinter import Canvas, Menu
from frontend.screens.collection import Collection
from frontend.containers.standard_node import StandardNode
from frontend.containers.node import Node
from frontend.fields.connector_subnodes.connection_sender import ConnectionSender


class MurderMap(Collection):
    def __init__(self, master):
        super().__init__(master=master)
        self.nodes = []
        self.connecting_line_ids = []

        self.current_line_id = None

        self.context_menu = Menu(self, tearoff=False)
        self.bind("<ButtonPress-3>", self.show_context_menu)

        self.grid_canvas = Canvas(self, state="disabled")

        self.context_menu.add_command(label="Make New Node", command=self.make_new_node)

    def show_context_menu(self, event):
        self.last_right_click_x = event.x
        self.last_right_click_y = event.y
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)

    def make_new_node(self):
        new_node = StandardNode(self, x=self.last_right_click_x, y=self.last_right_click_y,)
        self.number_of_nodes += 1
        new_node.set_name(str(self.number_of_nodes))
        self.add_node(new_node)

    def add_node(self, node):
        node.bind("<<Moving>>", self.draw_connecting_lines)
        node.bind("<<ConnectionSenderAdded>>", self.on_node_connection_sender_added)

    def get_nodes(self):
        nodes_array = []

        for child in self.winfo_children():
            if not isinstance(child, Node): continue

            nodes_array.append(child)

        return nodes_array

    def load_nodes_from_dictionary(self, dictionary):
        for child in self.winfo_children():
            if isinstance(child, Node):
                child.destroy()

        for key in dictionary:
            position = dictionary[key]["position"]
            new_node = StandardNode(self, x=position[0], y=position[1])
            new_node.set_name(key)
            self.add_node(new_node)

    def on_node_connection_sender_added(self, event):
        node = event.widget
        connection_senders = self.get_node_connection_senders(node)
        for connection_sender in connection_senders:
            connection_sender.bind("<<Searching>>", self.draw_searching_line)
            connection_sender.bind("<<SearchEnded>>", self.draw_connecting_lines)

    def get_node_connection_senders(self, widget):
        connection_senders = []

        for child in widget.winfo_children():
            if type(child) is ConnectionSender:
                connection_senders.append(child)

        return connection_senders

    def move_motion(self, event):
        dx = event.x - self.global_initial_x
        dy = event.y - self.global_initial_y

        for node in self.winfo_children():
            if type(node) is not StandardNode: continue
            node.x += dx
            node.y += dy
            node.place(x=node.x, y=node.y)

        self.draw_connecting_lines(None)

        self.global_initial_x = event.x
        self.global_initial_y = event.y

    def clear_all_lines(self):
        for line_id in self.connecting_line_ids:
            self.delete(line_id)

        self.connecting_line_ids.clear()

    def draw_searching_line(self, event):
        self.delete(self.current_line_id)
        connection_sender = event.widget

        x0, y0 = connection_sender.get_connecting_position()
        x0, y0 = x0 - self.winfo_rootx(), y0 - self.winfo_rooty()
        x1, y1 = event.x - self.winfo_rootx(), event.y - self.winfo_rooty()

        self.current_line_id = self.create_line(x0, y0, x1, y1, width=3, fill="red")

    def draw_connecting_line(self, connection_sender):
        self.delete(self.current_line_id)

        x0, y0 = connection_sender.get_connecting_position()
        x0, y0 = x0 - self.winfo_rootx(), y0 - self.winfo_rooty()

        connected_node = connection_sender.current_connected_node
        if connected_node is None: return

        x1, y1 = connected_node.get_connecting_position()
        x1, y1 = x1 - self.winfo_rootx(), y1 - self.winfo_rooty()

        line_id = self.create_line(x0, y0, x1, y1, width=3, fill="red")
        self.connecting_line_ids.append(line_id)

    def draw_connecting_lines(self, event):
        self.clear_all_lines()

        for node in self.winfo_children():
            connection_senders = self.get_node_connection_senders(node)
            if len(connection_senders) == 0: continue
            for connection_sender in connection_senders: self.draw_connecting_line(connection_sender)
