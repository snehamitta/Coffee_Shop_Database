import psycopg2
import datetime
import time
import OperatePage


class Employee:
    def __init__(self, id, privilege):
        self.conn = psycopg2.connect(database='postgres', user='postgres', password='zcy///', host='127.0.0.1',
                                     port='5432')
        self.user_id = id
        self.privilege = privilege
        self.loginTime = None
        self.logoutTime = None

    def login(self, user_id):
        self.user_id = user_id
        self.loginTime = datetime.datetime.now()

    def logout(self):
        self.logoutTime = datetime.datetime.now()
        cur = self.conn.cursor()
        cur.execute("Insert into session_table values (\'{}\',"
                    "\'{}\'::timestamp without time zone, "
                    "\'{}\'::timestamp without time zone)".format(self.user_id, self.loginTime, self.logoutTime))
        self.conn.commit()

    def register_sale(self, tid, cid, pp):
        cur = self.conn.cursor()
        cur.execute("select price, countofitme from product_table where productid=\'{}\';".format(pp.get()))
        rows = cur.fetchall()
        price = rows[0][0]
        quality = rows[0][1]
        if quality > 0:
            cur.execute("Insert into transaction_table values (\'{}\',\'{}\',\'{}\');".format(tid.get(),
                                                                                               cid.get(),
                                                                                               pp.get()))
            self.conn.commit()
            cur.execute("update product_table set countofitme = countofitme - 1 where productid=\'{}\';".format(pp.get()))
            self.conn.commit()
            cur.execute(
                "update customer_table set lifetimeearnedpoints = lifetimeearnedpoints + {} where customerid=\'{}\';".format(
                    price, cid.get()))
            self.conn.commit()
            cur.execute(
                "update customer_table set availablepoint = availablepoint + {} where customerid=\'{}\';".format(
                    price, cid.get()))
            self.conn.commit()
            cur.execute("select availablepoint from customer_table where customerid=\'{}\';".format(cid.get()))
            row = cur.fetchall()[0][0]
            if row >= 25:
                return 1
            else:
                return 2
        else:
            return 3

    def create_new_customer(self, fn, ln, add, cid, ltep, ap):
        cur = self.conn.cursor()
        try:
            cur.execute("Insert into customer_table values (\'{}\',\'{}\',\'{}\',\'{}\', {},{});".format(fn.get(),
                                                                                                         ln.get(),
                                                                                                         add.get(),
                                                                                                         cid.get(),
                                                                                                         ltep.get(),
                                                                                                         ap.get()))
            self.conn.commit()
            return 0
        except BaseException:
            return 1


class Manager(Employee):
    def __init__(self, id, privilege):
        super(Manager, self).__init__(id=id, privilege=privilege)

    def check_report(self, id=None):
        if id is None:
            cur = self.conn.cursor()
            cur.execute('Select * from transaction_table;')
            rows = cur.fetchall()
            return rows
        else:
            cur = self.conn.cursor()
            cur.execute('Select * from transaction_table where transactionid=(\'{}\');'.format(id))
            rows = cur.fetchall()
            return rows

    def create_new_employee(self, fn, ln, uid, pl):
        cur = self.conn.cursor()
        try:
            cur.execute("Insert into user_table values (\'{}\',\'{}\',\'{}\', {});".format(fn.get(),
                                                                                           ln.get(),
                                                                                           uid.get(),
                                                                                           pl.get(),
                                                                                           ))
            self.conn.commit()
            return 0
        except BaseException:
            return 1

