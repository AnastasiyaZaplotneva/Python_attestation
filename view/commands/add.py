
from .abstract import Command


class CommandAdd(Command):


    def description(self):
        return "Добавить заметку"

    def execute(self):
        self.console.add_note()