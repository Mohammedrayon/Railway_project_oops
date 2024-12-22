from train_base import TrainBase
import sqlite3
import pandas as pd
import datetime 

class Train(TrainBase):
    def __init__(self):
        # Initialize database
        self.conn = sqlite3.connect('database/train.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS train_info (
            Train_No INTEGER PRIMARY KEY,
            Train_Name TEXT,
            Source_Station TEXT,
            Destination_Station TEXT
        )
        ''')

        df = pd.read_csv('train_info.csv')
        df = df[['Train_No', 'Train_Name', 'Source_Station_Name', 'Destination_Station_Name']]
        df.columns = ['Train_No', 'Train_Name', 'Source_Station', 'Destination_Station']
        df.to_sql('train_info', self.conn, if_exists='replace', index=False)
        self.conn.commit()   
        return 


    def search_train(self):
        self.show_database()
        print("Search for a train")
        source = input("Enter the source:")
        self.cursor.execute("SELECT * FROM train_info WHERE Source_Station LIKE ?", ('%' + source + '%',))
        result = self.cursor.fetchall()
        if result:
            print("Train found")
            print(result)
        else:
            print("No trains found")  
        return        

    def show_database(self):
        print("\nShowing Database of Trains")
        self.cursor.execute("SELECT * FROM train_info")
        print(self.cursor.fetchall())
        return       
    
    def check_train_number(self, train_number):
        self.cursor.execute("SELECT * FROM train_info WHERE Train_No = ?", (train_number,))
        result = self.cursor.fetchone()
        if result:
            print(result)
            return True
        else:
            print("Train not found")
            return False
        
    def get_source(self, train_number):
        self.cursor.execute("SELECT Source_Station FROM train_info WHERE Train_No = ?", (train_number,))
        source = self.cursor.fetchone()
        return source[0]

    def get_destination(self, train_number):
        self.cursor.execute("SELECT Destination_Station FROM train_info WHERE Train_No = ?", (train_number,))
        destination = self.cursor.fetchone()
        return destination[0]    
        

    def check_date(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")
            return False
        
    def check_ticket_availablity(self):
        print("This feature is not available yet")
        pass    

    def update_train(self):
        pass

    def delete_train(self):
        pass

    def add_train(self):
        pass

    def get_train_name(self, train_number):
        self.cursor.execute("SELECT Train_Name FROM train_info WHERE Train_No = ?", (train_number,))
        train_name = self.cursor.fetchone()
        return train_name[0]