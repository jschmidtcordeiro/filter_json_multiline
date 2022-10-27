import json

class Parse():
    def __init__(self, line: str):
        if isinstance(line, str):
            self.__line = line
            self.__parsed_list = None
            self.__parsed_dict = {}
        else:
            print("ERR: File has not been read as a list")

    def get_parsed_list(self):
        return self.__parsed_list

    def get_parsed_dict(self):
        return self.__parsed_dict

    def str_to_list(self):
        try:
            self.__parsed_list = json.loads(self.__line)
            return self.__parsed_list
        except:
            print("ERR: Erro na")

    def list_to_dict(self):
        for j in self.__parsed_list:
            self.__parsed_dict.update(j)

