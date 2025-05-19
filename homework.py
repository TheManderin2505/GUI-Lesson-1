from tkinter import *

root = Tk()
root.geometry("100x100")
root.title("Game_1")

bn1 = Button(root,text = "Left",bd = 5,background="yellow",command=root.destroy)
bn1.pack(side =  'left')

bn2 = Button(root,text ="Right",bd = 5,background="blue",command=root.destroy)
bn2.pack(side = 'right')

bn3 = Button(root,text="Top",bd=5, background= "green",command=root.destroy)
bn3.pack(side='top')

bn4 = Button(root,text="bottem",bd=5,background="blue",command=root.destroy)
bn4.pack(side='bottom')

root.mainloop()