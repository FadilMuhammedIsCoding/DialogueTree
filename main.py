import tkinter
from frontend.containers.standard_node import StandardNode


class Manager:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Dialogue Tree")
        self.root.geometry("960x540")

        self.node = StandardNode(self.root, 50, 50)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Manager().run()
