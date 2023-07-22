

from .add import CommandAdd
from .change import CommandChange
from .exit import CommandExit
from .open import CommandOpen
from .remove import CommandRemove
from .save import CommandSave
from .show_all import CommandShowAll


class Menu:
    """
        Данный класс создает основное меню и реализует запуск методов
        Методы:
            1. __init__: конструктор класса для создания меню.
            2. __str__: возвращает строковое представление меню.
            3. get_size_menu: возвращает длину списка меню.
            4. execute: Запускает метод в зависимости от выбора пользователя по индексу команды в списке.
            5. change: изменение заметки.
    """

    def __init__(self, console):
        self.commands = []
        self.commands.append(CommandOpen(console))
        self.commands.append(CommandShowAll(console))
        self.commands.append(CommandAdd(console))
        self.commands.append(CommandChange(console))
        self.commands.append(CommandRemove(console))
        self.commands.append(CommandSave(console))
        self.commands.append(CommandExit(console))

    def __str__(self):
        menu_string = "\n~~~~~~~ Главное меню ~~~~~~~\n"
        for i, cmd in enumerate(self.commands, start=1):
            menu_string += f"\t{i}. {cmd.description()}\n"
        return menu_string

    def get_size_menu(self):
        return len(self.commands)

    def execute(self, index: int):
        option = self.commands[index]
        option.execute()