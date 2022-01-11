import tkinter as tk
from tkinter import ttk

def begin():
  print('出勤', variable.get())
  button_begin['state'] = tk.DISABLED
  button_finish['state'] = tk.NORMAL
  variable.set('')

def finish():
  print('退勤', variable.get())
  button_begin['state'] = tk.NORMAL
  button_finish['state'] = tk.DISABLED
  variable.set('')

root = tk.Tk()
root.title('出退勤ツール')

button_begin = ttk.Button(text='出勤', command=begin)
button_begin.pack(side='left')

button_finish = ttk.Button(text='退勤', command=finish, state=tk.DISABLED)
button_finish.pack(side='left')

variable = tk.StringVar()
entry = ttk.Entry(textvariable=variable)
entry.pack(side='left')

root.mainloop()