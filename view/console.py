
from .commands.menu import Menu
from .view_abc import View


class Console(View):
    
    working = False
    save = True
    open = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def open_notebook(self):
        if not self.open:
            self.presenter.open_file()
            self.open = True
            if self.presenter.is_full():
                print("\nЗаписная книжка открыта")
            else:
                print("\nВ записной книжке нет записей")
        else:
            print("\nЗаписная книжка уже открыта!")

    def show_all(self):
        if self.presenter.is_full():
            print("\n\t\t\t\t\t\t\t\t\tСПИСОК ВСЕХ ЗАМЕТОК",
                  self.presenter.get_tabl_notebook(), sep='\n')
        else:
            print("\nЗаписная книжка не открыта или пуста!")

    def remove_note(self):
        if self.presenter.is_full():
            index = self.get_index(self.presenter.get_size_notebook(),
                                     "\nВведите номер заметки: ")
            self.presenter.remove_note(index)
            self.save = False
            print("\nЗаметка удалена!\n")
        else:
            print("\nЗаписная книжка не открыта или пуста!")

    def change_note(self):
        if self.presenter.is_full():
            index = self.get_index(self.presenter.get_size_notebook(),
                                     "\nВведите номер заметки: ")
            update_title = input("\nОбновите заголовок заметки или нажмите ввод: ")
            update_note = input("\nОбновите заметку или нажмите ввод: ")
            self.presenter.change_note(index, update_title, update_note)
            self.save = False
            print("\nЗаметка изменена!\n")
        else:
            print("\nЗаписная книжка не открыта или пуста!")

    def add_note(self):
        new_title = input("\nВведите заголовок заметки: ")
        new_note = input("\nВведите заметку: ")
        self.presenter.add_note(new_title, new_note)
        print("\nЗаметка добавлена!\n")
        self.save = False

    def finish(self):
        if self.save:
            self.working = False
            print("\nЗавершение работы...")
            return

        answer = input("\nСохранить изменения (да/нет)? ").lower()

        if answer == 'да' and self.open:
            self.presenter.save()
            self.save = True
            print("\nИзменения сохранены")
        elif answer == 'да' and not self.open:
            print("\nВы не открыли вашу записную книжку. В случае сохранения все "
                  "предыдущие записи в ней будут удалены или переписаны.\n")
            answer_2 = input("Подтвердите сохранение (да/нет): ").lower()
            if answer_2 == 'да':
                self.presenter.save()
                self.save = True
                print("\nИзменения сохранены")
        self.working = False
        print("\nЗавершение работы...")

    def save_changes(self):
        if not self.__open:
            print("\nВы не открыли вашу записную книжку. В случае сохранения все "
                  "предыдущие записи в ней будут удалены или переписаны.\n")
            answer = input("Подтвердите сохранение (да/нет): ")
            if answer.lower() == 'да':
                self.presenter.save()
                self.save = True
                print("\nИзменения сохранены")
        else:
            self.presenter.save()
            self.save = True
            print("\nИзменения сохранены")

    def start(self):
        self.working = True
        menu = Menu(self)
        while self.working:
            print(menu)
            index = self.get_index(menu.get_size_menu(), "\nВыберите пункт меню: ")
            menu.execute(index)

    @staticmethod
    def get_index(size: int, text: str):
        
        while True:
            user_input = input(text)
            if (user_input.isdigit() and
                    1 <= int(user_input) <= size):
                index = int(user_input) - 1
                return index
            print(f"\nВведите число от 1 до {size}")