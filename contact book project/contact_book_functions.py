#functions defined in one module
import sqlite3 as sq
import contact_book_ui as cbui
from tkinter import messagebox as mb


def db_conn():
    conn = sq.connect('Contactbook.db')
    return conn


def create_db():
    conn = db_conn()
    cur = conn.cursor()
    sql_query='''CREATE TABLE IF NOT EXISTS Contact_book (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                f_name TEXT,
                l_name TEXT,
                phone TEXT,
                email TEXT,
                address TEXT)'''
    cur.execute(sql_query)
    conn.commit()


def database(self):
    self.first_name = self.first_entry.get()
    self.last_name = self.last_entry.get()
    self.phone_numbe = self.phone_entry.get()
    self.email_name = self.email_entry.get()
    self.address_name = self.address_entry.get()
    #self.listbox = self.contact_list

    conn = sq.connect('contact_book.db')
    cur = conn.cursor()

    conn.commit()
    conn.close()


def add_person(app):
    # return if first name or last name empty
    # TODO: add alert to notify first, last name required
    if app.first_name.get() == "" or app.last_name.get() == "":
        mb.showwarning('Warning', 'First, Last name are required')

    # put input fields into tuple
    insert_row = (app.first_entry.get(), app.last_name.get(),app.phone_entry.get(),
                   app.email_entry.get(), app.address_entry.get())
    conn = db_conn()
    with conn:
        cur = conn.cursor()
        sql_query = "INSERT INTO tbl_contactlist (col_fname, col_lname, col_email, col_phone, col_address)"\
                    "VALUES (?, ?, ?, ?, ?)"
        cur.execute(sql_query, insert_row)
        conn.commit()
    conn.close()
    clear_form_fields(app)
    load_contactlist(app)