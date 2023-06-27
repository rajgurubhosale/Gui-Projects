from tkinter import *
root=Tk()

#title
root.title('Calculator')
#color background
root.config(background="black")


#size
root.geometry('300x317')
root.minsize(300,317)
root.maxsize(300,317)


def click_button(num):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(num))


def add_button():
    first_number=entry.get()
    global f_num
    global op
    f_num=int(first_number)
    op="add"
    entry.delete(0,END)
    entry.insert(0,'+')

def sub_button():
    first_number=entry.get()
    global f_num
    global op
    op="sub"
    f_num=int(first_number)
    entry.delete(0,END)

def mul_button():
    first_number=entry.get()
    global f_num
    global op
    f_num=int(first_number)
    op="mul"
    entry.delete(0,END)
def div_button():
    first_number=entry.get()
    global f_num
    global op
    f_num=int(first_number)
    op="div"
    entry.delete(0,END)

def equal_button():
    second_number=entry.get()
    entry.delete(0,END)
    if op == "add":
        entry.insert(0,f_num + int(second_number))
    if op == "sub":
        entry.insert(0,f_num - int(second_number))
    if op == "mul":
        entry.insert(0, f_num * int(second_number))
    if op == "div":
        entry.insert(0, round(f_num / int(second_number),4))
def clear_button():
    entry.delete(0,END)



#first row
entry=Entry(root,width=49,borderwidth=2)
entry.grid(row=0,column=0,columnspan=3,pady=(5,15),ipady=5)

#buttons widget
button_0=Button(root,text="0",padx=41,pady=10,bg="grey",command=lambda: click_button(0))
button_1=Button(root,text="1",padx=41,pady=10,bg="grey",command=lambda: click_button(1))
button_2=Button(root,text="2",padx=41,pady=10,bg="grey",command=lambda: click_button(2))
button_3=Button(root,text="3",padx=41,pady=10,bg="grey",command=lambda: click_button(3))
button_4=Button(root,text="4",padx=41,pady=10,bg="grey",command=lambda: click_button(4))
button_5=Button(root,text="5",padx=41,pady=10,bg="grey",command=lambda: click_button(5))
button_6=Button(root,text="6",padx=41,pady=10,bg="grey",command=lambda: click_button(6))
button_7=Button(root,text="7",padx=41,pady=10,bg="grey",command=lambda: click_button(7))
button_8=Button(root,text="8",padx=41,pady=10,bg="grey",command=lambda: click_button(8))
button_9=Button(root,text="9",padx=41,pady=10,bg="grey",command=lambda: click_button(9))

button_clear=Button(root,text="Clear",padx=81,pady=10,bg="yellow",command=clear_button)
button_equal=Button(root,text="=",padx=91,pady=10,bg="yellow",command=equal_button)

button_add=Button(root,text="+",padx=41,pady=10,bg="orange",command=add_button)
button_sub=Button(root,text="-",padx=41,pady=10,bg="orange",command=sub_button)
button_mul=Button(root,text="X",padx=41,pady=10,bg="orange",command=mul_button)
button_div=Button(root,text="/",padx=41,pady=10,bg="orange",command=div_button)

#second row
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

#third row
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

#forth row
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

#fifth row
button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)


#operator
button_add.grid(row=5,column=0)
button_sub.grid(row=5,column=1)
button_mul.grid(row=5,column=2)
button_div.grid(row=6,column=0)

#equal
button_equal.grid(row=6,column=1,columnspan=3)


root.mainloop()
