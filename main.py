from tkinter import *
from tkinter import messagebox
import ttkthemes
import tkinter as tk
from tkinter import ttk
import pymysql


def add_button():
    if nameEntry.get() == '' or emailEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        try:
            con = pymysql.Connect(host='localhost', user='root', password='EzrA')
            cur = con.cursor()
        except:
            messagebox.showerror('Error', 'connection Error')
            return

        try:
            query = 'create database crud'
            cur.execute(query)
            query = 'use crud'
            cur.execute(query)
            query = ('create table cruds(Id int auto_increment primary key not null,Name varchar(30),Email varchar(50),'
                     'Phone varchar(50), gender varchar(10) )')
            cur.execute(query)
        except:
            cur.execute('use crud')
            query = 'insert into cruds(Name,email,phone,gender) values(%s,%s,%s,%s)'
            cur.execute(query, (nameEntry.get(), emailEntry.get(), phoneEntry.get(), genderEntry.get()))
            con.commit()
            con.close()
            result = messagebox.askyesno('confirm', 'data added successfully, do you want to clear')
            if result:
                nameEntry.delete(0, END)
                emailEntry.delete(0, END)
                phoneEntry.delete(0, END)
                genderEntry.delete(0, END)
            else:
                pass
            query = 'select *from cruds'
            cur.execute(query)
            fetched_data = cur.fetchall()
            crud.delete(*crud.get_children())
            for data in fetched_data:
                dataList = list(data)
                crud.insert('', END, values=dataList)


window = tk.Tk()
window.geometry('650x700')

root = Frame(window, width=30)
root.place(x=0, y=0)

titleLabel = Label(root, text='CRUD OPERATION', bg='gray20', fg='gold', font=('arial', 12, 'bold'))
titleLabel.grid(row=0, column=1, pady=20)

nameLabel = Label(root, text='Name', bg='gray20', fg='gold', font=('arial', 12, 'bold'), width=12)
nameLabel.grid(row=1, column=0, padx=15, pady=10)
nameEntry = Entry(root, width=20, font=('arial', 12, 'bold'))
nameEntry.grid(row=1, column=1, padx=15, pady=10)

emailLabel = Label(root, text='Email', bg='gray20', fg='gold', font=('arial', 12, 'bold'), width=12)
emailLabel.grid(row=2, column=0, padx=15, pady=10)
emailEntry = Entry(root, width=20, font=('arial', 12, 'bold'))
emailEntry.grid(row=2, column=1, padx=15, pady=10)

phoneLabel = Label(root, text='Phone number', bg='gray20', fg='gold', font=('arial', 12, 'bold'), width=12)
phoneLabel.grid(row=3, column=0, padx=15, pady=10)
phoneEntry = Entry(root, width=20, font=('arial', 12, 'bold'))
phoneEntry.grid(row=3, column=1, padx=15, pady=10)

genderLabel = Label(root, text='Gender', bg='gray20', fg='gold', font=('arial', 12, 'bold'), width=12)
genderLabel.grid(row=4, column=0, padx=15, pady=10)
genderEntry = Entry(root, width=20, font=('arial', 12, 'bold'))
genderEntry.grid(row=4, column=1, padx=15, pady=10)

insertButton = Button(root, text='Insert', bg='blue', font=('arial', 12, 'bold'), width=10, command=add_button)
insertButton.grid(row=1, column=2, pady=15)

updateButton = Button(root, text='Update', bg='blue', font=('arial', 12, 'bold'), width=10)
updateButton.grid(row=2, column=2, pady=15)

deleteButton = Button(root, text='Delete', bg='blue', font=('arial', 12, 'bold'), width=10)
deleteButton.grid(row=3, column=2, pady=15)

resetButton = Button(root, text='Reset', bg='blue', font=('arial', 12, 'bold'), width=10)
resetButton.grid(row=4, column=2, pady=15)

sendButton = Button(root, text='Send', bg='blue', font=('arial', 12, 'bold'), width=10)
sendButton.grid(row=5, column=2, pady=15)

dataFrame = Frame(window)
dataFrame.place(x=10, y=400, width=590)

scrollbarX = Scrollbar(dataFrame, orient=HORIZONTAL)
scrollbarY = Scrollbar(dataFrame, orient=VERTICAL)

crud = ttk.Treeview(dataFrame, columns=('Id', 'Name', 'email', 'phone', 'gender'), xscrollcommand=scrollbarX.set,
                    yscrollcommand=scrollbarY.set)

scrollbarX.config(command=crud.xview)
scrollbarY.config(command=crud.yview)

scrollbarX.pack(side=BOTTOM, fill=X)
scrollbarY.pack(side=RIGHT, fill=Y)

crud.pack(fill=BOTH)

crud.config(show='headings')

crud.heading('Id', text='Id')
crud.heading('Name', text='Name')
crud.heading('email', text='Email')
crud.heading('phone', text='Phone Number')
crud.heading('gender', text='Gender')

root.mainloop()
