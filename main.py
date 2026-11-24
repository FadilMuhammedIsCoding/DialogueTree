import tkinter
from frontend.containers.standard_node import StandardNode
from backend.data.parser import Parser
from backend.save_system.save_system import SaveSystem
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
        self.change_menu.add_command(label="Load", command=self.load)

        self.collection = MurderMap(self.root)
        self.collection.pack(fill="both", expand=True)

        self.save_system = SaveSystem()

    def save(self):
        final_dict = Parser.convert_collection_to_dictionary(self.collection.get_nodes())
        self.save_system.set_file_data(final_dict)

    def load(self):
        loaded_dict = self.save_system.get_file_data()
        self.collection.load_nodes_from_dictionary(loaded_dict)

    def run(self):
        self.collection.draw_grid()
        self.root.mainloop()


if __name__ == "__main__":
    Manager().run()
