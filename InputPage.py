from tkinter import *
import OperatePage


class InputOutputPage(object):
    def __init__(self, master=None, privilege=None, user=None):
        self.root = master
        self.root.geometry('400x500+200+100')
        self.privilege = privilege
        self.page = None
        self.user = user
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)
        self.page.pack()

    def check_button_id(self, id):
        if id == 0:
            tid = StringVar()
            Label(self.page, text="Transaction ID").pack()
            Entry(self.page, textvariable=tid).pack()
            cid = StringVar()
            Label(self.page, text="customer ID").pack()
            Entry(self.page, textvariable=cid).pack()
            pp = StringVar()
            Label(self.page, text="product purchased").pack()
            Entry(self.page, textvariable=pp).pack()
            Button(self.page, text="Submit", command=lambda: self.register_sale(tid=tid, cid=cid, pp=pp)).pack()

        elif id == 1:
            fn = StringVar()
            Label(self.page, text="First Name").pack()
            Entry(self.page, textvariable=fn).pack()
            ln = StringVar()
            Label(self.page, text="Last Name").pack()
            Entry(self.page, textvariable=ln).pack()
            cid = StringVar()
            Label(self.page, text="Customer ID").pack()
            Entry(self.page, textvariable=cid).pack()
            add = StringVar()
            Label(self.page, text="Address").pack()
            Entry(self.page, textvariable=add).pack()
            ltep = StringVar()
            Label(self.page, text="Lifetime earned points").pack()
            Entry(self.page, textvariable=ltep).pack()
            ap = StringVar()
            Label(self.page, text="available point").pack()
            Entry(self.page, textvariable=ap).pack()
            Button(self.page, text="Submit", command=lambda: self.create_new_customer(fn=fn, ln=ln, add=add, ltep=ltep,
                                                                                      ap=ap, cid=cid)).pack()
        elif id == 2:
            pid = StringVar()
            Label(self.page, text="product ID").pack()
            Entry(self.page, textvariable=pid).pack()
            Button(self.page, text="Submit", command=lambda: self.show_product_info(id=id)).pack()
        elif id == 3:
            fn = StringVar()
            Label(self.page, text="First Name").pack()
            Entry(self.page, textvariable=fn).pack()
            ln = StringVar()
            Label(self.page, text="Last Name").pack()
            Entry(self.page, textvariable=ln).pack()
            uid = StringVar()
            Label(self.page, text="User ID").pack()
            Entry(self.page, textvariable=uid).pack()
            pl = StringVar()
            Label(self.page, text="Privilege").pack()
            Entry(self.page, textvariable=pl).pack()
            Button(self.page, text="Submit", command=lambda: self.create_new_employee(fn=fn, ln=ln, uid=uid, pl=pl)).pack()
        Button(self.page, text="return to last page", command=self.return_to_last).pack()

    def show_product_info(self, id):
        rows = self.user.check_report(id=id)
        for row in rows:
            Label(self.page, text="{}".format(row)).pack()

    def return_to_last(self):
        self.page.destroy()
        OperatePage.OperatePage(master=self.root, user=self.user)

    def register_sale(self, tid, cid, pp):
        reward = self.user.register_sale(tid=tid, cid=cid, pp=pp)
        print(reward)
        if reward == 1:
            Label(self.page, text="Get a reward").pack()
        elif reward == 2:
            Label(self.page, text="Don't have enough points").pack()
        elif reward == 3:
            Label(self.page, text="Don't have this product anymore").pack()

    def create_new_employee(self, fn, ln, uid, pl):
        success = self.user.create_new_employee(fn=fn, ln=ln, uid=uid, pl=pl)
        if success == 1:
            top = Toplevel()
            top.title('Error')
            msg = Message(top, text="Can't create new user. The ID has already existed", width=150)
            msg.pack()

    def create_new_customer(self, fn, ln, add, ltep, ap, cid):
        success = self.user.create_new_customer(fn=fn, ln=ln, add=add, ltep=ltep, ap=ap, cid=cid)
        if success == 1:
            top = Toplevel()
            top.title('Error')
            msg = Message(top, text="Can't create new user. The ID has already existed", width=150)
            msg.pack()


