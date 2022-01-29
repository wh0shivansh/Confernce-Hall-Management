# THIS IS A BASIC   CONFERENCE HALL MANAGEMENT PROJECT BY SHIVANSH UPADHYAY
from tkinter import*
import sqlite3
from tkinter import messagebox

mydb = sqlite3.connect('conferenceHall.db')
print("Database Connected Sucessfully")

# CREATING CURSOR OBJECT  
c = mydb.cursor()

# EXECUTING SQL QUERY
# c.execute('''CREATE TABLE records(
#         NAME text    NOT NULL,
#         HALL text    NOT NULL,
#         CHAIRS integer  NOT NULL,
#         PROJECTOR text  NOT NULL,
#         HEADCOUNT integer   NOT NULL,
#         TOTALCOST integer)''')
# print("Table Succesfully Created")

# CREATIN THE MAIN WINDOW OR MASTER WINDOW
master = Tk()
master.geometry("1200x650")
master.maxsize(1200,650)
master.minsize(1200,650)

master.title("Conference Hall Booking")
master.configure(bg="#fcde67")


##########  VARIABLES DECLARATION  #########
name_var = StringVar()
chairs_var = IntVar()
radio_btn = IntVar()
hedcount_var = IntVar()

######## FUNCTIONS DEFINITION #########
def totalcost():
    if(clicked.get()=="Select any" or chairs_entry=="" or headcount_entry.get()=="" or headcount_entry.get()==""):
        messagebox.showerror("Error","All Fields Are Required")
    else:
        if(clicked.get()=="Hall - 1"):c = 10000
        elif(clicked.get()=="Hall - 2"):c = 9000
        elif(clicked.get()=="Hall - 3"):c = 8000
        elif(clicked.get()=="Hall - 4"):c = 5000
        elif(clicked.get()=="Hall - 5"):c = 2000

        if(radio_btn.get()==1):d=1000
        elif(radio_btn.get()==2):d=0

        a = int(chairs_entry.get()) * 45
        b = int(headcount_entry.get()) * 150
        totalcost_display = Label(bookingFrame,bd=1,text=(a+b+c+d),width=1,bg="white")
        totalcost_display.grid(row=7,column=1,padx="0 20",ipadx=30,ipady=4,pady="0 8")
        return a+b+c+d

# THE YES/NO RADIOBUTTONS OF PROJECTOR MANAGED THROUGH THIS FUNCTION
def getradiobtn():
    if(radio_btn.get()==1):
        return 1
    elif(radio_btn.get()==2):
        return 0

# SUBMIT BUTTON
def submit():
    user_entered = IntVar()
    show_user_entry = StringVar()
    if(clicked.get()=="Hall - 1"):
        user_entered = 1
        show_user_entry="1"
    elif(clicked.get()=="Hall - 2"):
        user_entered = 2
        show_user_entry="2"
    elif(clicked.get()=="Hall - 3"):
        user_entered = 3
        show_user_entry="3"
    elif(clicked.get()=="Hall - 4"):
        user_entered = 4
        show_user_entry="4"
    elif(clicked.get()=="Hall - 5"):
        user_entered = 5
        show_user_entry="5"
    if(name_entry.get()=="" or chairs_entry.get()=="" or clicked.get()=="Select any" or radio_btn==None or headcount_entry.get()==""):
        messagebox.showerror("Error","All Fields Are Required")
    
    else:
        if(user_entered == 2):
            mydb = sqlite3.connect('conferenceHall.db')
            c=mydb.cursor()
            c.execute("SELECT NAME from records WHERE HALL=2")
            check=c.fetchone()
            mydb.commit()
            mydb.close()
        elif(user_entered == 1):
            mydb = sqlite3.connect('conferenceHall.db')
            c=mydb.cursor()
            c.execute("SELECT NAME from records WHERE HALL=1")
            check=c.fetchone()
            mydb.commit()
            mydb.close()
        elif(user_entered == 3):
            mydb = sqlite3.connect('conferenceHall.db')
            c=mydb.cursor()
            c.execute("SELECT NAME from records WHERE HALL=3")
            check=c.fetchone()
            mydb.commit()
            mydb.close()
        elif(user_entered == 4):
            mydb = sqlite3.connect('conferenceHall.db')
            c=mydb.cursor()
            c.execute("SELECT NAME from records WHERE HALL=4")
            check=c.fetchone()
            mydb.commit()
            mydb.close()
        elif(user_entered == 5):
            mydb = sqlite3.connect('conferenceHall.db')
            c=mydb.cursor()
            c.execute("SELECT NAME from records WHERE HALL=5")
            check=c.fetchone()
            mydb.commit()
            mydb.close()
        
        if(check==None):
            yes_no = StringVar()

            if(getradiobtn()==1):
                yes_no="Yes"
            elif(getradiobtn()==0):
                yes_no ="No"

            mydb = sqlite3.connect('conferenceHall.db')

            c=mydb.cursor()
            c.execute("INSERT INTO records VALUES(:NAME,:HALL,:CHAIRS,:PROJECTOR,:HEADCOUNT,:TOTALCOST)",
                {
                    'NAME':name_entry.get(),
                    'HALL':user_entered,
                    'CHAIRS':chairs_entry.get(),
                    'PROJECTOR':yes_no,
                    'HEADCOUNT':headcount_entry.get(),
                    'TOTALCOST':totalcost()
                }

            )
            print("Inserted Succesfully")
            name_entry.delete(0,END)
            chairs_entry.delete(0,END)
            headcount_entry.delete(0,END)
            clicked.set("Select Any")
            totalcost_display = Label(bookingFrame,bd=1,text=0,width=1,bg="white")
            totalcost_display.grid(row=7,column=1,padx="0 20",ipadx=30,ipady=4,pady="0 8")

            mydb.commit()
            mydb.close()
        else:
            messagebox.showerror("Error","Hall "+show_user_entry+" Is Already Occupied \nClick On Show Button and Check For Available Halls")

# DISPLAYING THE RECORDS FROM THE TABLE records IN THE DATABASE conferenceHall.db
def show():
    
    records_frame = Frame(showBookings,bg="white")
    records_frame.place(x=0,y=19,height=500,width=656)
    mydb = sqlite3.connect('conferenceHall.db')

    c=mydb.cursor()
    c.execute("SELECT oid,* FROM records") # oid also called unique row id
    records = c.fetchall()
    print_id = ''
    print_name = ''
    print_halls = ''
    print_chairs = ''
    print_projector = ''
    print_headcount = ''
    print_totalcost = ''
    for record in records:
        print_id += str(record[0]) + "\n"
    for record in records:
        print_name += str(record[1]) + "\n"
    for record in records:
        print_halls += str(record[2]) + "\n"
    for record in records:
        print_chairs += str(record[3]) + "\n"
    for record in records:
        print_projector += str(record[4]) + "\n"
    for record in records:
        print_headcount += str(record[5]) + "\n"
    for record in records:
        print_totalcost += str(record[6]) + "\n"

    records_label_id = Label(records_frame,text=print_id,width=5,bg="white")
    records_label_id.grid(row=0,column=0)
    records_label_name = Label(records_frame,text=print_name,width=18,bg="white")
    records_label_name.grid(row=0,column=1)
    records_label_halls = Label(records_frame,text=print_halls,bd=1,width=15,bg="white")
    records_label_halls.grid(row=0,column=2)
    records_label_chairs = Label(records_frame,text=print_chairs,bd=1,width=8,bg="white")
    records_label_chairs.grid(row=0,column=3)
    records_label_projector = Label(records_frame,text=print_projector,width=13,bg="white")
    records_label_projector.grid(row=0,column=4)
    records_label_headcount = Label(records_frame,text=print_headcount,width=15,bg="white")
    records_label_headcount.grid(row=0,column=5)
    records_label_totalcost = Label(records_frame,text=print_totalcost,width=13,bg="white")
    records_label_totalcost.grid(row=0,column=6)


    mydb.commit()
    mydb.close()

# DELETE BUTTON 
# DELETE ENTRY BOX TAKES THE ID OF THE HALL AND ENDS THE MEETING OR SAY DELETE THAT RECORDS FROM DATABASE 
def delete():
    if(delete_entry.get()==""):
        messagebox.showerror("Error","Please Enter An Id To Delete")
    mydb = sqlite3.connect('conferenceHall.db')

    c=mydb.cursor()
    c.execute("DELETE from records WHERE HALL="+delete_entry.get())

    mydb.commit()
    mydb.close()
    delete_entry.delete(0,END)
    records_frame.destroy()
    show()

# JUST CREATED 5 HALLS FOR A VERY BASIC 
# DEFINITELY CAN TAKE MORE AS PER REQUIREMENT
options = [
    "Hall - 1",
    "Hall - 2",
    "Hall - 3",
    "Hall - 4",
    "Hall - 5"
]
clicked = StringVar()
clicked.set("Select any")

####### BOOKING-HALL FRAME STARTS HERE ######
heading = Label(master,text="WELCOME TO CONFERENCE HALL MANGEMENT",font=("" ,30, "bold"),fg="#030e12",bg="#fcde67")
heading.pack(pady="20 20",side=TOP)

bookingFrame = Frame(master,bg="#5bccf6")
bookingFrame.pack(ipady=24,padx="20 10",ipadx=25,side=LEFT)

##########  INSIDE BOOKING-HALL FRAME #########

heading_lbl = Label(bookingFrame,text="Book Hall",bg="#fcde67",fg="black",font=("",17))
heading_lbl.grid(row=0,columnspan=2,pady="15 30",)

name_lbl = Label(bookingFrame,text="Enter Your Name",bg="#5bccf6",font=("times",16))
name_entry = Entry(bookingFrame,font=("",12),width=13,justify=CENTER)

halls_lbl = Label(bookingFrame,text="Halls Available",bg="#5bccf6",font=("Times",16))
halls_entry = OptionMenu(bookingFrame,clicked,*options)
halls_entry.configure(bg="white",relief=RIDGE,font=("",10,"bold"))

chairs_lbl = Label(bookingFrame,text="Number Of Chairs",bg="#5bccf6",font=("times",16))
chairs_entry = Entry(bookingFrame,relief=SUNKEN,width=13,font=("",12),justify=CENTER)

projector_lbl = Label(bookingFrame,text="Projector",bg="#5bccf6",font=("Times",16,""))
radio1 = Radiobutton(bookingFrame,text="Yes",bg='#5bccf6',value=1,variable=radio_btn)
radio2 = Radiobutton(bookingFrame,text="No",bg='#5bccf6',value=2,variable=radio_btn)

headcount_lbl = Label(bookingFrame,text="Enter Headcount",bg="#5bccf6",font=("times",16))
headcount_entry = Entry(bookingFrame,justify=CENTER,width=13,font=("",12))


totalcost_btn = Button(bookingFrame,command=totalcost,text="Total Cost",bg="white",bd=3,relief=RAISED,font=("times",14))
totalcost_display = Label(bookingFrame,bd=1,text=0,width=1,bg="white")
delete_lbl = Label(bookingFrame,text="HALL ID",bg="#5bccf6",font=("times",12))
delete_entry = Entry(bookingFrame,width=4,justify=CENTER,font=("times",12))

###########        CREATING BUTTONS - SUBMIT | SHOW | DELETE | EXIT        ##################
ButtonsFrame = Frame(bookingFrame,bg="#5bccf6")
ButtonsFrame.place(x=8,y=479,width=445,height=40)

submit_btn = Button(ButtonsFrame,text="Submit",command=submit,bg="#1a1a1d",fg="white",relief=RAISED,bd=1,pady=5,padx=15,font=("",12,"bold"))

show_btn = Button(ButtonsFrame,text="Show",command=show,bg="#1a1a1d",fg="white",relief=RAISED,bd=1,pady=5,padx=15,font=("",12,"bold"))


delete_btn = Button(ButtonsFrame,command=delete,text="End Meeting",bg="#1a1a1d",fg="white",relief=RAISED,bd=1,pady=5,padx=15,font=("",12,"bold"))

exit_btn = Button(ButtonsFrame,text="Exit",command=master.destroy,bg="#1a1a1d",fg="white",relief=RAISED,bd=1,pady=5,padx=15,font=("",12,"bold"))




name_lbl.grid(row=1,column=0,padx="20 50",pady="0 30")
name_entry.grid(row=1,column=1,padx="0 20",ipadx=30,ipady=4,pady="0 30")
halls_lbl.grid(row=2,column=0,padx="8 50",pady="0 30")
halls_entry.grid(row=2,column=1,padx="0 20",ipadx=30,ipady=4,pady="0 30")

chairs_lbl.grid(row=3,column=0,pady="0 15",padx="0 24")
chairs_entry.grid(row=3,column=1,padx="0 20",ipadx=30,ipady=4,pady="0 15")

projector_lbl.grid(row=4,column=0,pady="0 20",padx="0 30")
radio1.grid(row=4,column=1,padx="0 72")
radio2.grid(row=5,column=1,pady="0 20",padx="0 72")

headcount_lbl.grid(row=6,column=0,padx="20 50",pady="0 20")
headcount_entry.grid(row=6,column=1,padx="0 20",ipadx=30,ipady=4,pady="0 20")

totalcost_btn.grid(row=7,column=0,padx="20 50",pady="0 8")
totalcost_display.grid(row=7,column=1,padx="0 20",ipadx=30,ipady=4,pady="0 8")

delete_lbl.grid(row=8,column=0,padx="20 50",pady="0 5")
delete_entry.grid(row=8,column=1,padx="0 20",ipady=3,pady="0 5")


submit_btn.grid(row=0,column=0,padx="7 9")
show_btn.grid(row=0,column=1,padx=9)
delete_btn.grid(row=0,column=3,padx=9)
exit_btn.grid(row=0,column=4,padx=9)


####### HALL-BOOKING FRAME ENDS HERE #######

####### SHOW-BOOKINGS FRAME STARTS HERE ######

showBookings = Frame(master,bg="white",width=10)
showBookings.pack(ipady=254,padx="10 20",side=RIGHT)

######### INSIDE SHOW-BOOKINGS FRAME #########

id_label = Label(showBookings,text='Id',width=5,bd=1,bg="white",relief=SOLID)
id_label.grid(row=0,column=0)

name_label = Label(showBookings,text="Name",width=18,bg="white",bd=1,relief=SOLID)
name_label.grid(row=0,column=1)

halls_label = Label(showBookings,text="Hall Number",width=15,bg="white",bd=1,relief=SOLID)
halls_label.grid(row=0,column=2)

chairs_label = Label(showBookings,text="Chairs",width=8,bg="white",bd=1,relief=SOLID)
chairs_label.grid(row=0,column=3)

projector_label = Label(showBookings,text="Projector",width=13,bg="white",bd=1,relief=SOLID)
projector_label.grid(row=0,column=4)

headcount_label = Label(showBookings,text="Head Count",width=15,bg="white",bd=1,relief=SOLID)
headcount_label.grid(row=0,column=5)

totalcost_label = Label(showBookings,text="Total Cost",width=13,bg="white",bd=1,relief=SOLID)
totalcost_label.grid(row=0,column=6)

records_frame = Frame(showBookings,bg="white")
records_frame.place(x=0,y=19,height=500,width=656)




mydb.commit()
mydb.close()
master.mainloop()