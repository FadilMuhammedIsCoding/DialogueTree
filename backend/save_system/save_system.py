import json


class SaveSystem:
    def __init__(self):
        self.current_file_path = "C:/godot projects/heaven/dialogues/interviewer_1.json"

    def get_file_data(self):
        with open(self.current_file_path, 'r') as file:
            data = json.load(file)

        file.close()
        return data

    def set_file_data(self, dictionary):
        with open(self.current_file_path, 'w') as file:
            json.dump(dictionary, file)

        file.close()
