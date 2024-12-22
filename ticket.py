import sqlite3
import random
from train import Train
import requests
import os
from ticket_base import TicketBase

class Ticket(TicketBase):
    def __init__(self):
        self.conn = sqlite3.connect("ticket.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ticket_book 
                            ( Name TEXT, Age INTEGER,
                            PNR_number INTEGER PRIMARY KEY ,
                            Gender TEXT, 
                            Source TEXT, Destination TEXT, 
                            Quota TEXT,No_of_tickets INTEGER ,Date TEXT, 
                            Train_name TEXT, Train_number INTEGER, Fare DOUBLE)""")
        self.conn.commit()

    def show_ticketbase(self):
        print("Showing Database of Tickets")
        self.cursor.execute("SELECT * FROM ticket_book")
        print(self.cursor.fetchall()) 
        return
     

    def book_ticket(self):
        self.train = Train()
        self.train.search_train()
        print("\n1.Book a ticket \n2.search Again")
        choice = input("Enter your choice:")
        if choice == '2':
            self.train.search_train()
        elif choice == '1':    
            self.name = input("Enter the name of the passenger:")
            self.age = input("Enter the age of the passenger:")
            self.gender = input("Enter the gender of the passenger(M/F/O):")
            self.train_num = input("Enter the train number:")
            if not self.train.check_train_number(self.train_num):
                return
            self.source = self.train.get_source(self.train_num)
            self.destination = self.train.get_destination(self.train_num)
            self.quota = input("Enter the quota(GK/CK):")
            self.no_of_tickets = input("Enter the number of tickets:")
            self.date = input("Enter the date of journey(yyyymmdd):")
            if not self.train.check_date(self.date):
                return
            self.pnr = self.generate_pnr()
            self.train_name = self.train.get_train_name(self.train_num)
            self.fare = self.ticket_fare()
            print("Ticket Fare is:", self.fare)
            self.cursor.execute("INSERT INTO ticket (Name , Age, PNR_number,gender Source, Destination, Quota , no_of_tickets ,Date ,train_name , train_no , fare ) VALUES (?, ?, ?)", (self.name, self.age, self.pnr, self.source, self.destination,self.quota,self.no_of_tickets, self.date))
            self.conn.commit()
            print("Ticket booked successfully")
            self.print_ticket()
        else:
            print("Invalid choice")
            self.book_ticket()
        return    

    def generate_pnr(self):
        region_code = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])  # First digit
        remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])  # Remaining 9 digits
        pnr_number = region_code + remaining_digits
        return pnr_number 

    def ticket_fare(self):
        print("Calculating Ticket Fare")
        api_key = os.environ.get('INDIAN_RAIL_API_KEY')
        url =f"""http://indianrailapi.com/api/v2/TrainFare/apikey/{api_key}/TrainNumber/{self.train_num}/From/{self.source}/To/{self.destination}/Quota/{self.quota}"""
        response = requests.get(url)
        data = response.json()
        print(data)
        return 50.0
    
    def print_ticket(self):
        pass

