from Tkinter import *
from ScrolledText import *
from dameImagen import *
from ejemplo import *
from ttk import *

win = Tk()
w, h = win.winfo_screenwidth(), win.winfo_screenheight()
win.geometry("%dx%d+0+0" % (w, h))

win.title('TagCloud')
app = Example(win)
prov = ImageProvider()

entry = Text(win, height=3, highlightbackground="red")
entry.pack(fill='x', expand=False, anchor = "n")


def update_output(*args):
	app.borrarHistorial()
	d = entry.get(1.0, END).split()
	l = [prov.imageFor(i) for i in d]
	for i in range(len(l)):
		app.mostrarImagen(l[i],i)

entry.bind("<KeyPress>", update_output)

win.mainloop()
