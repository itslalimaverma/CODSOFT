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
root.geometry("1000x700+300+300")
root.configure(bg="#d1edff")
root.resizable(False,False)

def getweather():
    city=testfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    #print(result)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d44fecaa88549bbffa2029d0571aa5c2"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

    

#Icon
Image_icon=PhotoImage(file="weather logo.png")
root.iconphoto(False,Image_icon)

#search box
Search_image=PhotoImage(file="search box.png")
myimage=Label(image=Search_image,bg="#d1edff")
myimage.place(x=20,y=20)
testfield=tk.Entry(root,justify='left',width=25,font=('poppins',20,'bold'),bg="#3C3B3B",border=0,fg='white')
testfield.place(x=50,y=45)
testfield.focus()
#search icon
Search_icon=PhotoImage(file="search icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#3C3B3B",command=getweather)
myimage_icon.place(x=410,y=35)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=200,y=150)

#box bottom
frame=Frame(root,width=1000,height=180,bg="#001a2b")
frame.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,'bold'),bg="#d1edff")
name.place(x=30,y=100)
clock=Label(root,font=("arial",20),bg="#d1edff")
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("arial",15,'bold'),fg="white",bg="#001a2b")
label1.place(x=250,y=530)

label2=Label(root,text="HUMIDITY",font=("arial",15,'bold'),fg="white",bg="#001a2b")
label2.place(x=350,y=530)

label3=Label(root,text="DESCRIPTION",font=("arial",15,'bold'),fg="white",bg="#001a2b")
label3.place(x=500,y=530)

label4=Label(root,text="PRESSURE",font=("arial",15,'bold'),fg="white",bg="#001a2b")
label4.place(x=700,y=530)

t=Label(font=("arial",80,"bold"),fg="#ee666d",bg="#d1edff")
t.place(x=600,y=150)
c=Label(font=("arial",20,"bold"),bg="#d1edff")
c.place(x=600,y=300)

w=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef",bg="#001a2b")
w.place(x=250,y=600)
h=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef",bg="#001a2b")
h.place(x=350,y=600)
d=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef",bg="#001a2b")
d.place(x=500,y=600)
p=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef",bg="#001a2b")
p.place(x=750,y=600)









root.mainloop()
