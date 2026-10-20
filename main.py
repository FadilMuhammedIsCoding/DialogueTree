import tkinter
from frontend.containers.standard_node import StandardNode
from backend.data.parser import Parser
from frontend.screens.murder_map import MurderMap


class Manager:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Dialogue Tree")
        self.root.geometry("960x540")

        self.menu_bar = tkinter.Menu(self.root)
        self.root['menu'] = self.menu_bar

        self.change_menu = tkinter.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu=self.change_menu)

        self.change_menu.add_command(label="Save", command=self.save)

        self.collection = MurderMap(self.root)
        self.collection.pack(fill="both", expand=True)

        self.node = StandardNode(self.collection, 50, 50)
        self.collection.add_node(self.node)

    def save(self):
        Parser.convert_node_to_dictionary(self.node)

    def run(self):
        self.collection.draw_grid()
        self.root.mainloop()


if __name__ == "__main__":
    Manager().run()
