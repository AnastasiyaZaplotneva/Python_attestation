

from model.file_manager import FileManager


class Presenter:
    


    def __init__(self, view, notebook, path: str):
        self.view = view
        self.notebook = notebook
        self.view.set_presenter(self)
        self.file = FileManager(path)

    def open_file(self):
        self.notebook = self.file.file_read(self.notebook)

    def save(self):
        self.file.file_write(self.notebook)

    def is_full(self):
        return self.notebook.is_full()

    def add_note(self, title_text: str, text_note: str):
        self.notebook.add_note(title_text, text_note)

    def remove_note(self, index: int):
        self.notebook.remove_note(index)

    def change_note(self, index: int, update_title: str, update_text: str):
        self.notebook.change_note(index, update_title, update_text)

    def get_size_notebook(self):
        return self.notebook.size()

    def get_tabl_notebook(self):
        return self.notebook.tabl