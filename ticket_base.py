from abc import ABC, abstractmethod

class TicketBase(ABC):

    @abstractmethod
    def book_ticket(self):
        pass
    
    @abstractmethod
    def show_ticketbase(self):
        pass

    @abstractmethod
    def generate_pnr(self):
        pass
    
    @abstractmethod
    def ticket_fare(self):
        pass


    @abstractmethod
    def print_ticket(self):
        pass