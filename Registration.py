from tkinter import *
import mysql.connector


root= Tk() 

             
bg_color = 'teal'

def submit():
    print('SUBMITTED')
    print(f_namevalue.get(),l_namevalue.get(),(m_numbervalue.get()),
          emailvalue.get(),locationvalue.get())

    # insert data into database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="shorya_db"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO employee (f_name, l_name, m_number, email, location) VALUES (%s, %s, %s, %s, %s)"
    val = (f_namevalue.get(), l_namevalue.get(), m_numbervalue.get(), emailvalue.get(), locationvalue.get())
    mycursor.execute(sql, val)
    mydb.commit()
   
    
    submit_message.config(text='Hey,Registration Form Submitted Successfully...')
    

# reset all data after submission
    f_namevalue.set('')
    l_namevalue.set('')
    m_numbervalue.set('')
    emailvalue.set('')
    locationvalue.set('')   

root.geometry('450x450')
root.minsize(450,450)
root.maxsize(450,450)
root.title("Registration Application")
root.config(bg='teal') 

frame1= Frame(root, bg='teal')
frame1.grid(row=1,column=0)

label1= Label(root,text="Welcome to our application",font=('Arial',17,"bold"),bg='purple',fg='white',
               relief =SUNKEN, borderwidth=5,padx=20,pady=5)
label1.grid(row=0,column=0,padx=50,pady=10,sticky= W)

frame2 = Frame(frame1, bg= bg_color, width= 60)
frame2.grid(row=0, column=2,sticky= W)

photo = PhotoImage(file="F:\IT Learning\MY PROJECTS\Python+MySQL Project\Registration\Registration.png")
label_2 = Label(frame2, image=photo)
label_2.pack(pady=10,fill=X)


f_name= Label(frame1,text="First Name",font=("Arial",12),bg= 'orange',borderwidth=3, relief= SUNKEN,padx=18)
l_name= Label(frame1,text="Last Name",font=("Arial",12),bg= 'orange',borderwidth=3, relief= SUNKEN,padx=18)
m_number= Label(frame1,text='Mobile Number',font=("Arial",12),bg= 'orange',borderwidth=3, relief= SUNKEN,padx=2)
email= Label(frame1,text='Email ID',font=("Arial",12),bg= 'orange',borderwidth=3, relief= SUNKEN,padx=25)
location= Label(frame1,text='Location',font=("Arial",12),bg= 'orange',borderwidth=3, relief= SUNKEN,padx=25)

f_name.grid(row=2,column=1,padx=20,pady=3)
l_name.grid(row=3,column=1,padx=20,pady=3)
m_number.grid(row=4,column=1,padx=20,pady=3)
email.grid(row=5,column=1,padx=20,pady=3)
location.grid(row=6,column=1,padx=20,pady=3)

f_namevalue= StringVar()
l_namevalue= StringVar()
m_numbervalue= StringVar()
emailvalue= StringVar()
locationvalue=StringVar()

f_nameentry= Entry(frame1,textvariable=f_namevalue)
l_nameentry= Entry(frame1,textvariable=l_namevalue)
m_numberentry= Entry(frame1,textvariable=m_numbervalue)
emailentry= Entry(frame1,textvariable=emailvalue)
locationentry= Entry(frame1,textvariable=locationvalue)

f_nameentry.grid(row=2,column=2)
l_nameentry.grid(row=3,column=2)
m_numberentry.grid(row=4,column=2)
emailentry.grid(row=5,column=2)
locationentry.grid(row=6,column=2)
 
submit_button = Button(frame1, text="Submit", command= submit)
submit_button.grid(row=7, column=2, sticky= W,padx=0,pady=10)


submit_frame= Frame(root, width=450, height=10, bg= bg_color)
submit_frame.grid(row=10, column=0, sticky= W, padx= 1, pady= 80)

submit_message = Label(submit_frame, text="",bg=bg_color, font=("Arial", 12), relief=SUNKEN)
submit_message.grid(row=10, column=1,pady= 2, padx= 5)

root.mainloop()