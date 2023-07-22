
from .abstract import Command


class CommandOpen(Command):
   

    def description(self):
        return "Открыть записную книжку"

    def execute(self):
        self.console.open_notebook()