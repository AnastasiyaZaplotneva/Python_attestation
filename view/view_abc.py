from abc import ABC, abstractmethod


class View(ABC):
 
  
    @abstractmethod
    def set_presenter(self, presenter):
        ...

    @abstractmethod
    def start(self):
        ...