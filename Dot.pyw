from customtkinter import *
import playsound
import datetime
import pandas
from Scripts import funcs, shorten_doubt
from PIL import Image

app = CTk()
app.geometry("1500x500")
app.wm_title("Dot")
app.iconbitmap("Assets/icon/Dot_Icon.ico")
app._set_appearance_mode('light')
set_default_color_theme("blue")
btn_img = Image.open('Assets/Images/Dot_black.png')


def button_func():
    if Chapter.get() != '':
        if Doubt_box.get('0.0', 'end') != '':
            csv_old=pandas.read_csv('Assets/data/data.csv')
            data={"Date":[datetime.date.today()],
                "Chapter":[Chapter.get()],
                "Doubt":[(Doubt_box.get('0.0', 'end'))[:-1]],
                "Resolved": [0]} 
            csv_new=pandas.DataFrame(data)
            csv_combined = pandas.concat([csv_old, csv_new])
            csv_combined.to_csv('Assets/data/data.csv', index=False)
            csv_combined = pandas.read_csv('Assets/data/data.csv')
        else:
            CTkLabel(master=frame_1, text="Enter Doubt!!!", text_color='#b52309', font=('Commissioner', 17)).pack(pady=[0,10])
    else:
        CTkLabel(master=frame_1, text="Enter Chapter!!!", text_color='#b52309', font=('Commissioner', 17)).pack(pady=[0,10])
    Doubt_box.delete('0.0', 'end')
    playsound.playsound('Assets/sound/click.wav')

def resolved_button_func():
    for i in range(len(csv.index)):
        if csv['Date'][i] == str(funcs.daychange(0)) or csv['Date'][i] == str(funcs.daychange(-1)) or csv['Date'][i] == str(funcs.daychange(-2)) or csv['Date'][i] == str(funcs.daychange(-3)) or csv['Date'][i] == str(funcs.daychange(-4)) or csv['Date'][i] == str(funcs.daychange(-5)) or csv['Date'][i] == str(funcs.daychange(-6)):
            csv.loc[i, 'Resolved'] = [1]
            csv.to_csv('Assets/data/data.csv', index=False)
    playsound.playsound('Assets/sound/click.wav')

csv= pandas.read_csv('Assets/Data/data.csv')




frame_1 = CTkFrame(master=app, fg_color="#CB7DE3", border_width=5, corner_radius=50)
frame_1.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=50, pady=50)

study_head = CTkLabel(master=frame_1, text='DOUBTS? ENTER HERE!!!', text_color='#35173E', font=("Cascadia Mono SemiBold", 25), justify="center")
Chapter = CTkEntry(master=frame_1, placeholder_text="Enter Chapter",text_color='#FFFFFF', width=400, font=("Cascadia Mono", 15), fg_color="#9628B8", placeholder_text_color='#FFFFFF')
Doubt_box = CTkTextbox(master=frame_1,text_color='#FFFFFF', width=400, font=("Cascadia Mono", 15), fg_color="#9628B8", height=100, scrollbar_button_color='#FFFFFF')
button = CTkButton(master=frame_1, text="ADD", command=button_func, font=("Cascadia Mono", 15), fg_color='#8524A3', text_color='#FFFFFF', hover_color='#4B145C', image = CTkImage(light_image=btn_img, dark_image=btn_img))

study_head.pack(expand=False, pady=(30, 15), padx= 20)
Chapter.pack(expand=False, pady=15, padx=20)
Doubt_box.pack(expand=False, pady=15, padx=20)
button.pack(expand=False, fill="both", pady=(30, 15), padx=30)



frame_2 = CTkScrollableFrame(master=app, fg_color="#E090C6", border_width=5, corner_radius=30, width=700, height=200, scrollbar_button_color='#C93F9D')
frame_2.grid(row=0, column=1, pady=2, padx=5)

CTkLabel(master=frame_2, text="CLEAR THESE DOUBTS QUICKLY!!!", text_color='#C93F9D', font=("Cascadia Mono SemiBold", 25), justify="center").pack(expand=True, pady=5, padx=20)

dot_displayed=False
for i in range(len(csv.index)):
    if csv['Date'][i] == str(funcs.daychange(0)) or csv['Date'][i] == str(funcs.daychange(-1)) or csv['Date'][i] == str(funcs.daychange(-2)) or csv['Date'][i] == str(funcs.daychange(-3)) or csv['Date'][i] == str(funcs.daychange(-4)) or csv['Date'][i] == str(funcs.daychange(-5)) or csv['Date'][i] == str(funcs.daychange(-6)):
        if csv['Resolved'][i]==0:
            doubt = shorten_doubt.shorten_doubt(csv['Doubt'][i])
            doubt_check = CTkLabel(master=frame_2, text=f'➧{csv['Chapter'][i]} ⇛ {doubt}', text_color='#5E224B',font=("Cascadia Mono", 20))
            doubt_check.pack(expand=True, pady=5, padx=5)
            dot_displayed = True
if dot_displayed == False:
    doubt_check = CTkLabel(master=frame_2, text='NO DOUBTS LEFT UNRESOLVED', text_color='#5E224B',font=("Cascadia Mono", 20))
    doubt_check.pack(expand=True, pady=5, padx=5)
resolved_button = CTkButton(master=frame_2, text="Resolved", command=resolved_button_func, font=("Cascadia Mono", 15), fg_color='#7F2462', hover_color='#3E173D').pack(expand=True, padx=5, pady=[5,0])
app.mainloop()
