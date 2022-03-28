import webbrowser
from tkinter import *
import tkinter.ttk as ttk
import DataControl.db_Controll as db
import tkinter.messagebox as msgbox
from Form.ins_win import insert_window
from Form.up_win import update_window

def main_window() :

    # Print Get List At Board
    def print_list(list) :
        for item in list :
            id_list.insert('', 'end', values=(item[0], item[2], item[3], item[4]))

    # Initialize List Board
    def list_initialize() :
        for row in id_list.get_children() :
            id_list.delete(row)
        print_list(db.search(search_kwd.get()))

    # Search
    def search():
        for row in id_list.get_children():id_list.delete(row) # Clear Board
        print_list(db.search(search_kwd.get())) # Add Search Result
    def bind_search(event) : search()
    def bind_search_press_key(event) : search()

    # Insert
    # 병합
    def insert() :
        insert_btn.config(state='disable')
        ires = insert_window()
        if  ires : list_initialize()
        insert_btn.config(state='normal')

    # Update
    def update() :
        update_btn.config(state='disable')
        if id_list.focus() != '' :
            update_window(id_list.item(id_list.focus()).get('values')[0:2])
            list_initialize()
        update_btn.config(state='normal')

    # delete
    def delete() :
        if  id_list.focus() != '' :
            target = (id_list.item(id_list.focus()).get('values')[0],str(id_list.item(id_list.focus()).get('values')[1]))
            if msgbox.askokcancel('Delete','Delete Select Account ?') :
                db.delete(target)
                list_initialize()

    def con_link(event) :
        link = db.get_link(id_list.item(id_list.focus()).get('values')[0])
        if link : webbrowser.open(link)


    root = Tk()
    root.title("IDM")
    root.iconbitmap('C:\Temp\idm.ico')
    root.geometry(f'730x310+{int(root.winfo_screenwidth() / 2) - 365}+{int(root.winfo_screenheight() / 2) - 400}')

#########################################[메뉴]###########################################
    '''
    menu = Menu(root)
    mf = Menu(root, tearoff=0)
    mf.add_command(label='Change Password')
    mf.add_separator()
    mf.add_checkbutton(label='Check_TEST')
    mf.add_separator()
    mf.add_command(label='Remove_All', stat='disable')

    mf2 = Menu(menu, tearoff=0)

    menu.add_cascade(label="File", menu=mf) # 기능
    menu.add_cascade(label="Help", menu=mf2) # 사용법 및 기타 명시
    '''
######################################################################################

    # Search
    search_frame = Frame(root)
    search_frame.pack(fill='x', padx=5, pady=5)
    search_btn = Button(search_frame, text='Search', width=10, height=1, command=search)
    search_btn.pack(side='right',padx=2)
    search_kwd = Entry(search_frame, text='', width=90)
    search_kwd.pack(side='right', ipady=2)
    search_kwd.bind('<Return>',bind_search)
    search_kwd.bind('<KeyRelease>',bind_search_press_key)

    # Account_List
    list_frame = Frame(root)
    list_frame.pack(fill='both', padx=5, pady=5)
    scroll = Scrollbar(list_frame)
    scroll.pack(side='right', fill='y')
    id_list = ttk.Treeview(list_frame, columns=['Site','ID','PW','Note'],displaycolumns=['Site','ID','PW','Note'],selectmode='extended',height=10, yscrollcommand=scroll.set)
    id_list.pack(side='left', fill='both', expand=True)
    id_list.column('#0',width=0, stretch=NO)
    id_list.column('#1', anchor='center',width=100)
    id_list.heading('Site',text='Site', anchor='center')
    id_list.column('#2', anchor='center',width=200)
    id_list.heading('ID',text='ID', anchor='center')
    id_list.column('#3', anchor='center',width=200)
    id_list.heading('PW',text='PW', anchor='center')
    id_list.column('#4', anchor='center',width=200)
    id_list.heading('Note',text='Note', anchor='center')
    id_list.bind("<Double-Button-1>", con_link) # Double-1
    scroll.config(command=id_list.yview)
    list_initialize()
    # id_list.selection_set(10)

    # Function
    func_frame = Frame(root)
    func_frame.pack(fill='x', padx=5, pady=5)
    delete_btn = Button(func_frame, text='Delete',width=32, height=1, command=delete)
    delete_btn.pack(side='right', padx=3)
    update_btn = Button(func_frame, text='Update',width=32, height=1, command=update)
    update_btn.pack(side='right', padx=3)
    insert_btn = Button(func_frame, text='Insert', width=32, height=1, command=insert)
    insert_btn.pack(side='right', padx=3)
    root.resizable(False, False)

    # root.config(menu=menu)
    root.mainloop()

# main_window()