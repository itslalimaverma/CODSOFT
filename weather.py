from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Weather Wizard!")
root.geometry("1000x600+300+300")
root.configure(bg="#d5f1f5")
root.resizable(False,False)

def getweather():
    city=testfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)
    longlat.config(text=f"{location.latitude}°N,{location.longitude}°E")

Image_icon=PhotoImage(file="weather logo.png")
root.iconphoto(False,Image_icon)

Round_box=PhotoImage(file="roundrec.png")
Label(root,image=Round_box,bg="#d5f1f5").place(x=30,y=10)

#labels
label1=Label(root,text="TEMPERATURE",font=("Arial",12),fg="white",bg="#002454")
label1.place(x=80,y=170)

label2=Label(root,text="HUMIDITY",font=("Arial",12),fg="white",bg="#002454")
label2.place(x=80,y=200)

label3=Label(root,text="PRESSURE",font=("Arial",12),fg="white",bg="#002454")
label3.place(x=80,y=230)

label4=Label(root,text="WIND SPEED",font=("Arial",12),fg="white",bg="#002454")
label4.place(x=80,y=260)

label5=Label(root,text="DESCRIPTION",font=("Arial",12),fg="white",bg="#002454")
label5.place(x=80,y=290)

#Search box
Search_image=PhotoImage(file="search box.png")
myimage=Label(image=Search_image,bg="#d5f1f5")
myimage.place(x=500,y=130)

#clo_image=PhotoImage(file="clouds.png")
#myimage1=Label(image=clo_image,bg="#acebf2")
#myimage1.place(x=500,y=20)

testfield=tk.Entry(root,justify='left',width=25,font=('poppins',20,'bold'),bg="#3C3B3B",border=0,fg='white')
testfield.place(x=550,y=150)
testfield.focus()

Search_icon=PhotoImage(file="search icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#3C3B3B",command=getweather)
myimage_icon.place(x=880,y=145)

#bottom box
frame=Frame(root,width=1000,height=180,bg="#212120")
frame.pack(side=BOTTOM)

firstbox=PhotoImage(file="box.png")
secondbox=PhotoImage(file="wb.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=5)
Label(frame,image=secondbox,bg="#212120").place(x=330,y=10)
Label(frame,image=secondbox,bg="#212120").place(x=430,y=10)
Label(frame,image=secondbox,bg="#212120").place(x=530,y=10)
Label(frame,image=secondbox,bg="#212120").place(x=630,y=10)
Label(frame,image=secondbox,bg="#212120").place(x=730,y=10)
Label(frame,image=secondbox,bg="#212120").place(x=830,y=10)


#clock
clock=Label(root,font=("Helvetica",30,'bold'),fg="#07001c",bg="#d5f1f5")
clock.place(x=70,y=30)

timezone=Label(root,font=("Helvetica",20),fg="#07001c",bg="#d5f1f5")
timezone.place(x=700,y=30)

longlat=Label(root,font=("Helvetica",10),fg="#07001c",bg="#d5f1f5")
longlat.place(x=700,y=70)


root.mainloop()
