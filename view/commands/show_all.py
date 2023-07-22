
from .abstract import Command


class CommandShowAll(Command):
   

    def description(self):
        return "Показать все заметки"

    def execute(self):
        self.console.show_all()