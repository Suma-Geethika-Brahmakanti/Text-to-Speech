#Importing all the required modules
import tkinter as tk
import PyPDF2
import pyttsx3
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import ttk
from PIL import Image, ImageTk

#selectionbutton
def select_pdf():
    global page_content
    file = askopenfile(parent=root,mode='rb',title="choose a file",filetype=[("Pdf file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        def get_text():
            try:
                text=int(x.get())-1
            except:
                if str(x.get())== "" :
                    y.set("Enter page Number")
                else:
                    y.set("Wrong page Number")
            print(text)
            return text
        a=get_text()
        page = read_pdf.getPage(a)
        page_content=page.extractText()
        

#objectcreation
speak = pyttsx3.init()

#Playbutton Function
def play():
    func1()
    func2()
    func3()
    print(page_content)
    speak.say(page_content)
    speak.runAndWait()

#Save button function
def save_mp3():
    print((page_content))
    try:
        speak.save_to_file(page_content, 'new.mp3')
        speak.runAndWait()

    except:
        y.set("Not Saved")

    


#speedmodulation
def func2():
    speedmod=v2.get()
    if speedmod=="SLOW":
        speak.setProperty('rate',50)
    elif speedmod=="NORMAL":
        speak.setProperty('rate',200)
    elif speedmod=="FAST":
        speak.setProperty('rate',400)
    else :
        speak.setProperty('rate',200)

#volumevariation
def func3():
    volumevar=v3.get()
    if volumevar=="LOW":
        speak.setProperty("volume",0.1)
    elif volumevar=="MEDIUM":
        speak.setProperty("volume",0.5)
    elif volumevar=="HIGH":
        speak.setProperty("volume",1)
    else :
        speak.setProperty("volume",0.5)

#voicemodulation
voices = speak.getProperty('voices')
def func1():
    gender=v1.get()
    if gender =="MALE":
        speak.setProperty("voice",voices[0].id)
    elif gender =="FEMALE":
        speak.setProperty("voice",voices[1].id)
    else :
        speak.setProperty("voice",voices[0].id)


#creating Tkinter window        
    
root=Tk()
root.title("Text to speech")
root.geometry("1300x700")
root.maxsize(1300,700)
root.minsize(1300,700)
root.configure(bg="#E6E6FA")
#logo
#Topframe
Top_frame=Frame(root,bg="#8250C4",width=1300,height=100)
Top_frame.place(x=0,y=0)
Logo=PhotoImage(file="speaker logo.png")
Label(Top_frame,image=Logo,bg="#8250C4").place(x=10,y=5)
Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="#8250C4",fg="white").place(x=100,y=30)

#textareas
x=StringVar()
x.set("")
y=StringVar()
y.set("")
text_area=Entry(root,textvariable=x,font="Robote 20",bg="white",relief=GROOVE)
text_area.place(x=70,y=350)
error=Entry(root,textvariable=y,font="Robote 20",bg="#E6E6FA",fg="black",relief=FLAT)
error.place(x=70,y=450)

#Labeling
Label(root,text="GENDER",font="Lucida 15 bold",bg="#E6E6FA",fg="black").place(x=590,y=160)
Label(root,text="SPEED",font="Lucida 15 bold",bg="#E6E6FA",fg="black").place(x=800,y=160)
Label(root,text="VOLUME",font="Lucida 15 bold",bg="#E6E6FA",fg="black").place(x=990,y=160)
Label(root,text="Enter Page Number",font="Lucida 15 bold",bg="#E6E6FA",fg="black").place(x=115,y=300)
#buttons
imageicon1=PhotoImage(file="select.png")
select=Button(root,text="Select PDF",image=imageicon1,compound=LEFT,font="lucida 20 bold",fg="black",bg="#E6E6FA",relief=FLAT,command=select_pdf,width=250,height=70)
select.place(x=90,y=170)
imageicon=PhotoImage(file="ooo.png")
Play=Button(root,compound=LEFT,image=imageicon,width=190,height=90,fg="black",bg="#E6E6FA",relief=FLAT,font="lucida 25 bold",command=play)
Play.place(x=600,y=400)
imageicon2=PhotoImage(file="mmm.png")
Save=Button(root,compound=LEFT,image=imageicon2,width=190,height=90,fg="black",bg="#E6E6FA",relief=FLAT,font="lucida 25 bold",command=save_mp3)
Save.place(x=850,y=400)

#radiobuttons
v1=StringVar()
v1.set(1)
v2=StringVar()
v2.set(1)
v3=StringVar()
v3.set(1)
l1=["MALE","FEMALE"]
l2=["SLOW","NORMAL","FAST"]
l3=["LOW","MEDIUM","HIGH"]
for i in range(2):
    radio=Radiobutton(root,relief=FLAT,bg="#E6E6FA",fg="black",text=l1[i],variable=v1,value=l1[i],command=func1).place(x=600,y=200+30*i)
for i in range(3):
    radio=Radiobutton(root,relief=FLAT,bg="#E6E6FA",fg="black",text=l2[i],variable=v2,value=l2[i],command=func2).place(x=800,y=200+30*i)
for i in range(3):
    radio=Radiobutton(root,relief=FLAT,bg="#E6E6FA",fg="black",text=l3[i],variable=v3,value=l3[i],command=func3).place(x=1000,y=200+30*i)

root.mainloop()
