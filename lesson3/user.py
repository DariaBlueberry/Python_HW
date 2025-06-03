class User:
    def __init__(self, last_name, first_name):
        self.last = last_name
        self.first = first_name

    def get_last_name(self):
        return self.last

    def get_first_name(self):
        return self.first

    def get_info(self):
        return f'Имя: {User.first_name}, Фамилия: {User.last_name}'
