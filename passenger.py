import sqlite3
from passenger_base import PassengerBase
from ticket import Ticket
from train import Train

class Passenger(PassengerBase):
    def __init__(self):
        # Initialize database
        self.conn = sqlite3.connect('database/passenger_login.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        self.logged_in_user = None

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS passenger (
            username TEXT PRIMARY KEY,
            password TEXT
        )
        """)
        self.conn.commit()

    def login(self):
        print("\nLogin to your account")
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.cursor.execute("SELECT * FROM passenger WHERE username = ? AND password = ?", 
                              (username, password))
            user = self.cursor.fetchone()
            if user:
                print(f"\nLogin successful! Welcome {username}.")
                self.logged_in_user = username
                self.show_main_menu()
                break
            else:
                print("Invalid username or password. Please try again.")

    def register(self):
        print("\nRegister for a new account")
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            try:
                self.cursor.execute("INSERT INTO passenger (username, password) VALUES (?, ?)", 
                                  (username, password))
                self.conn.commit()
                print("\nAccount created successfully!")
                self.logged_in_user = username
                self.show_main_menu()
                break
            except sqlite3.IntegrityError:
                print("Username already exists. Please try again.")

    def check_user(self):
        if not self.logged_in_user:
            print("Please login first!")
            return
        self.ticket = Ticket()
        self.ticket.book_ticket()

    def check_pnr_status(self):
        if not self.logged_in_user:
            print("Please login first!")
            return
        print("\nPNR status check functionality is not yet implemented.")

    def cancel_ticket(self):
        if not self.logged_in_user:
            print("Please login first!")
            return
        print("\nCancel ticket functionality is not yet implemented.")

    def show_initial_menu(self):
        while True:
            print("""
            === IRCTC Login System ===
            1. Login to your account
            2. Register for a new account
            3. Exit      
            """)
            choice = input("Enter your choice: ")
            if choice == '1':
                self.login()
                break
            elif choice == '2':
                self.register()
                break
            elif choice == '3':
                print("\nExiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            return    
    
    def show_main_menu(self):
        while True:
            print("""
            === IRCTC Main Menu ===
            1. Book Ticket
            2. Check PNR Status
            3. Check seat availability
            4. Cancel Ticket
            5. Exit
            """)
            choice = input("Enter your choice: ")
            if choice == '1':
                self.check_user()
            elif choice == '2':
                self.check_pnr_status()
            elif choice == '3':
                self.print_ticket()
            elif choice == '4':
                self.cancel_ticket()
            elif choice == '5':
                print("\nExiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")