from Tkinter import *
from dameImagen import *
from ejemplo import *
from ttk import *

win = Tk()
	win.title('TagCloud')
	app = Example(win)
	input_text = StringVar()
	prov = ImageProvider()

entry = Entry(win, textvariable=input_text)
	entry.pack(fill='x', expand=True)

output = Label(win)
	output.pack(fill='both', expand=True)

	def update_output(*args):
	app.borrarHistorial()
	d = input_text.get().split()
	l = [prov.imageFor(i) for i in d]
	for i in range(len(l)):
	app.mostrarImagen(l[i],i)
	output.config(text=l)

	input_text.trace_variable('w', update_output)

win.mainloop()
