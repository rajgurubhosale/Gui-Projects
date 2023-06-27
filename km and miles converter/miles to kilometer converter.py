from tkinter import *

root=Tk()


#size
root.title('Km-To-Miles')
root.geometry('270x160')
root.maxsize(270,160)
root.minsize(270,160)
root.config(background="black")


def miles_to_km():
    global miles
    try:
        miles=miles_entry.get()
        kilometer=int(miles)*1.60934
        output.insert(0,f'miles: {miles} in kilometer: {kilometer}')
    except:
        output.delete(0,END)
        output.insert(0,'enter number')


def clear():
    miles_entry.delete(0,END)
    output.delete(0,END)


#header of km_miles_tital
km_miles_header=Label(root,text="Miles to Kilometer Converter",bg="white",fg="black",padx=50,pady=8)
km_miles_header.grid(row=0,column=0,columnspan=2,pady=(3,4))
km_miles_header.config(font=('verdana',8,'bold'))

#miles
miles_label=Label(text="Miles:",bg="orange",fg="black",padx=20,pady=6)
miles_label.grid(row=1,column=0)
miles_label.config(font=('verdana',10))

#kilometer input
miles_entry=Entry(root,width=32,borderwidth=3)
miles_entry.grid(row=1,column=1,columnspan=2,ipady=5)


#convert button
convert_button=Button(root,text="Convert",bg="yellow",fg="black",width=15,command=miles_to_km)
convert_button.grid(row=2,column=0,columnspan=2)

#output in kilometer
output=Entry(root,width=46,borderwidth=3)
output.grid(row=3,column=0,columnspan=2,ipady=5,padx=(0,5))
output.config(font=('Ariel',8,'bold'))

#clear Button+
clear_button=Button(root,text="Clear",bg="yellow",fg="black",width=15,command=clear)
clear_button.grid(row=4,column=0,columnspan=2)

root.mainloop()
