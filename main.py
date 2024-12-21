import time
from passenger import Passenger

class IRCTC:
    def __init__(self):
        print("\nWelcome to IRCTC")
        time.sleep(1)
        self.passenger = Passenger()
        self.passenger.show_initial_menu()

if __name__ == '__main__':
    obj = IRCTC()