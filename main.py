from distutils.log import error
from tkinter import*
import sqlite3
from tkinter import messagebox


mydb = sqlite3.connect('conferenceHall.db')
print("Database Connected Sucessfully")

# CREATING CURSOR OBJECT  
c = mydb.cursor()

# CREATING TABLE
# c.execute('''CREATE TABLE registered_users(
#          NAME text    NOT NULL,
#          USERNAME text    NOT NULL,
#          PASSWORD text  NOT NULL)''')
# print("Table Succesfully Created")

# WHENEVER YOU WANTED TO CLEAR THE TABLE UNCOMMENT THE BELOW LINES
# c.execute("DELETE FROM registered_users")
# print("Deleted Succesfully ")

root = Tk()
root.title("Login Page")
root.geometry("1200x650")
root.maxsize(1200,650)
root.minsize(1200,650)
root.configure(bg="#fcde67")

def login():
    if(login_username_entry.get()=="" or password_entry.get()==""):
        messagebox.showerror("Error","All Fields Are Required")
    mydb=sqlite3.connect('conferenceHall.db')
    print("Database Connected Succesfully")

    c=mydb.cursor()

    c.execute("SELECT USERNAME from registered_users WHERE PASSWORD="+password_entry.get())
    rec = c.fetchone()
    c.execute("SELECT NAME from registered_users WHERE PASSWORD="+password_entry.get())
    newrec = c.fetchone()
    if(rec!=None and newrec!=None):
        unique_username = str(rec[0])
        unique_name = str(newrec[0])
    
    if(rec==None):
        messagebox.showerror("Error","No Such User Registered")
    if(unique_username == login_username_entry.get()):
        messagebox.showinfo("Welcome","Welcome To Conference Hall Management System "+unique_name)
        root.destroy()
        from additional import ConferenceHall
    elif(unique_username != login_username_entry.get()):
        messagebox.showerror("Error","Wrong Username or Password")
    
    mydb.commit()
    mydb.close()
        

def signup():
    login_username_entry.delete(0,END)

    def register():
        if(name_entry.get()=="" or register_username_entry.get()=="" or password_entry.get()=="" or confirm_password_entry.get()==""):
            messagebox.showerror("Error","All Fields Are Required")
        elif(password_entry.get()!=confirm_password_entry.get()):
            messagebox.showerror("Error","Password Does Not Match")
        else:
            mydb = sqlite3.connect('conferenceHall.db')
            print("Database Connected Sucessfully")

            # CREATING CURSOR OBJECT  
            c = mydb.cursor()
            c.execute("SELECT USERNAME from registered_users WHERE PASSWORD="+password_entry.get())
            check = c.fetchone()
            if(check == None):
                mydb = sqlite3.connect('conferenceHall.db')
                print("Database Connected Sucessfully")

                # CREATING CURSOR OBJECT  
                c = mydb.cursor()

                c.execute("INSERT INTO registered_users VALUES(:NAME,:USERNAME,:PASSWORD)",
                    {
                        'NAME':name_entry.get(),
                        'USERNAME':register_username_entry.get(),
                        'PASSWORD':password_entry.get()
                    }

                )
                print("Inserted Succesfully")

                mydb.commit()
                mydb.close()
                name_entry.delete(0,END)
                register_username_entry.delete(0,END)
                password_entry.delete(0,END)
                confirm_password_entry.delete(0,END)

                signup_frame.place_forget()
                login_frame.place(x=360,y=180)
            else:
                messagebox.showerror("Error","Password Already Exists")


            


    login_frame.place_forget()
    signup_frame = Frame(root,bg="#5bccf6",width=454,bd=3,relief=RIDGE,height=250)
    signup_frame.place(x=330,y=150)
    heading = Label(signup_frame,text="Sign Up Here",bg="#fcde67",fg="black",font=("",20))
    heading.grid(row=0,column=0,columnspan=5,pady=12)

    name_label = Label(signup_frame,text="Name",bg="#fcde67",fg="black",font=("",12),padx=5,pady=3)
    name_label.grid(row=1,column=0,padx=30,pady="30 0")

    name_entry = Entry(signup_frame,font=("",12),justify=CENTER)
    name_entry.grid(row=1,column=1,pady="30 0",padx=30,ipadx=30,ipady=4)

    register_username_label = Label(signup_frame,text="Username",bg="#fcde67",fg="black",font=("",12),padx=5,pady=3)
    register_username_label.grid(row=2,column=0,padx=32,pady="30 0")

    register_username_entry = Entry(signup_frame,font=("",12),justify=CENTER)
    register_username_entry.grid(row=2,column=1,pady="30 0",padx=32,ipadx=30,ipady=4)

    password_label = Label(signup_frame,text="Password",bg="#fcde67",fg="black",font=("",12),padx=5,pady=3)
    password_label.grid(row=3,column=0,padx=30,pady="30 0")

    password_entry = Entry(signup_frame,show="@",font=("",12),justify=CENTER)
    password_entry.grid(row=3,column=1,pady="30 0",padx=32,ipadx=30,ipady=4)

    confirm_password_label = Label(signup_frame,text="Confirm Password",bg="#fcde67",fg="black",font=("",12),padx=5,pady=3)
    confirm_password_label.grid(row=4,column=0,padx=30,pady="30 15")

    confirm_password_entry = Entry(signup_frame,show="@",font=("",12),justify=CENTER)
    confirm_password_entry.grid(row=4,column=1,pady="30 15",padx=32,ipadx=30,ipady=4)

    register_btn = Button(signup_frame,command=register,text="Register",bg="#1a1a1d",fg="white",padx=10,relief=SUNKEN,bd=2,font=("",12))
    register_btn.grid(row=5,column=0,pady=5)


login_frame = Frame(root,bg="#5bccf6",width=454,bd=3,relief=RIDGE,height=250)
login_frame.place(x=360,y=180)

heading = Label(login_frame,text="Login Here",bg="#fcde67",fg="black",font=("",20))
heading.grid(row=0,column=0,columnspan=5,pady=12)

login_username_label = Label(login_frame,text="Username",bg="#fcde67",fg="black",font=("",12),padx=5,pady=3)
login_username_label.grid(row=1,column=0,padx=30,pady="30 0")

login_username_entry = Entry(login_frame,font=("",12))
login_username_entry.grid(row=1,column=1,pady="30 0",padx=32,ipadx=30,ipady=4)

password_label = Label(login_frame,text="Password",bg="#fcde67",fg="black",font=("",12),padx=5,pady=3)
password_label.grid(row=2,column=0,padx=30,pady="10 10")

password_entry = Entry(login_frame,show="@",font=("",12))
password_entry.grid(row=2,column=1,pady="10 10",padx=32,ipadx=30,ipady=4)

login_btn = Button(login_frame,command=login,text="Login",bg="#1a1a1d",fg="white",bd=2,relief=SUNKEN)
login_btn.grid(row=3,column=0,pady="10 10",ipadx=20)

signup_msg = Label(login_frame,text="Don't have an account?",bg="#5bccf6",font=("",11))
signup_msg.grid(row=4,column=0,pady="5 10")
sign_up = Button(login_frame,command=signup,text="Sign Up",bg="#1a1a1d",fg="white")
sign_up.place(x=171,y=220)


mydb.commit()
mydb.close()

root.mainloop()