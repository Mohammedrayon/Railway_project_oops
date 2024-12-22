from passenger import Passenger

class IRCTC():
    def __init__(self):
        print("\nWelcome to IRCTC")
        self.passenger = Passenger()
        self.passenger.show_initial_menu()

if __name__ == '__main__':
    obj = IRCTC()