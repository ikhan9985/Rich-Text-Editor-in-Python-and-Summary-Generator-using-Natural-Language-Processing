import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
from collections import Counter 
from string import punctuation
from sklearn.feature_extraction._stop_words import ENGLISH_STOP_WORDS as stop_words






main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('BUIC Text Editor')

################################### Main Menu #############################################

main_menu = tk.Menu()

#variables assignment 
file = tk.Menu(main_menu,tearoff=False)
edit = tk.Menu(main_menu,tearoff=False)
view = tk.Menu(main_menu,tearoff=False)
bg_theme = tk.Menu(main_menu,tearoff=False)

#if we didn't use tearoff=false then list will be out from the Application e.g open in small new window


#cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Background Theme', menu=bg_theme)


#1- File

#file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')




#2- Edit

#edit icons 
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')




#3- View

#edit icons 
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')



#4- Background Theme

#bg_theme icons 
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')


theme_choice = tk.StringVar() 
#StringVar use for to store multiple variables

color_icons = (light_default_icon, light_plus_icon, dark_icon,red_icon, monokai_icon, night_blue_icon) #tuple

color_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Pink' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
}

#--------------------------&&&&&&&& End Main Menu &&&&&&&&&&&&&&&&&&&&&&-------------------

################################### Toolbar ###############################################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X) 

#1- Fontbox
font_tuple = tk.font.families()
font_family = tk.StringVar() #user jo select karega woh yaha jayega
font_box = ttk.Combobox(tool_bar, width = 30, textvariable=font_family, state="readonly")
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)


#2- Sizebox
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=30, textvariable=size_var, state="readonly")
font_size['values'] = tuple(range(8,73,2))
font_size.current(2)  # 2 is index
font_size.grid(row=0, column =1, padx=5)

#3- Bold Button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

#4- Italic Button
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

#5- Underline Button
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

#6- Font Color Button
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)


#7- Align Left Button
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

#8- Align Center Button
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

#9- Align Right Button
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

#10- Summary Button
sum_icon = tk.PhotoImage(file='icons2/sum.png')
sum_btn = ttk.Button(tool_bar, image=sum_icon)
sum_btn.grid(row=0, column=9, padx=5)





#--------------------------&&&&&&&& End Toolbar &&&&&&&&&&&&&&&&&&&&&&---------------------



################################### Text Editor #############################################


text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

###############font-family and font-size functionality

current_font_family = 'Arial'
current_font_size = 12

def change_fontfamily(Event=None):
    global current_font_family
    current_font_family = font_family.get() #font_family is String var variable initialize in toolbox 1-FontBox
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(Event=None):
    global current_font_size
    current_font_size = size_var.get() #size_var is Int var variable initialize in toolbox 2-SizeBox
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>", change_fontfamily)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

text_editor.configure(font=('Arial',12))



################# Buttons Functionality

# bold button functionality

def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size, 'normal'))

bold_btn.configure(command=change_bold)  #calling change_bold() function


# italic button functionality

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size, 'normal'))

italic_btn.configure(command=change_italic)  #calling change_italic() function


# underline button functionality

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size, 'normal'))

underline_btn.configure(command=change_underline)  #calling change_underline() function


# font color button functionality

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    #print(color_var) 
    #((126.4921875, 194.7578125, 184.71875), '#7ec2b8') // tuple within tuple, ((R,G,B), Hexa)
    text_editor.configure(fg=color_var[1])
    
font_color_btn.configure(command=change_font_color)  #calling change_font_color() function

# alignment functionality

#left
def align_left_func():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content, 'left')

align_left_btn.configure(command=align_left_func)

#center
def align_center_func():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content, 'center')

align_center_btn.configure(command=align_center_func)

#right
def align_right_func():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content, 'right')

align_right_btn.configure(command=align_right_func)

#Summarize

def sum_func():
    text_content = text_editor.get(1.0, 'end')
    text = text_editor.get(1.0, 'end')
    def tokenizer(s):
        tokens = []
        for word in s.split(' '):
            tokens.append(word.strip().lower())
        return tokens

    def sent_tokenizer(s):
        sents = []
        for sent in s.split('.'):
            sents.append(sent.strip())
        return sents
    tokens = tokenizer(text)
    sents = sent_tokenizer(text)
    def count_words(tokens):
        word_counts = {}
        for token in tokens:
            if token not in stop_words and token not in punctuation:
                if token not in word_counts.keys():
                    word_counts[token] = 1
                else:
                    word_counts[token] += 1
        return word_counts

    word_counts = count_words(tokens)

    def word_freq_distribution(word_counts):
        freq_dist = {}
        max_freq = max(word_counts.values())
        for word in word_counts.keys():  
            freq_dist[word] = (word_counts[word]/max_freq)
        return freq_dist

    freq_dist = word_freq_distribution(word_counts)

    def score_sentences(sents, freq_dist, max_len=40):
        sent_scores = {}  
        for sent in sents:
            words = sent.split(' ')
            for word in words:
                if word.lower() in freq_dist.keys():
                    if len(words) < max_len:
                        if sent not in sent_scores.keys():
                            sent_scores[sent] = freq_dist[word.lower()]
                        else:
                            sent_scores[sent] += freq_dist[word.lower()]
        return sent_scores

    sent_scores = score_sentences(sents, freq_dist)

    def summarize(sent_scores, k):
        top_sents = Counter(sent_scores) 
        summary = ''
        scores = []
        
        top = top_sents.most_common(k)
        for t in top: 
            summary += t[0].strip()+'. '
            scores.append((t[1], t[0]))
        return summary[:-1], scores

    summary, summary_sent_scores = summarize(sent_scores, 3)
    sum_box = tk.Toplevel()
    sum_box.geometry('600x400+500+200')
    sum_box.title('Summary Generator')
    
    text_editor_box = tk.Text(sum_box)
    text_editor_box.config(wrap='word', relief=tk.FLAT)

    scroll_bar_box = tk.Scrollbar(sum_box)
    text_editor_box.focus_set()
    scroll_bar_box.pack(side=tk.RIGHT, fill=tk.Y)
    text_editor_box.pack(fill=tk.BOTH, expand=True)
    scroll_bar_box.config(command=text_editor.yview)
    text_editor_box.config(yscrollcommand=scroll_bar.set)
    text_editor_box.insert(tk.INSERT,summary, 'center')
    sum_box.mainloop()
    

    

sum_btn.configure(command=sum_func)

#--------------------------&&&&&&&& End Text Editor &&&&&&&&&&&&&&&&&&&&&&-------------------



################################### Status Bar #############################################

status_bar = ttk.Label(main_application,text = 'Status Bar')
status_bar.pack(side= tk.BOTTOM)


text_changed = False
def changeStatusBar(event=None):
    global text_changed
    if(text_editor.edit_modified()):
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        chars = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Words: {words} Characters: {chars}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changeStatusBar)




#--------------------------&&&&&&&& End Status Bar &&&&&&&&&&&&&&&&&&&&&&-------------------



################################### Main Menu Functionality #################################

#variable 
path = ''



#New Functionality
def new_func(Event=None):
    global path
    path = ''
    text_editor.delete(1.0,tk.END)

#Open Functionality
def open_func(Event=None):
    global path
    path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes= (('Text File', '*.txt'),('All Files', '*.*')))
    try:
        with open(path,'r') as ff:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, ff.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(path))

#Save Functionality
def save_func(Event=None):
    global path
    try:
        if path:
            cont = str(text_editor.get(1.0, tk.END))
            with open(path, 'w', encoding='utf-8') as ff:
                ff.write(cont)
        else:
            path = filedialog.asksaveasfile(mode="w", defaultextension='.txt', filetypes= (('Text File', '*.txt'),('All Files', '*.*')))
            cont2 = text_editor.get(1.0, tk.END)
            path.write(cont2)
            path.close()
    except:
        return

#Save As Functionality
def saveas_func(Event=None):
    global path
    try:
        cont = text_editor.get(1.0, tk.END)
        path = filedialog.asksaveasfile(mode="w", defaultextension='.txt', filetypes= (('Text File', '*.txt'),('All Files', '*.*')))
        path.write(cont)
        path.close()      
    except:
        return

#Exit Functionality

def exit_func(Event=None):
    global text_changed, path
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?') # messagebox library of tkinter like filedialog
            if mbox is True:
                if path:
                    cont = text_editor.get(1.0, tk.END)
                    with open(path, 'w', encoding="utf-8") as fw:
                        fw.write(cont)
                        main_application.destroy() #important line for use in any project
                else:
                    cont2 =  str(text_editor.get(1.0, tk.END)) 
                    path = filedialog.asksaveasfile(mode="w", defaultextension='.txt', filetypes= (('Text File', '*.txt'),('All Files', '*.*')))
                    path.write(cont2)
                    path.close()      
                    main_application.destroy()

            elif mbox is False:
                main_application.destroy()
        
        else:
            main_application.destroy() 
        
    except:
        return


#1- File Commands

file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N", command=new_func )
file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O", command=open_func )
file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S", command=save_func )
file.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S", command=saveas_func )
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q", command=exit_func)

#----------------------------------------------------------------------------------------------------------#

#Find Functionality

def find_func(Event=None):

    def find(Event=None):

        word = find_input.get()
        text_editor.tag_remove('match','1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace(Event=None):
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)


    find_box = tk.Toplevel()
    find_box.geometry('400x200+500+200')
    find_box.title('Find')
    find_box.resizable(0,0) #dubara isko minimize maximize na karsaku

    #frame
    find_frame = ttk.LabelFrame(find_box, text="Find/Replace")
    find_frame.pack(pady=20)

    #labels
    text_find_label = ttk.Label(find_frame, text='Find: ')
    text_replace_label = ttk.Label(find_frame, text='Replace: ')

    #entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    #buttons
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    #label_grids
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    #entry_grids
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    #button_grids
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_box.mainloop()



#2- Edit Commands
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C", command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V", command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X" , command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+X" , command=lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F", command=find_func)

#----------------------------------------------------------------------------------------------------------#



#3- View Commands
show_statusbar = tk.BooleanVar()
show_toolbar = tk.BooleanVar()

show_statusbar.set(True)
show_toolbar.set(True)

def hide_toolbar(Event=None):
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar(Event=None):
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=0, variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False, variable=show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)

#----------------------------------------------------------------------------------------------------------#
#4- Background Theme

def change_theme(Event=None):
    choosen_theme = theme_choice.get()
    color_tuple = color_dict.get(choosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)


count=0
for i in color_dict:
    bg_theme.add_radiobutton(label=i, image=color_icons[count], compound=tk.LEFT, variable=theme_choice, command=change_theme)
    count+=1


#---------------------&&&&&&&& End Main Menu Functionality &&&&&&&&&&&&&&&&&&----------------


main_application.config(menu=main_menu)


#Shortcut Keys Binding
main_application.bind("<Control-n>", new_func)
main_application.bind("<Control-o>", open_func)
main_application.bind("<Control-s>", save_func)
main_application.bind("<Control-Alt-s>", saveas_func)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)


main_application.mainloop()



