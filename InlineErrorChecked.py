from tkinter import *
from PIL import Image, ImageTk

import tkinter as tk
import msgbox
import server as bd

import server

#window
window = Tk()
window.title("Inline Check Error")
window.geometry("400x180")
window.resizable(width=False, height=False)
window.iconbitmap(r"picture/logo.ico")

#block
frame_add_info = tk.Frame(window, width=400, height=105)
frame_add_data = tk.Frame(window, width=400, height=80)

frame_add_info.pack()
frame_add_data.pack()

#Blokowanie okna
def block():
    window.attributes("-topmost", True)
block()

#flaga PRODUCT
p_var = BooleanVar()
p_var.set(0)

#menu
menu = Menu(window)
new_info = Menu(menu, tearoff=0)
new_info.add_command(label='Info', command=msgbox.show_info)
new_info.add_separator()

menu.add_cascade(label = 'File', menu = new_info)
window.config(menu = menu)

product = Menu(window)
new_product = Menu(menu, tearoff=0)
new_product.add_radiobutton(label="P21 | 4 minut", variable=p_var, value=0, command=bd.timeP21)
new_product.add_radiobutton(label="P0   | 6 minut", variable=p_var, value=1, command=bd.timeP0)
new_product.add_radiobutton(label="P15 | 8 minut", variable=p_var, value=2, command=bd.timeP15)
new_product.add_separator()

menu.add_cascade(label="Product", menu=new_product)
window.config(menu=menu)

def refresh_data():
    local_time1, local_time2, local_time3 = bd.get_data()

    local_time1_label = local_time1.strftime("%Y-%m-%d %H:%M:%S")
    local_time2_label = local_time2.strftime("%Y-%m-%d %H:%M:%S")
    local_time3_label = local_time3.strftime("%Y-%m-%d %H:%M:%S")

    # Zaktualizuj etykiety w oknie Tkinter z nowymi danymi
    lastTest1SQL.config(text=local_time1_label)
    lastTest2SQL.config(text=local_time2_label)
    lastTest3SQL.config(text=local_time3_label)
    bd.tenminutago()

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

marker1 = False
marker2 = False
marker3 = False

def good_picture_1():
    image_pause = Image.open("picture/Inline1Good.png")
    photo_pause = ImageTk.PhotoImage(image_pause)
    button1.config(image=photo_pause)
    button1.image = photo_pause

def good_picture_2():
    image_pause = Image.open("picture/Inline2Good.png")
    photo_pause = ImageTk.PhotoImage(image_pause)
    button2.config(image=photo_pause)
    button2.image = photo_pause

def good_picture_3():
    image_pause = Image.open("picture/Inline3Good.png")
    photo_pause = ImageTk.PhotoImage(image_pause)
    button3.config(image=photo_pause)
    button3.image = photo_pause

def bad_picture_1():
    image_pause = Image.open("picture/Inline1Bad.png")
    photo_pause = ImageTk.PhotoImage(image_pause)
    button1.config(image=photo_pause)
    button1.image = photo_pause

def bad_picture_2():
    image_pause = Image.open("picture/Inline2Bad.png")
    photo_pause = ImageTk.PhotoImage(image_pause)
    button2.config(image=photo_pause)
    button2.image = photo_pause

def bad_picture_3():
    image_pause = Image.open("picture/Inline3Bad.png")
    photo_pause = ImageTk.PhotoImage(image_pause)
    button3.config(image=photo_pause)
    button3.image = photo_pause

def pause_picture_1():
    image_pause = Image.open("picture/Inline1Pause.png")
    photo_pause = ImageTk.PhotoImage(image_pause)
    button1.config(image=photo_pause)
    button1.image = photo_pause

def pause_picture_2():
    image_pause = Image.open("picture/Inline2Pause.png")
    photo_pause = ImageTk.PhotoImage(image_pause)
    button2.config(image=photo_pause)
    button2.image = photo_pause

def pause_picture_3():
    image_pause = Image.open("picture/Inline3Pause.png")
    photo_pause = ImageTk.PhotoImage(image_pause)
    button3.config(image=photo_pause)
    button3.image = photo_pause

tester_fail1, tester_fail2, tester_fail3 = False, False, False

#Pausa Inline 1
def pause1():
    global marker1
    global tester_fail1

    if button1_checked.get():
        button1_checked.set(0)
        marker1 = False
        if tester_fail1 is False:
            good_picture_1()
        else:
            bad_picture_1()
    else:
        button1_checked.set(1)
        marker1 = True
        pause_picture_1()

button1_checked = IntVar()

#Pausa Inline 2
def pause2():
    global marker2
    global tester_fail2

    if button2_checked.get():
        button2_checked.set(0)
        marker2 = False
        if tester_fail2 is False:
            good_picture_2()
        else:
            bad_picture_2()
    else:
        button2_checked.set(1)
        marker2 = True
        pause_picture_2()

button2_checked = IntVar()

#Pausa Inline 3
def pause3():
    global marker3
    global tester_fail3

    if button3_checked.get():
        button3_checked.set(0)
        marker3 = False
        if tester_fail3 is False:
            good_picture_3()
        else:
            bad_picture_3()
    else:
        button3_checked.set(1)
        marker3 = True
        pause_picture_3()

button3_checked = IntVar()

def kolor():
    time_result1, time_result2, time_result3 = bd.tenminutago()

    global tester_fail1, tester_fail2, tester_fail3

    if marker1 is True:
        pause_picture_1()
    if time_result1 is True and marker1 is False:
        good_picture_1()
        tester_fail1 = False
    if time_result1 is False and marker1 is False:
        bad_picture_1()
        tester_fail1 = True


    if marker2 is True:
        pause_picture_2()
    if time_result2 is True and marker2 is False:
        good_picture_2()
        tester_fail2 = False
    if time_result2 is False and marker2 is False:
        bad_picture_2()
        tester_fail2 = True

    if marker3 is True:
        pause_picture_3()
    if time_result3 is True and marker3 is False:
        good_picture_3()
        tester_fail3 = False
    if time_result3 is False and marker3 is False:
        bad_picture_3()
        tester_fail3 = True

    if marker1 is False and tester_fail1 is True:
        msgbox.warning_info1()

    if marker2 is False and tester_fail2 is True:
        msgbox.warning_info2()

    if marker3 is False and tester_fail3 is True:
        msgbox.warning_info3()

    window.after(60000, kolor)

    return tester_fail1, tester_fail2, tester_fail3

# Utwórz etykiety, ale bez przypisanych obrazów, które zostaną ustawione w funkcji kolor()
button1 = Button(frame_add_info, command=pause1, bd=0)
button1.pack()
button1.place(x=10, y=0)

button2 = Button(frame_add_info, command=pause2, bd=0)
button2.pack()
button2.place(x=150, y=0)

button3 = Button(frame_add_info, command=pause3, bd=0)
button3.pack()
button3.place(x=280, y=0)

kolor()

server.get_data()

window.mainloop()