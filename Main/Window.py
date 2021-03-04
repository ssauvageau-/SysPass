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
		
		input_use_case_var = tk.StringVar()
		input_use_case_var.set("")
		
		tk.Frame.__init__(self, master)
		self.master = master
		
		topFrame = tk.Frame(self.master)
		topFrame.grid(row=0, column=0, columnspan=4)
		
		Label_U = tk.Label(topFrame,
					 text="Use Case: ")
		Label_U.grid(row=0, column=0)
		
		Field_U = tk.Entry(topFrame,
					 bd = 5,
					 textvariable=input_use_case_var,
					 width=38)
		Field_U.grid(row=0, column=1, columnspan=3)
		
		middleFrame = tk.Frame(self.master)
		middleFrame.grid(row=1, column=0, columnspan=4)
		
		Label_P = tk.Label(middleFrame, 
				  text="Password: ")
		Label_P.grid(row=0, column=0)
		
		# Technically, this serves no real purpose other than to communicate that something happened. 
		Field_P = tk.Entry(middleFrame, 
				  bd=5, 
				  state=tk.DISABLED,
				  show="*", 
				  textvariable=pswd_var)
		Field_P.grid(row=0, column=1, columnspan=2)
		
		Button_G = tk.Button(middleFrame, 
					text="Generate Password", 
					command=lambda:self.genButton(pswd_var, input_use_case_var))
		Button_G.grid(row=0, column=3)
		
		bottomFrame = tk.Frame(self.master)
		bottomFrame.grid(row=2, column=0, columnspan=4)
		
		Button_C = tk.Button(bottomFrame, 
					text="Copy to Clipboard", 
					command=lambda:self.copyB(Field_P))
		Button_C.pack(side=tk.LEFT)
		
		Button_E = tk.Button(bottomFrame, 
					text="Exit Program",
					command=lambda:self.exitB())
		Button_E.pack(side=tk.RIGHT)
		
	# Lambda functions		
	def genButton(self, out_var, in_var):
		out_var.set(pwd_build(in_var.get()))
	def copyB(self, field):
		tk.Frame.clipboard_clear(self)
		tk.Frame.clipboard_append(self, field.get())
		tk.Frame.update(self)
	def exitB(self):
		self.master.destroy()
		

root = tk.Tk()
app = Window(root)

root.wm_title("Hardware Password Utility")

root.mainloop()