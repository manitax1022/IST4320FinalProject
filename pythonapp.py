from tkinter import *

def save_info():
	first_name_info = firstname.get()
	last_name_info = lastname.get()
	studentid_info = studentid.get()

	print(first_name_info,last_name_info,studentid_info)

	file = open("user.text","w")

	file.write("Your First Name :" + first_name_info)  

	file.write("\n") 

	file.write("Your Last Name :" + last_name_info)

	file.write("\n")

	file.write("Your Coyote ID :" + str(studentid_info))

	file.close()

app = Tk()

app.geometry("500x500")

app.title("Python Data Saving")

heading = Label(text="Data Saving Forms",bg="orange",fg="black",font="10",width="500",height="3")

heading.pack()

firstname_text = Label(text="First Name :")
lastname_text = Label(text="Last Name :")
studentid_text = Label(text="Coyote ID :")

firstname_text.place(x=15,y=70)
lastname_text.place(x=15,y=140)
studentid_text.place(x=15,y=210)

firstname = StringVar()
lastname = StringVar()
studentid = IntVar()

first_name_entry = Entry(textvariable=firstname, width="30")
last_name_entry = Entry(textvariable=lastname,width="30")
student_id_entry = Entry(textvariable=studentid,width="30")

first_name_entry.place(x=15,y=100)
last_name_entry.place(x=15,y=180)
student_id_entry.place(x=15,y=240)

button = Button(app,text="Submit Data",command=save_info,width="30",height="2",bg="grey")
button.place(x=15,y=290)

mainloop()