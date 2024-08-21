import tkinter as tk
import contact_book_functions as func
import contact_book_ui as cbui


class contact_book:
    def __init__(self):
        self.contacts_id = []
        self.root = root
        print('initialization success')
        cbui.load_gui(self, self.root)
        func.create_table()
        func.load_contactlist(self)
        print(self.contacts_id)


root = tk.Tk()
app = contact_book()
root.mainloop()
