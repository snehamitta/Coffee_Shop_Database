from tkinter import *
import LoginPage
import Operater
import datetime
import InputPage


class OperatePage(object):
    def __init__(self, master=None, user=None):
        self.root = master
        self.root.geometry('400x500+200+100')
        self.logoutTime = datetime.datetime.now()
        self.loginTime = datetime.datetime.now()
        self.page = None
        self.user = user
        self.inputPage = None
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)
        self.page.pack()
        if self.user.privilege == 0:
            self.user.login(self.user.user_id)
            self.inputPage = InputPage.InputOutputPage(master=self.root, user=self.user)
            button1 = Button(self.page, text="Register a sale", command=lambda: self.check_button_id(0))
            button1['width'] = 300
            button1['height'] = 2
            button1.pack()
            button2 = Button(self.page, text="Create new customer", command=lambda: self.check_button_id(1))
            button2['width'] = 300
            button2['height'] = 2
            button2.pack()
        else:
            self.user.login(self.user.user_id)
            self.inputPage = InputPage.InputOutputPage(master=self.root, user=self.user)
            button1 = Button(self.page, text="Register a sale", command=lambda: self.check_button_id(0))
            button1['width'] = 300
            button1['height'] = 2
            button1.pack()
            button2 = Button(self.page, text="Create new customer", command=lambda: self.check_button_id(1))
            button2['width'] = 300
            button2['height'] = 2
            button2.pack()
            button3 = Button(self.page, text="Business report", command=lambda: self.check_button_id(2))
            button3['width'] = 300
            button3['height'] = 2
            button3.pack()
            button4 = Button(self.page, text="Create new employee", command=lambda: self.check_button_id(3))
            button4['width'] = 300
            button4['height'] = 2
            button4.pack()
        buttonLogOut = Button(self.page, text="Logout", command=self.back_to_login)
        buttonLogOut.pack()

    def back_to_login(self):
        self.page.destroy()
        self.user.logout()
        LoginPage.LoginPage(self.root)

    def check_button_id(self, id):
        self.page.destroy()
        self.inputPage.check_button_id(id)


