from Tkinter import *

win = Tk()
win.title('TagCloud')
input_text = StringVar()

entry = Entry(win, textvariable=input_text)
entry.pack(fill='x', expand=True)

output = Label(win)
output.pack(fill='both', expand=True)

def update_output(*args):
  d = ' | '.join(input_text.get().split())
  output.config(text=d)

input_text.trace_variable('w', update_output)

win.mainloop()