import tkinter
from frontend.containers.standard_node import StandardNode
from backend.data.node_parser import NodeParser


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

        self.node = StandardNode(self.root, 50, 50)

    def save(self):
        NodeParser.convert_node_to_dictionary(self.node)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Manager().run()
