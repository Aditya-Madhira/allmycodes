from tkinter import *
from googletrans import Translator
from tkinter import ttk

def translate():
    thetext=userinp.get()
    mytrans=Translator()
    src=mytrans.detect(thetext)
    mydest=comboinp.get()
    op=mytrans.translate(thetext,dest=mydest)
    oplabel=Label(mywin,text=op.text,width=20).place(x=910,y=400)






mywin=Tk()
userinp=StringVar()
comboinp=StringVar()


mywin.attributes("-fullscreen", True)
myLabel=Label(mywin,text="Translator",font=('Ariel',40)).place(x=631,y=68)
userenter=Entry(mywin,width=70,textvariable=userinp).place(x=156,y=400)
to=Label(mywin,text="To").place(x=620,y=400)

langs=['english','japanese','chinese','korean','russain','spanish','french','italian','hindi','telugu']

lang_chooser=OptionMenu(mywin,comboinp,*langs).place(x=700,y=400)
comboinp.set(langs[0])



translate=Button(mywin,text="Translate",command=translate).place(x=690,y=464)


mywin.bind('<Escape>',lambda x:mywin.destroy())

mywin.mainloop()