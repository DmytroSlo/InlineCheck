from tkinter import *
from PIL import Image, ImageTk

import tkinter as tk
import os
import msgbox
import server as bd

import server

#window
window = Tk()
window.title("Inline Check Error")
window.geometry("400x180")
window.resizable(width=False, height=False)

#block
frame_add_info = tk.Frame(window, width=400, height=105)
frame_add_data = tk.Frame(window, width=400, height=80)

frame_add_info.pack()
frame_add_data.pack()

#refresh
def refresh():
    window.destroy()
    os.popen("bgaplication.py")

#Blokowanie okna
def block():
    window.attributes("-topmost", True)
block()

paused = False

def stop():
    global paused
    paused = True

def start():
    global paused
    paused = False

#flaga PAUSE\RESUNE
r_var = BooleanVar()
r_var.set(0)

#flaga PRODUCT
p_var = BooleanVar()
p_var.set(0)

#menu
menu = Menu(window)
new_info = Menu(menu, tearoff=0)
new_info.add_command(label='Info', command=msgbox.show_info)
new_info.add_separator()
new_info.add_command(label='Restart', command=refresh)
new_info.add_separator()
new_info.add_radiobutton(label='Pause', variable=r_var, value=1, command=stop)
new_info.add_radiobutton(label='Resume', variable=r_var, value=0, command=start)
new_info.add_separator()

menu.add_cascade(label = 'File', menu = new_info)
window.config(menu = menu)

product = Menu(window)
new_product = Menu(menu, tearoff=0)
new_product.add_radiobutton(label="P21 | 3 minut", variable=p_var, value=0, command=bd.timeP21)
new_product.add_radiobutton(label="P0   | 5 minut", variable=p_var, value=1, command=bd.timeP0)
new_product.add_radiobutton(label="P15 | 7 minut", variable=p_var, value=2, command=bd.timeP15)

menu.add_cascade(label="Product", menu=new_product)
window.config(menu=menu)

def refresh_data():
    time_value1, time_value2, time_value3 = bd.get_data()

    # Zaktualizuj etykiety w oknie Tkinter z nowymi danymi
    lastTest1SQL.config(text=time_value1)
    lastTest2SQL.config(text=time_value2)
    lastTest3SQL.config(text=time_value3)
    bd.tenminutago()
    bd.result_time()

    # Planuj ponowne wywołanie funkcji po np. 10 sekundach
    window.after(60000, refresh_data)

#wpisy ostatniego testu
lastTest1 = Label(frame_add_data, text = "Ostatni test:", font=("Sylfaen", 10))
lastTest1.pack()
lastTest1.place(x=30, y=10)

lastTest1SQL = Label(frame_add_data, font=("Sylfaen", 10))
lastTest1SQL.pack()
lastTest1SQL.place(x=10, y=30)

lastTest2 = Label(frame_add_data, text = "Ostatni test:", font=("Sylfaen", 10))
lastTest2.pack()
lastTest2.place(x=160, y=10)

lastTest2SQL = Label(frame_add_data, font=("Sylfaen", 10))
lastTest2SQL.pack()
lastTest2SQL.place(x=140, y=30)

lastTest3 = Label(frame_add_data, text = "Ostatni test:", font=("Sylfaen", 10))
lastTest3.pack()
lastTest3.place(x=290, y=10)

lastTest3SQL = Label(frame_add_data, font=("Sylfaen", 10))
lastTest3SQL.pack()
lastTest3SQL.place(x=270, y=30)
refresh_data()

def kolor():
    time_boolen1, time_boolen2, time_boolen3 = bd.result_time()

    tester_fail1, tester_fail2, tester_fail3 = False, False, False

    if time_boolen1 == False:
        image1 = Image.open("picture/Inline1Good.png")
    else:
        image1 = Image.open("picture/Inline1Bad.png")
        tester_fail1 = True

    if time_boolen2 == False:
        image2 = Image.open("picture/Inline2Good.png")
    else:
        image2 = Image.open("picture/Inline2Bad.png")
        tester_fail2 = True

    if time_boolen3 == False:
        image3 = Image.open("picture/Inline3Good.png")
        tester_fail3 = False
    else:
        image3 = Image.open("picture/Inline3Bad.png")
        tester_fail3 = True

    photo1 = ImageTk.PhotoImage(image1)
    photo2 = ImageTk.PhotoImage(image2)
    photo3 = ImageTk.PhotoImage(image3)

    label1.config(image=photo1)
    label2.config(image=photo2)
    label3.config(image=photo3)

    # Zaktualizuj etykiety w oknie Tkinter z nowymi obrazami
    label1.image = photo1
    label2.image = photo2
    label3.image = photo3

    if paused == False and tester_fail1 == True:
        msgbox.warning_info1()

    if paused == False and tester_fail2 == True:
        msgbox.warning_info2()

    if paused == False and tester_fail3 == True:
        msgbox.warning_info3()

    window.after(30000, kolor)

# Utwórz etykiety, ale bez przypisanych obrazów, które zostaną ustawione w funkcji kolor()
label1 = tk.Label(frame_add_info)
label1.pack()
label1.place(x=10, y=0)

label2 = tk.Label(frame_add_info)
label2.pack()
label2.place(x=150, y=0)

label3 = tk.Label(frame_add_info)
label3.pack()
label3.place(x=280, y=0)

kolor()

server.get_data()

window.mainloop()