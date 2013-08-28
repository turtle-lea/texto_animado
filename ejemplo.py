#! usr/bin/python

from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
	self.historial = []
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Misterious space")
        self.pack(fill=BOTH, expand=1)
        
        Style().configure("TFrame", background="#333")
        
              
    def mostrarImagen(self,filename,offset):
		
        bard = Image.open(filename)
        bardejov = ImageTk.PhotoImage(bard)
	ancho_total = sum([x.image.width()+1 for x in self.historial])
        label1 = Label(self,image=bardejov)
        label1.image = bardejov
        label1.place(x=ancho_total, y=20)
	self.historial.append(label1)

    def borrarHistorial(self):
	for x in self.historial:
		x.destroy()
	self.historial= []
	

