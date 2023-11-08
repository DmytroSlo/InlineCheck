from tkinter import messagebox as mb

def show_info():
    msg = ("Wersja: 1.0.1\n"
           "Autor: Dmytro Slobodian & Kamil Jankowski\n"
           "Special for Kitron©")
    mb.showinfo("Info", msg)

def warning_info1():
    msg = "Sprawdz Inline 1!"
    mb.showwarning("Awaria!", msg)

def warning_info2():
    msg = "Sprawdz Inline 2!"
    mb.showwarning("Awaria!", msg)

def warning_info3():
    msg = "Sprawdz Inline 3!"
    mb.showwarning("Awaria!", msg)