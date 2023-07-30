# animal.py

class Animal:
    def __init__(self, name):
        self.name = name
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands


class Pet(Animal):
    pass


class PackAnimal(Animal):
    pass
