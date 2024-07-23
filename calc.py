from tkinter import *

win=Tk()
win.title(Calculator)
win.geometry(570x600+100+200)
win.resizable(False,False)
win.configure(bg='grey')


label_result=Label(win,width=25,height=2,text=,background='red',font=('arial',30)) #for output screen
label_result.pack()

eqn=
def disp(val):
    global eqn
    eqn+=val
    label_result.config(text=eqn)

def clear():
    global eqn
    eqn=
    label_result.config(text=eqn)

def calculate():
    global eqn 
    result=
    if eqn !=:
        try:
            result=eval(eqn)
        except:
            result=error
            eqn=
    label_result.config(text=result)
