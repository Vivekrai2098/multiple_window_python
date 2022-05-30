from tkinter import*
from tkinter import messagebox
import random
# s=random.randint(100,1000)
# so=random.randint(100,1000)
# print(s,so)
h=Tk()
h.title("SBI Bank")
# h.geometry("200x200+{}+{}".format(s,so))
h.geometry("300x200+600+200")
h.title("Information")
def shyam1():
        j=Toplevel()
        j.title("information")
        Label(j, text="you are hacked.....",fg='black', height=45, width=40).pack()
        # Label(j, text="share the bitcoins......",fg='red', height=45, width=40).pack()
        s = random.randint(130, 970)
        so = random.randint(200, 920)
        j.geometry("200x200+{}+{}".format(s, so))

def shyam():
    for i in range(30):
        shyam1()
        # k = Toplevel()
        # s = random.randint(100, 1000)
        # so = random.randint(100, 1000)
        # k.geometry("200x200+{}+{}".format(s, so))
k=Label(h,text="cliam your prize",font=("arial",29),fg='black',height=45,width=40)
k.place(x=300,y=200)
bt=Button(text="Widthdrwal money",bd=2,fg="green",command=shyam)
bt.place(x=10,y=12)
def cool():
    h.destroy()
bt=Button(text="exit",bd=2,fg="red",command=cool)
bt.place(x=220,y=12)
k.pack()
h.mainloop()