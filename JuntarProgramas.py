import os
from tkinter import *
from tkinter.font import Font
import time
#Para crear una nueva ventana, usar toplevel

def main():
    link = entradaLink.get()
    autor = entradaAuthor.get()
    entradaAuthor.delete(0,"end")
    entradaLink.delete(0,"end")
    ejecutar = 'python DescargarArchivos.py ' + '"' + link + '" ' + '"' + autor + '"'
    os.system(ejecutar)
    os.system('python DelateVideos.py')

def agregarAutor():
    print("hOla")

def verCanciones():
    os.system("notepad Canciones.csv")
    botonVerCanciones.config(state="disabled")
root = Tk()
root.configure(bg='#F98E8E')
root.resizable(0,0)
root.title("Descargador de música")
yt_font = Font(family="Roboto Cn", size=14, weight= 'bold') 


titulo = Label(root, text = "YOUTUBE", font = yt_font, fg = "#CD0707", bg = "#F79085")

titulo.grid(row = 0, column = 0, sticky=E+W, columnspan= 5)
labelLink = Label(root, text = "Link", width = 10)
labelLink.grid(row = 1, column = 1)
entradaLink = Entry(root, width = 30)
entradaLink.grid(row = 1, column = 2)

labelAgra = Label(root, text = "Hecho por Iñaki Frutos\n Agradecimientos a pytube y tkinter")
labelAgra.grid(row = 1, column = 0, rowspan = 2)

labelAuthor = Label(root, text = "Autor", width = 10)
labelAuthor.grid(row = 2, column = 1)
entradaAuthor = Entry(root, width = 30)
entradaAuthor.grid(row = 2, column = 2)

botonActivar = Button(root, text = "Descargar música", command = main, height= 3, bg = "#D51010")
botonActivar.grid(column = 4, row = 1, rowspan = 2)

botonSalir = Button(root, text = "Salir", command = root.quit)
botonSalir.grid(column = 2, row = 3, columnspan = 2)

botonAgregarAutor = Button(root, text = "Agregar autor", command = agregarAutor)
botonAgregarAutor.grid(column = 1, row = 3)

botonVerCanciones = Button(root, text = "Ver canciones", command = verCanciones)
botonVerCanciones.grid(column = 0, row = 3)

root.mainloop()