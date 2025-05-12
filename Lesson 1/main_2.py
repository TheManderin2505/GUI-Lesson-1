from tkinter import *

root = Tk()
root.geometry("450x350")
root.title("Log in")

User_l = Label(root, text = "User -->", fg = "black")
User_l.place(x=80, y=50)

User_e = Entry(root, width =35)
User_e.place(x=130, y = 50)

Password_l = Label(root,text="Password -->",fg="black")
Password_l.place(x = 53, y = 80 )

Password_e = Entry(root,width=35,show="*")
Password_e.place(x=130,y=80)

btn1 = Button(root,text="Submit",background="pink", bd = 5, command=root.destroy)
btn1.place(x=50,y=200)

root.mainloop()