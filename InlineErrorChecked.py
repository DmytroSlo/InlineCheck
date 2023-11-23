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
new_product.add_radiobutton(label="P21 | 3 minut", variable=p_var, value=0, command=bd.timeP21)
new_product.add_radiobutton(label="P0   | 5 minut", variable=p_var, value=1, command=bd.timeP0)
new_product.add_radiobutton(label="P15 | 7 minut", variable=p_var, value=2, command=bd.timeP15)
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
    # bd.result_time()

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

#Pausa Inline 1
def pause1():
    global marker1
    if button1_checked.get():
        button1_checked.set(0)
        marker1 = False
        image_pause = Image.open("picture/Inline1Good.png")
        photo_pause = ImageTk.PhotoImage(image_pause)
        button1.config(image=photo_pause)
        button1.image = photo_pause
    else:
        button1_checked.set(1)
        marker1 = True
        image_pause = Image.open("picture/Inline1Pause.png")
        photo_pause = ImageTk.PhotoImage(image_pause)
        button1.config(image=photo_pause)
        button1.image = photo_pause

button1_checked = IntVar()

#Pausa Inline 2
def pause2():
    global marker2
    if button2_checked.get():
        button2_checked.set(0)
        marker2 = False
        image_pause = Image.open("picture/Inline2Good.png")
        photo_pause = ImageTk.PhotoImage(image_pause)
        button2.config(image=photo_pause)
        button2.image = photo_pause
    else:
        button2_checked.set(1)
        marker2 = True
        image_pause = Image.open("picture/Inline2Pause.png")
        photo_pause = ImageTk.PhotoImage(image_pause)
        button2.config(image=photo_pause)
        button2.image = photo_pause

button2_checked = IntVar()

#Pausa Inline 3
def pause3():
    global marker3
    if button3_checked.get():
        button3_checked.set(0)
        marker3 = False
        image_pause = Image.open("picture/Inline3Good.png")
        photo_pause = ImageTk.PhotoImage(image_pause)
        button3.config(image=photo_pause)
        button3.image = photo_pause
    else:
        button3_checked.set(1)
        marker3 = True
        image_pause = Image.open("picture/Inline3Pause.png")
        photo_pause = ImageTk.PhotoImage(image_pause)
        button3.config(image=photo_pause)
        button3.image = photo_pause

button3_checked = IntVar()

def kolor():
    time_result1, time_result2, time_result3 = bd.tenminutago()
    tester_fail1, tester_fail2, tester_fail3 = False, False, False

    if marker1 == True:
        image1 = Image.open("picture/Inline1Pause.png")

    if time_result1 == True and marker1 == False:
        image1 = Image.open("picture/Inline1Good.png")

    if time_result1 == False and marker1 == False:
        image1 = Image.open("picture/Inline1Bad.png")
        tester_fail1 = True

    if marker2 == True:
        image2 = Image.open("picture/Inline2Pause.png")

    if time_result2 == True and marker2 == False:
        image2 = Image.open("picture/Inline2Good.png")

    if time_result2 == False and marker2 == False:
        image2 = Image.open("picture/Inline2Bad.png")
        tester_fail2 = True

    if marker3 == True:
        image3 = Image.open("picture/Inline3Pause.png")

    if time_result3 == True and marker3 == False:
        image3 = Image.open("picture/Inline3Good.png")
        tester_fail3 = False

    if time_result3 == False and marker3 == False:
        image3 = Image.open("picture/Inline3Bad.png")
        tester_fail3 = True

    photo1 = ImageTk.PhotoImage(image1)
    photo2 = ImageTk.PhotoImage(image2)
    photo3 = ImageTk.PhotoImage(image3)

    button1.config(image=photo1)
    button2.config(image=photo2)
    button3.config(image=photo3)

    # Zaktualizuj etykiety w oknie Tkinter z nowymi obrazami
    button1.image = photo1
    button2.image = photo2
    button3.image = photo3

    if marker1 == False and tester_fail1 == True:
        msgbox.warning_info1()

    if marker2 == False and tester_fail2 == True:
        msgbox.warning_info2()

    if marker3 == False and tester_fail3 == True:
        msgbox.warning_info3()

    window.after(60000, kolor)

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