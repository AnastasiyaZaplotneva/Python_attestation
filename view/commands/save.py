
from .abstract import Command


class CommandSave(Command):
    

    def description(self):
        return "Сохранить изменения"

    def execute(self):
        self.console.save_changes()