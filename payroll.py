# -*- coding: utf-8 -*-
from tkinter import Tk, Label, Button, RIGHT, LEFT, PhotoImage, HORIZONTAL, StringVar
from tkinter.ttk import *
import time
from PIL import Image, ImageTk
import subprocess


def button_confirm():
    """
    runs the interface

    """
    try:
        task = 10
        x = 0
        while x < task:
            time.sleep(1)
            progress_bar['value'] += 10
            x += 1
            percent.set(
                str(int((x / task) * 100)) + "% Iniciando Interfaz. Por Favor, Espere Hasta Que El Proceso Termine.")
            WindowFrame.update_idletasks()

        completed_process = subprocess.run('python payroll_b.py')
        print(completed_process)

    except:
        print("An error has occurred in payroll_b")
    else:
        print("Successful execution of payroll_b")

    WindowFrame.quit()


def button_cancel():
    """
    Cancel process and exit...

    """
    WindowFrame.quit()


WindowFrame = Tk()
WindowFrame.geometry('500x500')
# WindowFrame.eval('tk::PlaceWindow . center')
WindowFrame.title("Interfaz Ajustes Salariales de Nomina SPI")

lbl = Label(WindowFrame, text='¿Desea Confirmar la Ejecucion del Proceso?')
lbl.config(font=('Arial)', 10))
lbl.pack()

# Progress bar ...
percent = StringVar()
progress_bar = Progressbar(WindowFrame, orient=HORIZONTAL, length=300, mode="determinate")
progress_bar.pack(pady=20)

Label(WindowFrame, textvariable=percent).pack()

image = Image.open("icons8-payroll-64.png")
image_ = ImageTk.PhotoImage(image)
lbl_img = Label(WindowFrame, image=image_)
lbl_img.pack()

but1 = Button(WindowFrame, text='      OK           ', command=button_confirm)
but1.pack(side=LEFT, padx=15, pady=20)
but1.pack()

but2 = Button(WindowFrame, text='    Cancel     ', command=button_cancel)
but2.pack(side=RIGHT, padx=15, pady=20)
but2.pack()

# WindowFrame.config(bg='#ce9dd4')
WindowFrame.resizable(0, 0)
WindowFrame.mainloop()
