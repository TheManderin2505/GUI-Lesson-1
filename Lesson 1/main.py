from tkinter import *

#creating the output window
root = Tk()
root.geometry("250x250")            #set width + height
root.title("First App")

#creating widget - button , text , enery ....

btn1 = Button(root, text = "Click Here" , background = "purple", bd = 5, command = root.destroy)
#side = top, bottom, left, right
btn1.pack(side = 'bottom',pady=20)


root.mainloop()
