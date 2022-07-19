from tkinter import*
from tkinter import messagebox
import pyspeedtest

def logic():
    st = pyspeedtest.SpeedTest("www.google.com")
    d = (str(st.download())) + "[Bytes per second]"
    messagebox.showinfo("Your Download Speed:",d)

    st = pyspeedtest.SpeedTest("www.google.com")
    u = (str(st.upload())) + "[Bytes per second]"
    messagebox.showinfo("Your Upload Speed:", u)


logic()

#top = Tk()
#top.title('AK Speed Test')
#top.geometry('100x100')
#filename = PhotoImage(file ="A:\Edits\icon_speed.png")
