from kivymd.app import MDApp
from kivy.lang import Builder
import sqlite3


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGrey"
        # create database or connect
        conn = sqlite3.connect('first_db.db')
        # Create a curso()
        c = conn.cursor()
        #create a table
        c.execute("""CREATE TABLE if not exists customers(
        name text)
        """)
        # Commit our changes
        conn.commit()
        # close our connection

        conn.close()




        return Builder.load_file('first_db.kv')

    def submit (self):
        conn = sqlite3.connect('first_db.db')
        # Create a curso()
        c = conn.cursor()

        #Add a record

        c.execute("INSERT INTO customers VALUES (:first)",
                  {
                      'first': self.root.ids.word_input.text,
                  })
        # Add a little message
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

        # clear the input box
        self.root.ids.word_input.text = ''

        # Commit our changes
        conn.commit()
        # close our connection

        conn.close()
    def show_records(self):
        conn = sqlite3.connect('first_db.db')
        # Create a curso()
        c = conn.cursor()

        # Take records from database
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        word = ''
        #loop through records
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text= f'{word}'

        # Commit our changes
        conn.commit()
        # close our connection

        conn.close()




MainApp().run()