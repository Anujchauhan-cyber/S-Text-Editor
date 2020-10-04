import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,font,colorchooser,filedialog
import os

main_application=tk.Tk()
main_application.geometry('1200x600')
main_application.title('S-Text Editor')
main_application.wm_iconbitmap('icon.ico')

#--------------------------------------main menu-------------------------
main_menu = tk.Menu()

#-----flle menu -------
file_menu = tk.Menu(main_menu,tearoff=False)

#icons
new_icon = tk.PhotoImage(file=r'icons\new.png')
open_icon = tk.PhotoImage(file=r'icons\open.png')
save_icon = tk.PhotoImage(file=r'icons\save.png')
save_as_icon = tk.PhotoImage(file=r'icons\saveas.png')
exit_icon = tk.PhotoImage(file=r'icons\exit1.png')

#----end of file menu -----

#----edit menu -------
edit_menu = tk.Menu(main_menu,tearoff=False)

#icons
copy_icon=tk.PhotoImage(file=r'icons\copy.png')
paste_icon=tk.PhotoImage(file=r'icons\paste1.png')
cut_icon=tk.PhotoImage(file=r'icons\cut.png')
undo_icon=tk.PhotoImage(file=r'icons\undo_icon.png')
redo_icon=tk.PhotoImage(file=r'icons\redo_icon.png')
find_icon=tk.PhotoImage(file=r'icons\find.png')
clear_all_icon=tk.PhotoImage(file=r'icons\clear.png')

#-------end of file menu ----------


#---------view menu ------------

view_menu = tk.Menu(main_menu,tearoff=False)

#icons
viwe_toolbar_icon=tk.PhotoImage(file=r'icons\tool_bar.png')
view_status_icon=tk.PhotoImage(file=r'icons\status_bar.png')

#-------end of view menu-------------

#-------------color menu---------
color_menu = tk.Menu(main_menu,tearoff=False)


#icons
light_icon=tk.PhotoImage(file=r'icons\light_default.png ')
lightplus_icon=tk.PhotoImage(file=r'icons\light_plus.png')
dark_icon=tk.PhotoImage(file=r'icons\dark.png')
red_icon=tk.PhotoImage(file=r'icons\red.png')
monokai_icon=tk.PhotoImage(file=r'icons\monokai.png')
night_icon=tk.PhotoImage(file=r'icons\night_blue.png')

theme=tk.StringVar()
icons=(light_icon,lightplus_icon,dark_icon,red_icon,monokai_icon,night_icon)

color_dict ={
    'Light Default' : ('#000000','#ffffff'),
    'Light plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
    'Night' : ('#ededed','#6b9dc2')
    }
#--------------help menu ---------------------
help_menu = tk.Menu(main_menu,tearoff=False)

#casscading menu
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='View',menu=view_menu)
main_menu.add_cascade(label='Color Theme',menu=color_menu)
main_menu.add_cascade(label='Help',menu=help_menu)

#--------------------------------------main menu end------------------------


#-------------------------------------Toolbar----------------------------------------------
toolbar = ttk.Label(main_application)
toolbar.pack(side=tk.TOP, fill=tk.X)


#font_box
fonts = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(toolbar, width=30 , textvariable=font_family, state='readonly')
font_box['values'] = fonts
font_box.grid(row=0,column=0,padx=5)
font_box.current(fonts.index('Arial'))

#size box

size=tk.IntVar()
font_size=ttk.Combobox(toolbar, width=10, textvariable=size, state='readonly')
font_size['values'] = tuple(range(8,74,2))
font_size.current(2)
font_size.grid(row=0,column=1,padx=5)

#bold button
bold_icon=tk.PhotoImage(file=r'icons\bold.png')
bold_button = ttk.Button(toolbar, image=bold_icon)
bold_button.grid(row=0,column=2,padx=5)


#italic button
italic_icon=tk.PhotoImage(file=r'icons\italic.png')
italic_button=ttk.Button(toolbar, image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)


#underline button
underline_icon = tk.PhotoImage(file=r'icons\underline.png')
underline_button =  ttk.Button(toolbar, image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)



#font color button
font_color_icon = tk.PhotoImage(file=r'icons\font_color.png')
font_color_button = ttk.Button(toolbar, image=font_color_icon)
font_color_button.grid(row=0,column=5,padx=5)

#left align
left_align_icon = tk.PhotoImage(file=r'icons\align_left.png')
left_align_button = ttk.Button(toolbar, image=left_align_icon)
left_align_button.grid(row=0,column=6,padx=5)


#center align
center_align_icon = tk.PhotoImage(file=r'icons\align_center.png')
center_align_button = ttk.Button(toolbar, image=center_align_icon)
center_align_button.grid(row=0,column=7,padx=5)


#right align
right_align_icon = tk.PhotoImage(file=r'icons\align_right.png')
right_align_button = ttk.Button(toolbar, image=right_align_icon)
right_align_button.grid(row=0,column=8,padx=5)

#-------------------------------------Toolbar ending----------------------------------------------


#--------------------------------------Text editor------------------------------------------------
text_editor = tk.Text(main_application, undo=True)
text_editor.config(wrap = 'word' ,relief=tk.FLAT)
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#text editor font family and font size functions
current_font='Arial'
current_size= 12
text_editor.configure(font=('Arial',12))

#font Family function
def change_font(value=None):
    global current_font
    current_font = font_family.get()
    text_editor.configure(font=(current_font,current_size))

#font size function
def change_size(value=None):
    global current_size
    current_size = size.get()
    text_editor.configure(font=(current_font,current_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)


#-------buttons functionaity----------

#bold_button functions
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual().get('weight')=='normal':
       text_editor.configure(font=(current_font,current_size,'bold'))
    if text_property.actual().get('weight')=='bold':
       text_editor.configure(font=(current_font,current_size,'normal'))
bold_button.configure(command=change_bold)

#italic_button function
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual().get('slant')=='roman':
       text_editor.configure(font=(current_font,current_size,'italic'))
    if text_property.actual().get('slant')=='italic':
       text_editor.configure(font=(current_font,current_size,'roman'))
italic_button.configure(command=change_italic)


#underline button function
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual().get('underline')==0:
       text_editor.configure(font=(current_font,current_size,'underline'))
    if text_property.actual().get('underline')==1:
       text_editor.configure(font=(current_font,current_size,'normal'))
underline_button.configure(command=change_underline)

#font color function
def change_color():
    color_variable = tk.colorcCombobohooser.askcolor()
    text_editor.configure(fg=color_variable[1])

font_color_button.configure(command=change_color)

#left align button
def change_left_align():
    text_contant=text_editor.get(1.0,'end-1c')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0,'end-1c')
    text_editor.insert(tk.INSERT, text_contant, 'left')
left_align_button.configure(command=change_left_align)

#center align function
def change_center_align():
    text_contant=text_editor.get(1.0,'end-1c')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0,'end-1c')
    text_editor.insert(tk.INSERT, text_contant, 'center')
center_align_button.configure(command=change_center_align)


#right align function
def change_right_align():
    text_contant=text_editor.get(1.0,'end-1c')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0,'end-1c')
    text_editor.insert(tk.INSERT, text_contant, 'right')
right_align_button.configure(command=change_right_align)
    
    

#--------------------------------------End Text editor------------------------------------------------


#----------------------------------------Status bar ----------------------------------------------
status_bar = ttk.Label(main_application, text='Status bar')
status_bar.pack(side=tk.BOTTOM)

text_change = False

def change_status_value(value=None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        lines=len(text_editor.get(1.0,'end-1c').split('\n'))
        status_bar.config(text=f'Characters: {characters} Words: {words} Lines: {lines}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",change_status_value)



#----------------------------------------Status bar ----------------------------------------------


#--------------------------------------main menu functionality -------------------------------------

#variable for file
url=''


#file menu commands

#---new file function------
def new_file(value=None):
    global url
    try:
        if text_change:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the File')
            if mbox is True:
                if url:
                    content= str(text_editor.get(1.0,tk.END))
                    with open(url, 'w', encoding='utf-8') as fr:
                        fr.write(content)
                        url=''
                        text_editor.delete(1.0,tk.END)
                        main_application.title('S-Text Editor')
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    url=''
                    text_editor.delete(1.0,tk.END)
                    main_application.title('S-Text Editor')
            elif mbox is False:
                url=''
                text_editor.delete(1.0,tk.END)
                main_application.title('S-Text Editor')
            else:
                return
        else:
            url=''
            text_editor.delete(1.0,tk.END)
            main_application.title('S-Text Editor')
    except:
        return
    
    
file_menu.add_command(label='New File' , image=new_icon ,compound=tk.LEFT , accelerator='Ctrl+N',command=new_file)


#---open  file function --------
def open_file(value=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetype=(('Text Files','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
file_menu.add_command(label='Open File' ,image=open_icon , compound=tk.LEFT , accelerator='Ctrl+O',command=open_file)
file_menu.add_separator()

#---save file function
def save_file(value=None):
    global url
    try:
        if url:
            contant=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fr:
                fr.write(contant)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text Files','*.txt'),('All Files','*.*')))
            contant2=text_editor.get(1.0,tk.END)
            url.write(contant2)
            url.close()
    except:
        return
file_menu.add_command(label='Save File' ,image=save_icon , compound=tk.LEFT , accelerator='Ctrl+S',command=save_file)


#---save as function------
def saveas_file(value=None):
    global url
    try:
        contant=text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text Files','*.txt'),('All Files','*.*')))
        url.write(contant)
        url.close()
    except:
        return
        
file_menu.add_command(label='Save File As' ,image=save_as_icon , compound=tk.LEFT , accelerator='Ctrl+Alt+S', command=saveas_file)
file_menu.add_separator()

#---exit function-------
def exit_func(value=None):
    global url,text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the File')
            if mbox is True:
                if url:
                    content= str(text_editor.get(1.0,tk.END))
                    with open(url, 'w', encoding='utf-8') as fr:
                        fr.write(content)
                        main_application.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
            else:
                return
        else:
            main_application.destroy()
    except:
        return
                    
file_menu.add_command(label='Exit Application' ,image=exit_icon , compound=tk.LEFT , accelerator='Ctrl+Q',command=exit_func)


#edit menu commands

edit_menu.add_command(label='Copy', image=copy_icon ,compound=tk.LEFT ,accelerator='Ctrl+C',command=lambda : text_editor.event_generate("<Control c>"))
edit_menu.add_command(label='Paste', image=paste_icon ,compound=tk.LEFT ,accelerator='Ctrl+V',command=lambda : text_editor.event_generate("<Control v>"))
edit_menu.add_command(label='Cut', image=cut_icon ,compound=tk.LEFT ,accelerator='Ctrl+X',command=lambda : text_editor.event_generate("<Control x>"))
edit_menu.add_separator()

#----- find function ------------------
def find_func(value=None):

    def find():
        word = find_box.get()
        text_editor.tag_remove('match',1.0,tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
                find_dialouge.destroy()
    def replace():
        word = find_box.get()
        replace_word=replace_box.get()
        contant=str(text_editor.get(1.0,tk.END))
        replace_contant = contant.replace(word,replace_word)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,replace_contant)
    
    find_dialouge=tk.Toplevel()
    find_dialouge.geometry('450x200')
    find_dialouge.title('Find And Replace')
    find_dialouge.resizable(0,0)

    #lable frame of find
    find_frame=ttk.LabelFrame(find_dialouge, text='Find/Replace')
    find_frame.pack(pady=20)

    #lable
    find_label=ttk.Label(find_frame, text='Find')
    replace_label=ttk.Label(find_frame, text='Replace')

    #entry box
    find_box=ttk.Entry(find_frame, width=30)
    replace_box=ttk.Entry(find_frame, width=30)

    #button
    find_button = ttk.Button(find_frame, text='Find',command=find)
    replace_button = ttk.Button(find_frame, text='Replace',command=replace)

    #label and entry box _grid
    find_label.grid(row=0,column=0,padx=4,pady=4)
    replace_label.grid(row=1,column=0,padx=4,pady=4)
    find_box.grid(row=0,column=1,padx=4,pady=4)
    replace_box.grid(row=1,column=1,padx=4,pady=4)
    find_button.grid(row=2,column=0,padx=10,pady=4)
    replace_button.grid(row=2,column=1,padx=10,pady=4)

    find_dialouge.mainloop()
    
edit_menu.add_command(label='Find And Replace',image=find_icon, compound=tk.LEFT ,accelerator='Ctrl+F',command=find_func)
edit_menu.add_separator()
edit_menu.add_command(label='Undo',image=undo_icon, compound=tk.LEFT ,accelerator='Ctrl+Z',command=lambda : text_editor.event_generate("<Control z>"))
edit_menu.add_command(label='Redo',image=redo_icon, compound=tk.LEFT ,accelerator='Ctrl+Y',command=lambda : text_editor.event_generate("<Control y>"))
edit_menu.add_separator()
edit_menu.add_command(label='Clear All', image=clear_all_icon ,compound=tk.LEFT ,accelerator='Ctrl+Alt+C',command=lambda : text_editor.delete(1.0,tk.END))

#view menu command check button
#variable
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar= False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
        


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True
    

view_menu.add_checkbutton(label='View Tool Bar',onvalue=True,offvalue=False, \
                          variable=show_toolbar ,image=viwe_toolbar_icon,compound=tk.LEFT,command=hide_toolbar)
view_menu.add_separator()
view_menu.add_checkbutton(label='view Status Bar',onvalue=True,offvalue=False,\
                          variable=show_statusbar ,image=view_status_icon ,compound=tk.LEFT,command=hide_statusbar)


#color menu commands
def change_theme():
    choose = theme.get()
    color=color_dict.get(choose)
    fgcolor,bgcolor=color[0],color[1]
    text_editor.config(background=bgcolor,foreground=fgcolor)
count=0
for i in color_dict:
    color_menu.add_radiobutton(label = i , image=icons[count], variable=theme, compound=tk.LEFT,command=change_theme)
    if count<5 : color_menu.add_separator()
    count+=1

#help menu commands
def about():
    #dialouge box about
    about_dialouge=tk.Toplevel()
    about_dialouge.geometry('450x200')
    about_dialouge.title('About')
    about_dialouge.resizable(0,0)
    #frame inside anout dialouge box
    about_frame=ttk.LabelFrame(about_dialouge, text='About Author')
    about_frame.pack(pady=20)
    #labels 
    author_label= ttk.Label(about_frame, text='Author :')
    author_details= ttk.Label(about_frame, text='Anuj')
    version_lable= ttk.Label(about_frame, text='Version :')
    version_details=ttk.Label(about_frame, text='1.0')
    info_label=ttk.Label(about_frame, text='Info :')
    info_details=ttk.Label(about_frame, text='Simple text editor with some basic functions.\n You can use Diffrent themes for your text editor')
    #grid of labels
    author_label.grid(row=0,column=0,padx=5,pady=5)
    version_lable.grid(row=1,column=0,padx=5,pady=5)
    info_label.grid(row=2,column=0,padx=1,pady=5)
    author_details.grid(row=0,column=1,padx=5,pady=5)
    version_details.grid(row=1,column=1,padx=5,pady=5)
    info_details.grid(row=2,column=1,padx=4,pady=5)
    about_dialouge.mainloop()
help_menu.add_command(label='About S-Text Editor' ,command=about)


#--------------------------------------main menu functionality End-------------------------------------

main_application.config(menu=main_menu)

#bind shortcut
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", saveas_file)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)
main_application.bind("<Alt-F4>",exit_func)
main_application.mainloop()
