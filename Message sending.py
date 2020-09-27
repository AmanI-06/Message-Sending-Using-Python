import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo,showerror
def send_sms(number,message):
    url='https://www.fast2sms.com/dev/bulk'
    params={'authorization':'2D9zPYmdaoi8XtsVAEBcOeKuhNvU5TxjC4WgrywH1SnG0fb3IRtMC5SyBIYW2vpTG3jfawKP8FcJEu9b',
                  'sender_id':'FSTSMS' ,
                  'message':message,
                  'language':'english',
                  'route':'p',
                  'numbers':number}
    response=requests.get(url,params=params)
    dicti=response.json()
    print(dicti)
    return dicti.get('return')

 #creating GUI
def btn_click():
    n=textNumber.get()
    m=textMsg.get("1.0",END)
    fun=send_sms(n,m)
    if fun==True:
        showinfo("Send Success","Message sent successfully")
    else:
        showerror("Send Failed","Message couldnt be delivered")
root=Tk()
root.title("Message Sender")
root.geometry("500x500")
font=("Arial",18,"bold")

textNumber=Entry(root,font=font)
textNumber.pack(fill=X,pady=25)

textMsg=Text(root)
textMsg.pack(fill=X)

sendBtn=Button(root,text="SEND MESSAGE",command=btn_click)
sendBtn.pack()

root.mainloop()
