import json
from tkinter import *
from frontend.functionals.functional import Functional
from frontend.containers.node import Node
from frontend.fields.node_name import NodeName
from frontend.fields.text_field import TextField
from frontend.fields.connector import ConnectionSender


class Parser:
    """
    class that converts a given tkinter widget/widgets into a dictionary that represents it.
    """
    def __init__(self):
        pass

    @staticmethod
    def convert_node_to_dictionary(node):
        final_dict = {
            "position": [node.x, node.y]
        }

        for field in node.fields:
            if type(field) is TextField:
                final_dict[field.get_id()] = field.get_data()

            if type(field) is ConnectionSender:
                final_dict["next"] = field.get_connector_name()

        return final_dict

    @staticmethod
    def convert_collection_to_dictionary(collection):
        main_dict = {}

        for child in collection:
            node_dict = Parser.convert_node_to_dictionary(child)
            main_dict[child.get_name()] = node_dict

        return main_dict
