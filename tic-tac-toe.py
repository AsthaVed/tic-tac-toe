'''
from tkinter import *
import tkinter.messagebox

def play(btn):
    global flag,counter
    if btn["text"]==" " and flag==True:
        flag=False
        btn["text"]="X"
        counter += 1
        check()
    elif btn["text"]==" " and flag==False:
        flag=True
        btn["text"]="O"
        counter += 1
        check()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Not Allowed")

def clearBtn():
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "

def check():
    global counter,ptr1,ptr2,p1_score,p2_score
    if (btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X' or 
        btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X' or
        btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X' or
        btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X' or 
        btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X' or
        btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X' or
        btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X' or 
        btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X'):
        clearBtn()
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Player 1 Win")
        ptr1+=1
        counter=0
        p1_score.set(ptr1)
    elif (btn1['text']=='O' and btn2['text']=='O' and btn3['text']=='O' or
          btn4['text']=='O' and btn5['text']=='O' and btn6['text']=='O' or
          btn7['text']=='O' and btn8['text']=='O' and btn9['text']=='O' or
          btn1['text']=='O' and btn5['text']=='O' and btn9['text']=='O' or 
          btn3['text']=='O' and btn5['text']=='O' and btn7['text']=='O' or
          btn1['text']=='O' and btn4['text']=='O' and btn7['text']=='O' or
          btn3['text']=='O' and btn6['text']=='O' and btn9['text']=='O' or 
          btn2['text']=='O' and btn5['text']=='O' and btn8['text']=='O'):
          clearBtn()
          tkinter.messagebox.showinfo("Tic-Tac-Toe","Player 2 Win")
          ptr2+=1
          counter=0
          p2_score.set(ptr2)
    elif (counter==9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Match is Tie")
        clearBtn()
        play()

root=Tk()
root.title("Tic-Tac-Toe Game")
root.geometry("350x381+500+200")
p1_score=StringVar()
p2_score=StringVar()
ptr1=0
ptr2=0
flag=True
counter=0

btn1=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn1))
btn1.grid(row=1, column=0)
btn2=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn2))
btn2.grid(row=1, column=1)
btn3=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn3))
btn3.grid(row=1, column=2)
btn4=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn4))
btn4.grid(row=2, column=0)
btn5=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn5))
btn5.grid(row=2, column=1)
btn6=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn6))
btn6.grid(row=2, column=2)
btn7=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn7))
btn7.grid(row=3, column=0)
btn8=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn8))
btn8.grid(row=3, column=1)
btn9=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn9))
btn9.grid(row=3, column=2)

label = Label(root,text="Player 1:",font=("ariel",12,"bold"),bg="green",fg="white",)
label.grid(row=4, column=0, columnspan=2)
display = Entry(root,textvariable=p1_score,bd=12,width=6)
display.grid(row=4, column=2)
label = Label(root,text="Player 2:",font=("ariel",12,"bold"),bg="red",fg="white",)
label.grid(row=5, column=0, columnspan=2)
display = Entry(root,textvariable=p2_score,bd=12,width=6)
display.grid(row=5, column=2)
root.mainloop()
'''

from tkinter import *
import tkinter.messagebox
import random

def play(btn):
    global flag,counter
    if btn["text"]==" " and flag==True:
        flag=False
        btn["text"]="X"
        counter += 1
        check()
    elif btn["text"]==" " and flag==False:
        flag=True
        r = random.choice((btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9))
        btn["text"]= "O"
        counter += 1
        check()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Not Allowed")

def clearBtn():
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "

def check():
    global counter,ptr1,ptr2,p1_score,p2_score
    if (btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X' or 
        btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X' or
        btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X' or
        btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X' or 
        btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X' or
        btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X' or
        btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X' or 
        btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X'):
        clearBtn()
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Player 1 Win")
        ptr1+=1
        counter=0
        p1_score.set(ptr1)
    elif (btn1['text']=='O' and btn2['text']=='O' and btn3['text']=='O' or
          btn4['text']=='O' and btn5['text']=='O' and btn6['text']=='O' or
          btn7['text']=='O' and btn8['text']=='O' and btn9['text']=='O' or
          btn1['text']=='O' and btn5['text']=='O' and btn9['text']=='O' or 
          btn3['text']=='O' and btn5['text']=='O' and btn7['text']=='O' or
          btn1['text']=='O' and btn4['text']=='O' and btn7['text']=='O' or
          btn3['text']=='O' and btn6['text']=='O' and btn9['text']=='O' or 
          btn2['text']=='O' and btn5['text']=='O' and btn8['text']=='O'):
          clearBtn()
          tkinter.messagebox.showinfo("Tic-Tac-Toe","Player 2 Win")
          ptr2+=1
          counter=0
          p2_score.set(ptr2)
    elif (counter==9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Match is Tie")
        clearBtn()
        play()

root=Tk()
root.title("Tic-Tac-Toe Game")
root.geometry("350x381+500+200")
p1_score=StringVar()
p2_score=StringVar()
ptr1=0
ptr2=0
flag=True
counter=0

btn1=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn1))
btn1.grid(row=1, column=0)
btn2=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn2))
btn2.grid(row=1, column=1)
btn3=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn3))
btn3.grid(row=1, column=2)
btn4=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn4))
btn4.grid(row=2, column=0)
btn5=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn5))
btn5.grid(row=2, column=1)
btn6=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn6))
btn6.grid(row=2, column=2)
btn7=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn7))
btn7.grid(row=3, column=0)
btn8=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn8))
btn8.grid(row=3, column=1)
btn9=Button(root,text=" ",bd=25,height=2,width=6,font=("ariel",12,"bold"),command=lambda:play(btn9))
btn9.grid(row=3, column=2)

label = Label(root,text="Player 1:",font=("ariel",12,"bold"),bg="green",fg="white",)
label.grid(row=4, column=0, columnspan=2)
display = Entry(root,textvariable=p1_score,bd=12,width=6)
display.grid(row=4, column=2)
label = Label(root,text="Player 2:",font=("ariel",12,"bold"),bg="red",fg="white",)
label.grid(row=5, column=0, columnspan=2)
display = Entry(root,textvariable=p2_score,bd=12,width=6)
display.grid(row=5, column=2)
root.mainloop()