from abc import ABC, abstractmethod

class IRCTCBase(ABC):
    @abstractmethod
    def login(self):
        pass
    
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def book_ticket(self):
        pass
    
    @abstractmethod
    def check_pnr_status(self):
        pass
    
    @abstractmethod
    def print_ticket(self):
        pass
    
    @abstractmethod
    def cancel_ticket(self):
        pass
