from abc import ABC, abstractmethod

class TrainBase(ABC):

    @abstractmethod
    def add_train(self):
        pass

    @abstractmethod
    def show_database(self):
        pass

    @abstractmethod
    def update_train(self):
        pass

    @abstractmethod
    def delete_train(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def check_ticket_availablity(self):
        pass

    @abstractmethod
    def search_train(self):
        pass

    @abstractmethod
    def check_train_number(self, train_number):
        pass

    @abstractmethod
    def check_date(self, date):
        pass

    @abstractmethod
    def get_source(self, train_number):
        pass

    @abstractmethod
    def get_destination(self, train_number):
        pass

    @abstractmethod
    def get_train_name(self, train_number):
        pass

