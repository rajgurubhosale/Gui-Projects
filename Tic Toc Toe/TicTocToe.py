from tkinter import *
from tkinter import messagebox

root=Tk()
#basics
root.geometry('279x252')
root.maxsize(279,252)
root.minsize(279,252)
root.title('Tic-Toc-Toe')


clicked = True
count = 0

def disable_all_button():
    b1['state']="disabled"
    b2['state']="disabled"
    b3['state']="disabled"
    b4['state']="disabled"
    b5['state']="disabled"
    b6['state']="disabled"
    b7['state']="disabled"
    b8['state']="disabled"



def winner():
    global win,clicked,var,count
    if b1['text'] == b2['text'] and b1['text'] == b3['text'] and (b1['text']=="O" or b1['text']=="X"):
        var=b1['text']
        b1['bg']="orange"
        b2['bg']="orange"
        b3['bg']="orange"
        messagebox.showinfo('Tic-Toc-Toe',f'winner is: {var}')
        disable_all_button()

    if b4['text'] == b5['text'] and b4['text'] == b6['text'] and (b4['text'] == "O" or b4['text'] == "X"):
        var = b4['text']
        b4['bg'] = "orange"
        b5['bg'] = "orange"
        b6['bg'] = "orange"
        messagebox.showinfo('Tic-Toc-Toe', f'winner is: {var}')
        disable_all_button()

    if b7['text'] == b8['text'] and b7['text'] == b9['text'] and (b7['text'] == "O" or b7['text'] == "X"):
        var = b7['text']
        b7['bg'] = "orange"
        b8['bg'] = "orange"
        b9['bg'] = "orange"
        messagebox.showinfo('Tic-Toc-Toe', f'winner is: {var}')
        disable_all_button()

    if b1['text'] == b4['text'] and b1['text'] == b7['text'] and (b1['text'] == "O" or b1['text'] == "X"):
        var = b1['text']
        b1['bg'] = "orange"
        b4['bg'] = "orange"
        b7['bg'] = "orange"
        messagebox.showinfo('Tic-Toc-Toe', f'winner is: {var}')
        disable_all_button()

    if b2['text'] == b5['text'] and b2['text'] == b8['text'] and (b2['text'] == "O" or b2['text'] == "X"):
        var = b2['text']
        b2['bg'] = "orange"
        b5['bg'] = "orange"
        b8['bg'] = "orange"
        messagebox.showinfo('Tic-Toc-Toe', f'winner is: {var}')
        disable_all_button()

    if b3['text'] == b6['text'] and b3['text'] == b9['text'] and (b3['text'] == "O" or b3['text'] == "X"):
        var = b3['text']
        b3['bg'] = "orange"
        b6['bg'] = "orange"
        b9['bg'] = "orange"
        messagebox.showinfo('Tic-Toc-Toe', f'winner is: {var}')
        disable_all_button()

    if b1['text'] == b5['text'] and b1['text'] == b9['text'] and (b1['text'] == "O" or b1['text'] == "X"):
        var = b1['text']
        b1['bg'] = "orange"
        b5['bg'] = "orange"
        b9['bg'] = "orange"
        messagebox.showinfo('Tic-Toc-Toe', f'winner is: {var}')
        disable_all_button()


    if b3['text'] == b5['text'] and b3['text'] == b7['text'] and (b3['text'] == "O" or b3['text'] == "X"):
        var = b1['text']
        b3['bg'] = "orange"
        b5['bg'] = "orange"
        b7['bg'] = "orange"
        messagebox.showinfo('Tic-Toc-Toe', f'winner is: {var}')
        disable_all_button()
    if count == 9 and winner == False:
        messagebox.showinfo('Tic-Toc-Toe', 'Draw')
        disable_all_button()


def click(b):
    global clicked,count
    if clicked==True and b['text']==" ":
        b['text'] = "X"
        clicked=False
        count=count+1
        winner()

    elif clicked==False and b['text']==" ":
        b['text'] = "O"
        clicked=True
        count=count+1

        winner()
    elif count==9:
        messagebox.showinfo('tic-toc-toe','Start a New Game')
        disable_all_button()

    else:
        messagebox.showerror('Tic-Toc-Toe','move already there')

b1=Button(root,text=" ",padx=40,pady=30,command=lambda :click(b1))
b2=Button(root,text=" ",padx=40,pady=30,command=lambda :click(b2))
b3=Button(root,text=" ",padx=40,pady=30,command=lambda :click(b3))
b4=Button(root,text=" ",padx=40,pady=30,command=lambda :click(b4))
b5=Button(root,text=" ",padx=40,pady=30,command=lambda :click(b5))
b6=Button(root,text=" ",padx=40,pady=30,command=lambda :click(b6))
b7=Button(root,text=" ",padx=40,pady=30,command=lambda :click(b7))
b8=Button(root,text=" ",padx=40,pady=30,command=lambda :click(b8))
b9=Button(root,text=" ",padx=40,pady=30,command=lambda :click(b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)



root.mainloop()
