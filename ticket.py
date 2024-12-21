from main import IRCTC
import sqlite3

class Ticket(IRCTC):
    def book_ticket(self):
        print("Book a ticket")
        source = input("Enter the source:")
        destination = input("Enter the destination:")
        date = input("Enter the date of journey:")
        self.cursor.execute("INSERT INTO ticket (source, destination, date) VALUES (?, ?, ?)", (source, destination, date))
        self.conn.commit()
        print("Ticket booked successfully")