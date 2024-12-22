import sqlite3
import random
from train import Train
import datetime

class Ticket:
    def __init__(self):
        self.conn = sqlite3.connect("database/ticket.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ticket_book (
                Name TEXT,
                Age INTEGER,
                PNR_number TEXT PRIMARY KEY,
                Gender TEXT,
                Source TEXT,
                Destination TEXT,
                Quota TEXT,
                No_of_tickets INTEGER,
                Date TEXT,
                Train_name TEXT,
                Train_number INTEGER,
                Fare REAL
            )
        """)
        self.conn.commit()

    def show_ticketbase(self):
        print("Showing Database of Tickets")
        self.cursor.execute("SELECT * FROM ticket_book")
        print(self.cursor.fetchall())
        return

    def book_ticket(self):
        self.train = Train()
        self.train.search_train()
        print("\n1. Book a ticket \n2. Search Again")
        choice = input("Enter your choice: ")
        if choice == '2':
            self.train.search_train()
        elif choice == '1':
            self.name = input("Enter the name of the passenger: ")
            self.age = int(input("Enter the age of the passenger: "))
            self.gender = input("Enter the gender of the passenger (M/F/O): ")
            self.train_num = int(input("Enter the train number: "))
            if not self.train.check_train_number(self.train_num):
                return
            self.source = self.train.get_source(self.train_num)
            self.destination = self.train.get_destination(self.train_num)
            self.quota = input("Enter the quota (GK/CK): ")
            self.no_of_tickets = int(input("Enter the number of tickets: "))
            self.date = input("Enter the date of journey (YYYY-MM-DD): ")
            if not self.train.check_date(self.date):
                return
            self.pnr = self.generate_pnr()
            self.train_name = self.train.get_train_name(self.train_num)
            self.fare = self.ticket_fare(self.no_of_tickets)
            print("Ticket Fare is:", self.fare)
            try:
                self.cursor.execute("""
                    INSERT INTO ticket_book (Name, Age, PNR_number, Gender, Source, Destination, Quota, No_of_tickets, Date, Train_name, Train_number, Fare)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    self.name, self.age, self.pnr, self.gender, self.source, self.destination,
                    self.quota, self.no_of_tickets, self.date, self.train_name, self.train_num, self.fare
                ))
                self.conn.commit()
                print("Ticket booked successfully")
                self.show_ticketbase()
                self.print_ticket(self.pnr)
            except sqlite3.IntegrityError:
                print("Error: Duplicate PNR number. Please try again.")
        else:
            print("Invalid choice")
            self.book_ticket()
        return

    def generate_pnr(self):
        region_code = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])  # First digit
        remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])  # Remaining 9 digits
        return region_code + remaining_digits

    def ticket_fare(self, no_of_tickets):
        print("Calculating Ticket Fare")
        return 50.0 * no_of_tickets

    def print_ticket(self, pnr_number):
        self.cursor.execute("SELECT * FROM ticket_book WHERE PNR_number = ?", (pnr_number,))
        ticket = self.cursor.fetchone()
        print("\nTicket Details:")
        print(ticket)
        return
