import mysql.connector

class ResOrder:

    def CRUD(self):
        self.user_id = self.user_info[0][0]
        self.uname = self.user_info[0][1]
        self.password = self.user_info[0][2]
        while (True):
            self.choice = int(input(
                "Following Are the Operations :\n1.Orders\n2.Add a new Item\n3.Update Existing Orders\n4.Delete your Todo List\n5.Exit\nSelect Your Choice:"))

            if (self.choice == 1):  # Select Statement

                self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="food_order")
                self.mycursor = self.mydb.cursor()
                self.mycursor.execute("SELECT * FROM food_order.food_order WHERE c_id={};".format(self.user_id))
                self.result = self.mycursor.fetchall()

                if (self.mycursor.rowcount > 0):
                    print("------ORDER LIST---------")
                    print("Ord_Id  Fname Qty C_id")
                    for i in self.result:
                        print(i)
                else:
                    print("--------Your ORDER List is Empty-----")

            elif (self.choice == 2):  # Insert Statement

                self.fname= input("Enter your Order:")
                self.quantity=int(input("Enter the Quantity:"))
                self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="food_order")
                self.mycursor = self.mydb.cursor()

                self.mycursor.execute("SELECT * FROM food_order.food_order where fname='{}' and c_id={};".format(self.fname,self.user_id))
                self.result = self.mycursor.fetchall()
                if (self.mycursor.rowcount > 0):
                    # print("Hello")
                    # self.quantity = int(input("Enter the New Quantity:"))
                    self.mycursor.execute("UPDATE food_order.food_order set quantity={} where c_id={} AND fname='{}';".format(self.quantity,self.user_id,self.fname))
                    self.mydb.commit()
                else:
                    self.mycursor.execute("INSERT INTO food_order.food_order (fname,quantity,c_id) VALUES('{}',{},{});".format(self.fname,self.quantity,self.user_id));
                    self.mydb.commit()

            elif (self.choice == 3):  # Update Statement
                self.fname = input("Enter your Order:")

                self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="food_order")
                self.mycursor = self.mydb.cursor()
                self.mycursor.execute("SELECT * FROM food_order.food_order where fname='{}' and c_id={};".format(self.fname,self.user_id));
                self.result = self.mycursor.fetchall()
                if (self.mycursor.rowcount > 0):
                    self.quantity = int(input("Enter the New Quantity:"))
                    self.mycursor.execute("UPDATE food_order.food_order set quantity={} where c_id={} AND fname='{}';".format(self.quantity,self.user_id,self.fname))
                    self.mydb.commit()
                else:
                    print("No such order Exist ")

            elif (self.choice == 4):  # Delete Statement
                self.del_ord = int(input("Enter Order_id to Delete the Order:"))
                self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="food_order")
                self.mycursor = self.mydb.cursor()
                self.mycursor.execute("SELECT * FROM food_order.food_order where order_id={};".format(self.del_ord))
                self.result = self.mycursor.fetchall()
                # print("UserID",user_id,"\nResult",result)
                if (self.mycursor.rowcount > 0):
                    # print(result[0][1])
                    self.mycursor.execute("DELETE FROM food_order.food_order where order_id={};".format(self.del_ord))
                    self.mydb.commit()
                    print("-----List Deleted------")
                else:
                    print("No List Exist with Entered Order_id value")

            elif (self.choice == 5):  # Exit
                print("------------Program Terminated-------------")

                exit()
            else:
                print("Invalid Choice")

    def checkUP(self):

        self.check = int(input("Are you a Todo User (1/0):"))

        if (self.check == 1):
            self.checkCredentials()

        else:
            self.register()

    def checkCredentials(self):
        self.uname = input("Enter Username:")
        self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="food_order")
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("Select * from customer where username='{}'".format(self.uname))
        self.user_info = self.mycursor.fetchall()
        # print(mycursor.rowcount)
        if (self.mycursor.rowcount != 0):
            self.password = input("Enter Your Password:")
            self.mycursor.execute("SELECT password FROM customer WHERE username='{}';".format(self.uname))
            self.result = self.mycursor.fetchall()
            # print(self.result[0][0])
            if (self.result[0][0] == self.password):
                # print("-------")
                self.CRUD()

            else:
                print("-------Wrong Password------")


        else:
            print("No Username Found")
            self.register()

    def register(self):

        reg = int(input("Do you want to Register(1/0):"))
        while (True):
            if (reg == 1):
                # Check if uname exist
                self.uname = input("Enter Username:")
                self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="food_order")
                self.mycursor = self.mydb.cursor()
                self.mycursor.execute("Select * from customer where username='{}'".format(self.uname))
                self.result = self.mycursor.fetchall()
                # Check if uname exist

                if (self.mycursor.rowcount != 0):
                    print("Username Already Exists Plz Enter Valid Username")

                else:
                    self.password = input("Enter a Password consisting of Alphabet and Numbers:")
                    # Add uname and pass to user database

                    # print(pass_check,"----",password[0].isalpha())
                    self.digit = 0
                    self.alpha = 0
                    for i in self.password:
                        if (i.isdigit()):
                            self.digit = 1
                        elif (i.isalpha()):
                            self.alpha = 1

                    if not (self.digit == 1 and self.alpha == 1):
                        print("Invalid Password")
                        exit()
                    self.mycursor.execute(
                        "insert into food_order.CUSTOMER(username,password) value('{}','{}')".format(self.uname, self.password))
                    self.mydb.commit()
                    self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="food_order")
                    self.mycursor = self.mydb.cursor()
                    self.mycursor.execute("Select * from food_order.CUSTOMER where username='{}'".format(self.uname))
                    self.user_info = self.mycursor.fetchall()
                    self.CRUD()
            else:
                print("Sorry to here that!!")
                exit()


try:
    customer=ResOrder()
    customer.checkUP()
except Exception as ex:
    print(ex)
