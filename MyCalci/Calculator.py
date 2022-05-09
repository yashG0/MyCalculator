from tkinter import *

def click(event):
    global scValue
    text = event.widget.cget("text")
    if text == "=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:    
                print(e)
                value = "Error"
        scValue.set(value)
        screen.update()

    elif text == "C":
        scValue.set("")
        screen.update

    else:
        scValue.set(scValue.get() + str(text))
        screen.update()


root = Tk()
root.geometry("480x580")
root.maxsize(width=480,height=580)
root.minsize(width=480,height=580)

root.title("My-Calculator")
root.wm_iconbitmap("C:\\Users\\yashg\\Downloads\\myicon.ico")

scValue = StringVar()
scValue.set("")
screen = Entry(root,textvar=scValue,font="monospace 30 bold",border=2)
screen.pack(fill=X,ipadx=6,ipady=8,padx=6,pady=6)

# Frames -
f1 = Frame(root,bg="grey")
f1.pack()

f2 = Frame(root,bg="grey")
f2.pack()

f3 = Frame(root,bg="grey")
f3.pack()

f4 = Frame(root,bg="grey")
f4.pack()

f5 = Frame(root,bg="grey")
f5.pack()

# My Calci-Buttons(0,9)
for i in reversed(range(9,6,-1)) :
    b1 = Button(f1,text=i,padx=18,pady=12,font="Comic 20 bold")
    b1.pack(side=RIGHT,padx=15,pady=10)
    b1.bind("<Button-1>",click)

for i in reversed(range(6,3,-1)) :
    b1 = Button(f2,text=i,padx=18,pady=12,font="Comic 20 bold")
    b1.pack(side=RIGHT,padx=15,pady=10)
    b1.bind("<Button-1>",click)

for i in reversed(range(3,0,-1)) :
    b1 = Button(f3,text=i,padx=18,pady=12,font="Comic 20 bold")
    b1.pack(side=RIGHT,padx=15,pady=10)
    b1.bind("<Button-1>",click)

b1 = Button(f4,text="=",padx=18,pady=12,font="Comic 20 bold")
b1.pack(side=RIGHT,padx=15,pady=10)
b1.bind("<Button-1>",click)

b1 = Button(f4,text="C",padx=18,pady=12,font="Comic 19 bold")
b1.pack(side=RIGHT,padx=15,pady=10)
b1.bind("<Button-1>",click)

b1 = Button(f4,text=0,padx=18,pady=12,font="Comic 19 bold")
b1.pack(side=RIGHT,padx=15,pady=10)
b1.bind("<Button-1>",click)

b1 = Button(f4,text=".",padx=18,pady=12,font="Comic 20 bold")
b1.pack(side=RIGHT,padx=15,pady=10)
b1.bind("<Button-1>",click)

b1 = Button(f5,text="+",padx=18,pady=12,font="Comic 22 bold")
b1.pack(side=RIGHT,padx=15,pady=10)
b1.bind("<Button-1>",click)
b1 = Button(f5,text="-",padx=18,pady=12,font="Comic 22 bold")
b1.pack(side=RIGHT,padx=15,pady=10)
b1.bind("<Button-1>",click)
b1 = Button(f5,text="*",padx=18,pady=12,font="Comic 22 bold")
b1.pack(side=RIGHT,padx=15,pady=10)
b1.bind("<Button-1>",click)
b1 = Button(f5,text="/",padx=18,pady=12,font="Comic 22 bold")
b1.pack(side=RIGHT,padx=15,pady=10)
b1.bind("<Button-1>",click)

root.mainloop()