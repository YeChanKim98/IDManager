from tkinter import *
from sys import exit
from Form.IdManager_main import main_window

root = Tk()
root.title('Chk_Pass')
root.iconbitmap('C:\Temp\idm.ico')
root.geometry(f'220x105+{int(root.winfo_screenwidth() / 2) - 155}+{int(root.winfo_screenheight() / 2) - 350}')
chance = 3

def chk() :
    global chance
    if passwd.get() == '9860':
        root.destroy()
        main_window()
    else:
        if chance == 1 :
            exit()
        else :
            chance -= 1
            passwd.delete(0, 'end')
def chk_bind(event) :
    chk()

Label(root, text='Enter Password').place(x=68,y=10)
passwd = Entry(root,show='*',width=28);passwd.place(x=10, y=40); passwd.focus()
passwd.bind('<Return>',chk_bind)
btn_submit = Button(root, text="OK", width=10, command=chk).place(x=10, y=70)
btn_cancel = Button(root, text="Cancel",width=10, command=exit).place(x=130, y=70)
root.resizable(False, False)
root.mainloop()