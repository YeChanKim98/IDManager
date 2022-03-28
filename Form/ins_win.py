from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import DataControl.db_Controll as db

def insert_window() :
    def insert() :
        submit_btn.config(state='disable')
        if site_name_entry.get() == '' or id_entry.get() == '' or pw_entry.get() == '' :
            msgbox.showwarning('Empty Value','Please Input Essential Value!')
            # 가능하면 창 top level로 변경 -> 현재 메시지박스 생성 후 하단으로 감
            root.attributes('-topmost', True)
        else :
            data=(site_name_entry.get(),site_url_entry.get(),id_entry.get(),pw_entry.get(),note_text.get("1.0","end-1c"))
            db.insert(data)
            close_window()

    def close_window() :
        root.quit()
        root.destroy()
    root = Tk()
    root.iconbitmap('C:\Temp\idm.ico')
    root.title("Insert New Account")
    root.geometry(f'310x230+{int(root.winfo_screenwidth() / 2) - 155}+{int(root.winfo_screenheight() / 2) - 350}')
    insert_frame = Frame(root)
    insert_frame.pack(fill='x', padx=5, pady=5)
    site_label = Label(insert_frame,text="* Site")
    site_name_entry = Entry(insert_frame)
    site_url_label = Label(insert_frame,text="Url")
    site_url_entry = Entry(insert_frame) # Null OK
    id_label = Label(insert_frame,text="* ID")
    id_entry = Entry(insert_frame,width=5)
    pw_label = Label(insert_frame,text="* PW")
    pw_entry = Entry(insert_frame,width=5)
    note_label = Label(insert_frame,text="Note",height=3)
    note_text = Text(insert_frame, height=5, width=35)
    submit_btn = Button(insert_frame,text="Submit",command=insert)


    site_label.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3)
    site_name_entry.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3)
    site_url_label.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
    site_url_entry.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
    id_label.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
    id_entry.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
    pw_label.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
    pw_entry.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
    note_label.grid(row=4,column=0, sticky=N+E+W+S, padx=3, pady=3)
    note_text.grid(row=4,column=1, sticky=N+E+W+S, padx=3, pady=3)
    submit_btn.grid(row=5,column=1, sticky=N+S+E, padx=3, pady=3)

    root.protocol('WM_DELETE_WINDOW',close_window)
    root.resizable(False, False)
    root.mainloop()
    return 1