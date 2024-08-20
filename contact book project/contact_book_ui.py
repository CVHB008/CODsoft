import tkinter as tk
from tkinter import messagebox as mb


def load_gui(root):
        #self.root = root
        root.title('Contact Book')
        root.geometry('500x300')
        fonts = ('Helvetica 11')
        #print('initialization success')

        first_name = tk.Label(root, text='First name  ', font=fonts)
        first_entry = tk.Entry(root, width=24, font=fonts)
        first_name.place(x=20, y=10)
        first_entry.place(x=20, y=30)

        last_name = tk.Label(root, text='Last name  ', font=fonts)
        last_entry = tk.Entry(root, width=24, font=fonts)
        last_name.place(x=20, y=60)
        last_entry.place(x=20, y=80)

        phone = tk.Label(root, text='Phone number  ', font=fonts)
        phone_entry = tk.Entry(root, width=24, font=fonts)
        phone.place(x=20, y=110)
        phone_entry.place(x=20, y=130)

        email = tk.Label(root, text='Email  ', font=fonts)
        email_entry = tk.Entry(root, width=24, font=fonts)
        email.place(x=20, y=160)
        email_entry.place(x=20, y=180)

        address = tk.Label(root, text='Address ', font=fonts)
        address_entry = tk.Entry(root, width=24, font=fonts)
        address.place(x=20, y=210)
        address_entry.place(x=20, y=230)

        button_add = tk.Button(root,text='Add',font=fonts,padx=5, bg='#dcdcdc', relief='groove')
        button_add.place(x=20, y=260)

        label_contact = tk.Label(root,text='Contact list', font=fonts)
        label_contact.place(x=270, y=10)
        
        contact_list = tk.Listbox(root, height=12, width=24, font=fonts)
        contact_list.place(x=270, y=30)

        
        

