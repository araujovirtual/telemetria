from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk
import time
from graphics import *

root = Tk(className='Telemetria - Orion')
root.iconbitmap('images/pp.ico')
root.geometry("1045x680")

spacer1 = Label(root, text="")
spacer1.grid(row=4, column=0)
spacer1.pack()

srcImage = ImageTk.PhotoImage(Image.open("images/pp.jfif"))
myImage = Label(image= srcImage)
myImage.pack()

spacer2 = Label(root, text="")
spacer2.pack()

myLabel = Label(root, text="Upload de Arquivos telemetria")
myLabel.pack()
myLabel.config(font=("Courier", 24))

myProgress = ttk.Progressbar(root, orient=HORIZONTAL, length= 300, mode="determinate")

def loading():
  myProgress.pack(pady=10)
  myProgress.start(10)

def stopLoading():
  myProgress.pack_forget()
  myProgress.stop()


def open():
  loading()
  global myFile
  root.filename = filedialog.askopenfilename(initialdir="C:/Users/Public/Downloads",title="Selecione o arquivo de telemetria",filetypes=(("text files", ".txt"),("All files", "*.*")))
  fileNameLabel = Label(root, text=root.filename).pack()
  parserFile(root.filename)
  stopLoading()


btn = Button(root, text="escolher Arquivo", command=open).pack()

root.mainloop()