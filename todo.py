import tkinter
from tkinter import *

root=Tk()
root.title("List Me Up!")
root.geometry("500x650+400+200")
root.configure(bg="#ffd1f4")
root.resizable(False,False)

Tasks=[]

#icon
Image_icon=PhotoImage(file="tasks.png")
root.iconphoto(False,Image_icon)

dockImage=PhotoImage(file="dock.png")
Label(root,image=dockImage,bg="#ffd1f4").place(x=30,y=40)


noteImage=PhotoImage(file="1.png")
Label(root,image=noteImage,bg="#ffd1f4").place(x=350,y=25)

heading=Label(root,text="YOUR TASKS", font="arial 30 bold",fg="#ff008c",bg="#ffd1f4")
heading.place(x=70,y=80)

#main
frame=Frame(root,width=500,height=60,bg="white")
frame.place(x=0,y=180)

task=StringVar()

task_entry=Entry(frame,width=20,font="arial 25",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button1=Button(frame,text="ADD",font="arial 25 bold",width=6,bg="#750046",fg="#fff",bd=0)
button1.place(x=380,y=0)

#list
frame1=Frame(root,bd=3,width=700,height=300,bg="#750046")
frame1.pack(pady=(250,0))

listbox=Listbox(frame1,font=('arial',12),width=70,height=20,bg="#750046",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommannd=scrollbar.set)
scrollbar.config(command=listbox.yview)




root.mainloop()
