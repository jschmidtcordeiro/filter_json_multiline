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
        if self.__line[0] != "[" and self.__line[0] != "{":
            self.__line = self.remove_verbose(self.__line)

        try:
            self.__parsed_list = json.loads(self.__line)
            return self.__parsed_list
        except:
            print("ERR: Erro na")

    def remove_verbose(self, line: str):
        return "[" + line.split("[")[1]

    def list_to_dict(self):
        if self.__parsed_list == None:
            return
        for j in self.__parsed_list:
            self.__parsed_dict.update(j)

