import json
from tkinter import *
from frontend.functionals.functional import Functional
from frontend.containers.node import Node
from frontend.fields.node_name import NodeName
from frontend.fields.text_field import TextField


class NodeParser:
    """
    class that converts a given tkinter node into a dictionary.
    """
    def __init__(self):
        pass

    @staticmethod
    def convert_node_to_dictionary(node: Node):
        final_dict = {}

        for field in node.fields:
            if type(field) is NodeName:
                final_dict["name"] = field.get_text()

            if type(field) is TextField:
                final_dict[field.get_id()] = field.get_data()

        print(final_dict)
