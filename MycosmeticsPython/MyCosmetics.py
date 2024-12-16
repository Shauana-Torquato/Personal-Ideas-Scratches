#Personal System to Manage my Cosmetics and SelfCare Routines

import sqlite3;
import tkinter as tk;
from tkinter import ttk;

#Conection to the Database and creation of the same in case it doesn't exist

conn = sqlite3.connect("my_cosmetics_py.db")
cursor = conn.cursor()

#Creation of the table to register the products

cursor.execute('''CREATE TABLE IF NOT EXISTS my_cosmetics_py
               (itemId INTEGER PRIMARY KEY AUTOINCREMENT,
               routineId TEXT,
               activeIngredient TEXT,
               brand TEXT,
               purchasingDate INTEGER,
               cost REAL,
               amount INTEGER,
               description TEXT,
               rate REAL)''')
conn.commit()

#Interation functions with the database

def show my_cosmetics_py(): 
    list_cosmetics.delete(0, tk.END)
    cursor.execute("SELECT * FROM my_cosmetics_py")
    rows = cursor.fetchall()
    for row in rows:
        list_cosmetics.insert(tk.END, row)

#main window

conn.close()

