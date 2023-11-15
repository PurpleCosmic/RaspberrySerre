from tkinter import *

tk = Tk()

frame = Frame(tk, borderwidth=2)
frame.pack(fill=BOTH, expand=1)

def quitFunction():
	print("Exitting")
	tk.quit()

exitButton = Button(frame, text = "Exit", command = quitFunction,  height = 2, width = 6)
exitButton.pack(side = BOTTOM)

tk.mainloop()
