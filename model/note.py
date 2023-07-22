
from datetime import datetime


class Note:

  
    def __init__(self, title="заголовок", content="заметка",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.title = title
        self.content = content
        self.date = date

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_date(self):
        return self.date

    def change_note(self, new_title: str, new_content: str):
        if new_title:
            self.title = new_title
        if new_content:
            self.content = new_content
        self.date = datetime.today().strftime('%d.%m.%Y %H:%M')