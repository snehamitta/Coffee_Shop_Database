from tkinter import *
import psycopg2
import OperatePage
import Operater


class LoginPage(object):

    def __init__(self, master=None):
        self.root = master
        self.root.geometry('400x500+200+100')
        self.entryInput = StringVar()
        self.page = None
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page, text='Please enter user ID').pack()
        Entry(self.page, textvariable=self.entryInput).pack()
        Button(self.page, text='Login', command=self.login_check).pack()
        self.label2 = Label(self.page, text="LogIn fail, please try again!")

    def login_check(self):
        user_id = self.entryInput.get()
        conn = psycopg2.connect(database='postgres', user='postgres', password='zcy///', host='127.0.0.1',
                                port='5432')
        cur = conn.cursor()
        cur.execute("select * from user_table where userid = \'{}\';".format(user_id))
        rows = cur.fetchall()
        if len(rows) != 0 and rows[0][3] == 1:
            self.page.destroy()
            OperatePage.OperatePage(master=self.root, user=Operater.Manager(id=user_id, privilege=rows[0][3]))
        elif len(rows) != 0 and rows[0][3] == 0:
            self.page.destroy()
            OperatePage.OperatePage(master=self.root, user=Operater.Employee(id=user_id, privilege=rows[0][3]))
        elif len(rows) == 0:
            self.label2.forget()
            self.label2.pack()





