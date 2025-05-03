from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

ws = Tk()
ws.title('Python Guides')
ws.geometry('500x500')
#ws.eval('tk::PlaceWindow . center')
ws.resizable(0, 0)

ws.title("Interfaz Ajustes Salariales de Nomina SPI")

image = Image.open("icons8-payroll-64.png")
image_ = ImageTk.PhotoImage(image)
lbl_img = Label(ws, image = image_)
lbl_img.pack()

messagebox.showinfo(message='¡La Interfaz de Ajustes Salariales se Completo de forma Satisfactoria!')

ws.quit()
#ws.mainloop()