import contact_book_functions as cbf
import contact_book_ui as cbui
import tkinter as tk


class contact_book:
    def __init__(self,root):
        self.root = root
        print('initialization success')
        cbui.load_gui(self.root)
        cbf.getter(self)
    

root = tk.Tk()
app = contact_book(root)

root.mainloop()
