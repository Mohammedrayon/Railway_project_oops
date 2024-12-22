from abc import ABC, abstractmethod

class PassengerBase(ABC):
    #Ticket
    @abstractmethod
    def check_user(self):
        pass

    @abstractmethod
    def check_pnr_status(self):
        pass
    
    @abstractmethod
    def cancel_ticket(self):
        pass


