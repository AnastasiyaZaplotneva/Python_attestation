
from .abstract import Command


class CommandRemove(Command):


    def description(self):
        return "Удалить заметку"

    def execute(self):
        self.console.remove_note()