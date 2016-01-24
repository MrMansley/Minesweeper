from Tkinter import *
from random import *

root = Tk()
root.resizable(0, 0)
root.title("Minesweeper")
frame = Frame(root)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0)

class Tiles:
    def __init__(self, frame, size, mines):
        self.size = size
        self.frame = frame
        self.mines = mines
        self.tiles = []
        self.minearray = []

        for x in range(self.size):
            self.tiles.append([])
            self.minearray.append([])
            for y in range(self.size):
                self.minearray[x].append(0)
                self.tiles[x].append(Button())
                self.tiles[x][y] = Button(self.frame, text=' ', width=2, bd = 3, bg="#CDCDCD", command=lambda row=x, col=y: self.clicked(row, col))
                self.tiles[x][y].grid(row=x, column=y)

        while self.mines > 0:
            randX = randint(0, size - 1)
            randY = randint(0, size - 1)
            if self.minearray[randX][randY] == 0:
                self.minearray[randX][randY] = 1
                self.mines -= 1

        print(self.minearray)
    
    def clicked(self, x, y):
        neighbors = 0
        self.tiles[x][y]["relief"] = SUNKEN

        if self.minearray[x][y] == 0:
            if x < self.size - 1 and self.minearray[x+1][y] == 1:
                neighbors += 1
            if x < self.size - 1 and y < self.size - 1 and self.minearray[x+1][y+1] == 1:
                neighbors += 1
            if x < self.size - 1 and y > 0 and self.minearray[x+1][y-1] == 1:
                neighbors += 1
            if x > 0 and self.minearray[x-1][y] == 1:
                neighbors += 1
            if x > 0 and y < self.size - 1 and self.minearray[x-1][y+1] == 1:
                neighbors += 1
            if x > 0 and y > 0 and self.minearray[x-1][y-1] == 1:
                neighbors += 1
            if y < self.size - 1 and self.minearray[x][y+1] == 1:
                neighbors += 1
            if y > 0 and self.minearray[x][y-1] == 1:
                neighbors += 1
        
        if self.minearray[x][y] == 1:
            self.tiles[x][y]["text"] = '@'
        else:
            self.tiles[x][y]["text"] = neighbors

gameTiles = Tiles(frame, 10, 25)
root.mainloop()
