#!/usr/bin/env python
# coding: utf-8

# In[68]:


from tkinter import *
import tkinter as tk
from geopy.geocoders import Photon
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests 
import pytz
from newsapi import NewsApiClient


root=Tk()
root.title("The Local Guide App")
root.geometry("900x500+300+200")
root.resizable(True,True)
news_api_key='2add1761eac745a59255f197de4b72ca'


def getLocalData():
    try:
        city=textfield.get()
    
        geolocator=Photon(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)

    
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7274a4b9bc8213d8775663d16fb4a6a2"
    
        json_data = requests.get(api).json()
        country = json_data['sys']['country']
        getcity = json_data['name']
        name.config(text="Showing the current weather for " + getcity + "," + country )
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-272.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']


        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)


        # Get news top headlines
        newsapi = NewsApiClient(api_key=news_api_key)
        top_headlines = newsapi.get_everything(q=getcity,sort_by='relevancy',
                                          language='en',page_size=1,page=1)

        # Extract and print the article titles
        news.config(text=top_headlines['articles'][0]['title'])
        print(top_headlines['articles'][0]['title'])
        
    except Exception as e:
        messagebox.showerror("Invalid Ciy Name!")


#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center", width=17,font=("poppins",25,"bold"),
                   bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getLocalData)
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.place(x=60,y=320)

#time
name=Label(root, font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="White",bg="#1ab5ef")
label1.place(x=120,y=350)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="White",bg="#1ab5ef")
label2.place(x=250,y=350)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="White",bg="#1ab5ef")
label3.place(x=430,y=350)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="White",bg="#1ab5ef")
label4.place(x=650,y=350)

label5=Label(root,text="NEWS",font=("Helvetica",15,"bold"),fg="White",bg="#1ab5ef")
label5.place(x=30,y=420)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)  
c=Label(font= ("arial",15,'bold'))
c.place(x=400,y=250)   

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=380)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=380)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=380)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=380)

news=Label(root, font=("arial",15,"bold"))
news.place(x=30,y=450) 

root.mainloop()


# In[ ]:




