from datetime import datetime
from .note import Note
from tabulate import tabulate


class Notebook:
   
   
    def __init__(self):
        self.notes = []

    def size(self):
        return len(self.notes)

    def add_note(self, title: str, content: str):
        note = Note(title, content, datetime.today().strftime('%d.%m.%Y %H:%M'))
        self.notes.append(note)

    def remove_note(self, index: int):
        del self.notes[index]

    def change_note(self, index: int, title: str, content: str):
        self.notes[index].change_note(title, content)

    def is_full(self):
        return bool(self.notes)

    def get_notes(self):
        return self.notes

    @property
    def tabl(self):
        headers = ['№', 'Заголовок', 'Заметка', 'Дата создания/изменения']
        tabl = [[i,
                 note.get_title(),
                 note.get_content(),
                 note.get_date()]
                for i, note in enumerate(self.notes, start=1)]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')