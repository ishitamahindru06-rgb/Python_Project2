import csv
import random
from prettytable import PrettyTable

#function to enter train list
def train_list():
    import csv
    f=open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\train.csv","a",newline='')
    w = csv.writer(f)
    rec = []
    while True:
        print("Enter Train details: ")
        sno = int(input("Train_No : "))
        sn= input(" Train_Name : ")
        s= input("Soure: ")
        d= input("Destination : ")
        a= int(input("AC  Fare:"))
        sl=int(input("Sleeper Fare:"))
        rec.append([sno,sn,s,d,a,sl])
        ch = input("Do you want to continue ?? (Y?N)")
        if ch == "N" or ch =="n":
            break
    w.writerows(rec)
    f.close()
#function to enter train schedule
def train_schedule():
    import csv
    f1=open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\train schedule.csv","a",newline='')
    w = csv.writer(f1)
    rec = []
    while True:
        print("Enter Train details: ")
        sno = int(input("Train_No : "))
        sn= input(" Train_Name : ")
        a=float(input("Arrival Time:"))
        dp=float(input("Departure Time:"))
        s= input("Soure: ")
        d= input("Destination : ")
        rec.append([sno,sn,a,dp,s,d])
        ch = input("Do you want to continue ?? (Y?N)")
        if ch == "N" or ch =="n":
            break
    w.writerows(rec)
    f1.close()
#function to enter train fare
def train_fare ():
    import csv
    f=open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\train fare.csv","a",newline='')
    w = csv.writer(f)
    rec = []
    while True:
        print("Enter Train details: ")
        sno = int(input("Train_No : "))
        sn= input(" Train_Name : ")
        a= int(input("AC  Fare:"))
        sl=int(input("Sleeper Fare:"))
        rec.append([sno,sn,a,sl])
        ch = input("Do you want to continue ?? (Y?N)")
        if ch == "N" or ch =="n":
            break
    w.writerows(rec)
    f.close()
#function to display train list
def display_train_list():
     import csv
     from prettytable import PrettyTable
     f=open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\train.csv","r")
     ro = csv.reader(f)
     traindata=list(ro)
     t=PrettyTable(["Train_No","Train_Name","Soure","Destination","AC Fare","Sleeper Fare"])
     for i in traindata[1:]:
         t.add_row(i)
     print(t)
     f.close()
#function to display schedule of trains
def display_train_schedule():
     import csv
     from prettytable import PrettyTable
     f=open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\train schedule.csv","r")
     r = csv.reader(f)
     traindata=list(r)
     t=PrettyTable(["Train_No","Train_Name","Arrival Time(AM)","Departure Time(AM)","Soure","Destination"])
     for i in traindata[1:]:
         t.add_row(i)
     print(t)
     f.close()
# function to display fare of trains
def display_train_fare():
     import csv
     from prettytable import PrettyTable
     f=open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\train fare.csv","r")
     r = csv.reader(f)
     traindata=list(r)
     t=PrettyTable(["Train_No","Train_Name","AC Fare","Sleeper Fare"])
     for i in traindata[1:]:
         t.add_row(i)
     print(t)
     f.close()
#function to book a new train reservation
def new_ticketreservation():
    import csv
    train = input ("Enter the Train Number you want to book: ")
    train_found=False
    ac_fare =0
    slp_fare=0
    with open (r"C:\Users\hp\AppData\Local\Programs\Python\Python311\train.csv", "r") as obj:
        reader= csv.reader (obj)
        next(reader)
        for row in reader:
            if row[0]==train:
                train_found =True
                ac_fare= row[4]
                slp_fare=row[5]
                print("AC FARE OF SPECIFIED TRAIN NO.:",ac_fare)
                print( "SLEEPER FARE OF SPECIFIED TRAIN NO.:",slp_fare)
                break
    if not train_found:
        print ("No Train Found")
        return
    with open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\reservation1.csv", "a", newline='') as obj1:
        w1= csv.writer (obj1)
        num = int(input ("How many Reservations do you want to make? "))
        pnr = generate_pnr()
        total_fare =0
        print ("Please Enter the Passenger details...")
        for i in range (num):
            name=input ("Name of the Passenger: " )
            phn = input ("Phone Number: ")
            age=int (input ("Age: "))
            gender= input ("Gender (M-Male/F-Female/0-Others): ").upper()
            if gender not in ["M", "F", "O"]:
                print ("Wrong Option")
            category =input ("Category (G-General, SR-Senior citizen, D-Disabled): ").upper ()
            if category not in ["G","SR", "D"]:
                print ("Wrong Option")
            Class =input("AC/SLEEPER").upper ()
            if  Class not in ["AC", "SLEEPER"]:
                print ("Wrong Option")
                continue
            if Class=="AC":
                fare=ac_fare
            else:
                fare =slp_fare
            l= [pnr, train, name, phn,age, gender.upper (), category.upper(),Class.upper(), fare]
            w1.writerow(l)
            total_fare += int (fare)
    print("reservation for",num,"passengers done successfully")
    print("PNR:",pnr)
    print("total fare:",total_fare)

#function to generate pnr no.
def generate_pnr():
    import random
    random_num= str(random.randint (100, 999))
    pnr= "PNR" + random_num
    return pnr
#function to display the reservations made
def display_listofreservations():
    import csv
    from prettytable import PrettyTable
    print ("LIST OF ALL RESERVATIONS")
    print ()
    with open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\reservation1.csv", "r") as file:
        reader = csv.reader (file)
        res_data= list (reader)
        table = PrettyTable (["PNR", "Train No.", "Passenger Name", "Phone No.", "Age", "Gender","Category", "Class", "'Fare"])
        for row in res_data[1:]:
                              table.add_row (row)
        print (table)    
#function to search a passenger details using PNR number
def find_pnr():
    import csv
    from prettytable import PrettyTable
    pnr= input ("Enter the PNR number: ")
    reservation_found = False
    records = []
    with open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\reservation1.csv", "r") as obj:
        reader = csv.reader (obj)
        for row in reader:
            if row[0] == pnr:
                reservation_found = True
                records.append(row)
    if reservation_found:
        print ("RESERVATION DETAILS: ")
        table = PrettyTable (["PNR", "Train Number", "Passenger Name", "Phone Number", "Age","Gender", "Category", "Class",  "Fare"])
        for record in records:
            table.add_row (record)
        print (table)
    else:
        print ("No records found.")

#function to signup
def signup():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    with open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\login1.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, password])
        print("Account created successfully!")

#function to login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    found = False
    with open(r"C:\Users\hp\AppData\Local\Programs\Python\Python311\login1.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == username and row[1] == password:
                found = True
                print("Login successful!")
                while True:
                    print ("====================================================================================================")
                    print(" OPTIONS THAT ARE AVAILABLE ")
                    print ("1. Entering Train List")
                    print ("2. Entering Train Schedule")
                    print ("3. Entering Train Fare")
                    print ("4. Display All the PNR Tickets")
                    print ("5. Display Specific Train Ticket Details using PNR")
                    print ("6. Display Train List")
                    print ("7. Display Train Schedule")
                    print ("8. Display Train Fare")
                    print()
                    print(" BOOKING OF TICKETS")
                    print ("9. Book New Ticket Reservation")
                    print ("10. WIFI")
                    print("11. Customer support")
                    print ("12. Quit")
                    print ("====================================================================================================")
                    choice=int (input ("Enter your choice (1-12):"))
                    if choice==1:
                        print("YOU HAVE SELECTED 1 TO  Entering LIST OF TRAINS")
                        train_list ()
                    elif choice==2:
                        print("YOU HAVE SELECTED 2 TO  Entering TRAIN SCHEDULE")
                        train_schedule ()
                    elif choice==3:
                        print("YOU HAVE SELECTED 3 TO  Entering TRAIN FARE")
                        train_fare ()
                    elif choice==4:
                        print("YOU HAVE SELECTED 4 TO  DISPLAY LIST OF TRAIN RESERVATION")
                        display_listofreservations ()
                    elif choice==5:
                        print("YOU HAVE SELECTED 5 TO  DISPALY RECORD OF PASSENGERS USING PNR NO.")
                        find_pnr ()
                    elif choice==6:
                        print("YOU HAVE SELECTED 6 TO  DISPLAY LIST OF TRAINS")
                        display_train_list ()
                    elif choice==7:
                        print("YOU HAVE SELECTED 7 TO  DISPLAY TRAIN SCHEDULE")
                        display_train_schedule ()
                    elif choice==8:
                        print("YOU HAVE SELECTED 8 TO  DISPLAY TRAIN FARE")
                        display_train_fare ()
                    elif choice ==9:
                        print("YOU HAVE SELECTED 9 TO BOOK YOUR TRAIN TICKET")
                        new_ticketreservation ()
                    elif choice==10:
                        print("YOU HAVE SELECTED 10 TO  AVAIL FREE WIFI FACILITY")
                        p= input("Enter your PNR  ")
                        print("The wifi code for ",p, "  is  134671")
                    elif choice==11:
                       print("We are sorry for the inconvenience caused. You can email the queries to : Indianrailways@gmail.com or call us at 01824-64598")
                       p= input("Enter your PNR ")
                       print("You shall receive a callback within 12-16 hours regarding the issues you've faced")
                    elif choice ==12:
                        print("YOU HAVE SELECTED 12 TO QUIT")
                        print("---------------Thank you for visiting Indian Railways Ticket Booking System Developed by: Hridya Sharma,Ishita-------------------")
                        break
                    ch=input ("Do you want to continue (y/n)?")
                    if ch not in ['y', 'Y', 'yes', 'YES', 'Yes']:
                        print("Thank you for visiting Indian Railways Ticket Booking System Developed by: Ishita, Hridya Sharma")
                        break
    if not found:
        print("Invalid username or password. Try again!")


                                                                                                                            #MAIN SECTION
print ("--------------------------------------------Welcome To Indian Railways Ticket Booking System ----------------------------------------")
print("------------------------------------------------For any enqueries select various options given-------------------------------------------")
print("-----------------------------------------------------Customer Support No.::0755-3934141----------------------------------------------")
print("PRESS : 1 FOR LOGIN OPTION")
print("PRESS : 2 FOR SINGN UP OPTION")
n=int(input("Enter the no (1,2):"))
if n==1:
    print("you have selected for Login option")
    login()
if n==2:
    signup()
    print("kindly log into the account using valid credentials")
    login()
    
    
