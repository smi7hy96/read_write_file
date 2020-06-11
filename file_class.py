class FileFunction:
    def __init__(self, file_name):
        if self.test_file(file_name):
            self.__file_name = file_name

    def test_file(self, file_name):
        try:
             with self.__open_file('r', file_name) as file:
                return True
        except IOError:
            print("File does not exist")
            return False

    def get_file_name(self):
        return self.__file_name

    def set_file_name(self, file_name):
        if self.test_file(file_name):
            self.__file_name = file_name
            return True
        else:
            return False

    def __open_file(self, command, file_name=None):
        if file_name is None:
            return open(self.__file_name, f'{command}')
        else:
            return open(file_name, f'{command}')

    def read_file(self):
        with self.__open_file('r') as file:
            lines = file.readlines()
            temp_list = [line.rstrip('\n') for line in lines]
        return temp_list

    def print_file(self):
        with self.__open_file('r') as file:
            data = file.read()
        return data

    def add_to_file(self, name):
        with self.__open_file('a') as file:
            file.write(f'\n{name}')