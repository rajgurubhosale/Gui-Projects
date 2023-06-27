from tkinter import *

root = Tk()

root.title('Miles to Kilometer')
root.geometry('400x300')
root.maxsize(400,300)
root.minsize(400,300)
root.config(background="black")

#miles converter
def miles_converter():
    global mile
    try:
        km=kilometer_entry.get()
        mile=int(km) *0.62137119
        miles.insert(0,f'kilometers to miles: {mile}')

    except:
        miles.insert(0,"you entered a char, enter a number")

def clear():
    miles.delete(0,END)
    kilometer_entry.delete(0,END)


#miles
kilometer_miles=Label(root,text="Kilometer To Miles Program",width=30,bg="black",fg="white")
kilometer_miles.pack(pady=(10,5),ipady=5)
kilometer_miles.config(font=('verdana',10,'bold'))

kilometer=Label(root,text="Enter Kilometer",width=20,bg="black",fg="white")
kilometer.pack(ipady=3)
kilometer.config(font=('verdana',10))


kilometer_entry=Entry(root,width=30)
kilometer_entry.pack(pady=(5,10),ipady=3)

convert_button=Button(root,text="Convert",bg="yellow",fg="black",width=8,command=miles_converter)
convert_button.pack(ipady=1)
convert_button.config(font=('verdana',12))

miles=Entry(root,text="Miles",width=40,)
miles.pack(pady=(5,10),ipady=5)
miles.config(font=('verdana',10,'bold'))


clear_button=Button(root,text="Clear",bg="yellow",fg="black",width=8,command=clear)
clear_button.pack(ipady=1)
clear_button.config(font=('verdana',12))

root.mainloop()
