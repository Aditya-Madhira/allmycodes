#python prog to implement bike renting system
#non dataase prog
#10 user limit
import sys
import random
import mysql.connector
import string
s=5


con=mysql.connector.connect(host='localhost',   user='root',password='12345',db='bikesys')
cur=con.cursor()

ulist=[]
class Customer():
    Name = ""
    Password = ""
    objname=""

    def __init__(self, Name, Password,objname):
        self.Name = Name
        self.Password = Password
        self.objname=objname

    def changeuname(self):
        pass

    def changepass(self):
        pass

    def addnewuser(self):
        try:
            obj = self.objname
            name = self.Name
            passwd = self.Password
            myq = "INSERT INTO userdata (objname, uname,pwd) VALUES (%s, %s, %s)"
            vals = (obj, name, passwd)
            cur.execute(myq, vals)
            con.commit()
        except:
            print("an error has occured")
            print("This version does not support rollback ,exiting portal")
            sys.exit(0)
    def rent(self,objname,bname,dur):
        try:
            obj=self.objname

            myq = "INSERT INTO userrent (objname, bikename,duration) VALUES (%s, %s, %s)"
            vals = (obj, bname, dur)
            cur.execute(myq, vals)
            con.commit()

        except:
            print("an error has occured")
            print("This version does not support rollback ,exiting portal")
            sys.exit(0)

    def rent_history(self):
        pass
    def return_info(self):
        pass


bike_l={
    'Zepplin':1000,'muntag':3000
}
bike_d_l={'Zepplin':10,'muntag':5}
def show_inventory():
    for i in bike_l.items():
        print(i)
    print("Enter the name of the bike you want to rent,additional info will be shown")
    bname=input()
    return bname



print(" HELLO, WELCOME TO ONLINE BIKE RENTALS")
print("1-New User,2-Exissting user,3-exit")
choice = int(input())
if (choice == 1):
    print("Please enter a username and password")
    uname = input("Username")
    pwd = input("password")
    ran = ''.join(random.choices(string.ascii_uppercase, k=s))
    ulist.append(ran)
    ulist[0]=Customer(uname,pwd,ulist[0])
    ulist[0].addnewuser()
    print("YAY - Welcome aboard!!!, {name}".format(name=ulist[0].Name))
    while(True):
        print("1-Rent, 2 - change username,3- change password,4-exit")
        c_1=int(input())
        if(c_1==1):
            bname=show_inventory()
            while(True):
                print("The duration is {d}".format(d=bike_d_l[bname]))
                print("1-Purchase,2- Go back")
                intchoice=int(input())
                if( intchoice ==1   ):
                    print("updating database,..... configuring engine ")
                    ulist[0].rent(ulist[0],bname,bike_d_l[bname])
                    print("Purchase successfull")
                    break

                if(intchoice==2):
                    break


        if (c_1 == 2):
            pass
        if (c_1 == 3):
            pass
        if(c_1==4):
            sys.exit(0)





if (choice == 2):
    name=input("enter username")
    passwd=input("enter password")
    #evealuate with db
    #update db



if (choice == 3):
    sys.exit(0)



