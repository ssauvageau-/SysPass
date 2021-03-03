# -*- coding: utf-8 -*-
"""
@author: ssauvageau-
"""
import tkinter as tk
from SysPass import pwd_build

class Window(tk.Frame):
	def __init__(self, master=None):
		pswd_var = tk.StringVar()
		pswd_var.set("")
		tk.Frame.__init__(self, master)
		self.master = master
		
		Label_1 = tk.Label(self.master, 
				  text="Password: ")
		Label_1.grid(row=0, column=0)
		
		Field_1 = tk.Entry(self.master, 
				  bd=5, 
				  state=tk.DISABLED,
				  show="*", 
				  textvariable=pswd_var)
		Field_1.grid(row=0, column=1, columnspan=2)
		
		Button_G = tk.Button(self.master, 
					text="Generate Password", 
					command=lambda:self.genButton(pswd_var))
		Button_G.grid(row=0, column=3)
		
		bottomFrame = tk.Frame(self.master)
		bottomFrame.grid(row=1, column=0, columnspan=4)
		
		Button_C = tk.Button(bottomFrame, 
					text="Copy to Clipboard", 
					command=lambda:self.copyB(Field_1))
		Button_C.pack(side=tk.LEFT)
		#Button_C.grid(row=1, column=0, columnspan=2)
		
		Button_E = tk.Button(bottomFrame, 
					text="Exit Program",
					command=lambda:self.exitB())
		Button_E.pack(side=tk.RIGHT)
		#Button_E.grid(row=1, column=2, columnspan=2)
		
	def genButton(self, var):
		var.set(pwd_build())
	def copyB(self, field):
		tk.Frame.clipboard_clear(self)
		tk.Frame.clipboard_append(self, field.get())
		tk.Frame.update(self)
	def exitB(self):
		self.master.destroy()
		

def main():
	root = tk.Tk()
	app = Window(root)

	root.wm_title("Hardware Password Generator")

	root.mainloop()