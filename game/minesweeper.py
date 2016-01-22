from tkinter import *

root = Tk()
root.resizable(0, 0)
root.title("Minesweeper")
frame = Frame(root)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0)

class Tiles:
	def __init__(self, frame, size):
		self.size = size
		self.frame = frame
		self.tiles[]

		for x in range(self.size):
			self.tiles.append([])
			for y in range(self.size):
				this.tiles[x].append(Button())
				tiles[x][y] = Button(self.frame, text=' ', width=2, bd = 3, command=lambda row=x, col=y: self.clicked(row, col)
				tiles[x][y].grid(row=x, column=y)

		for x in range(this.size):
			Grid.columnconfigure(frame, x, weight=1)

		for y in range(this.size):
  			Grid.rowconfigure(frame, y, weight=1)
  	
	def clicked(self, x, y):
		tiles[x][y]["text"] = '@'
		tiles[x][y]["relief"] = SUNKEN

root.mainloop()
