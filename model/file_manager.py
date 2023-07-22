
import csv

from .note import Note
from .notebook import Notebook


class FileManager:
   
  

    def __init__(self, path: str):
        self.path = path

    def file_read(self, notebook: Notebook):
        try:
            with open(self.path, 'r', encoding='1251') as data:
                reader = csv.reader(data, delimiter=';')
                for i, note_list in enumerate(reader):
                    if i:
                        notebook.get_notes().append(Note(note_list[1], note_list[2], note_list[3]))
        except FileNotFoundError:
            pass
        return notebook

    def file_write(self, notebook: Notebook):
        with open(self.path, 'w', encoding='1251', newline='') as data:
            writer = csv.writer(data, delimiter=';')
            writer.writerow(['№', 'Заголовок', 'Заметка', 'Дата создания/изменения'])
            for i, note in enumerate(notebook.get_notes(), start=1):
                writer.writerow([i, note.get_title(), note.get_content(),
                                 note.get_date()])