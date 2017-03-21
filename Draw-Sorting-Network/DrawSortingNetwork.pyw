from Tkinter import *
from math import *
resolutionX = 1024
resolutionY = 512
def radius(k):
    if k == 1:
        return 6
    if k == 2:
        return 5
    elif k ==3:
        return 4
    elif k == 4:
        return 3
    elif k <= 6:
        return 2
    return 1
def horizonalSize(k):
    if k == 1:
        return 1
    else:
        return horizonalSize(k-1) + int(pow(2, k)) - 1
def numberOfComparators(k):
    return int(k * (k + 1) * pow(2, k - 2))
def pairs(k):
    if k == 1:
        return [[1],[1],[2]]
    else:
        derived = pairs(k - 1)
        derivedHorizonalSize = horizonalSize(k - 1)
        derivedNumberOfComparators = numberOfComparators(k - 1)
        x = []
        y1 = []
        y2 = []
        bias = int(pow(2, k - 1))
        for i in range(derivedNumberOfComparators):
            x.append(derived[0][i])
            x.append(derived[0][i])
            y1.append(derived[1][i])
            y1.append(derived[1][i] + bias)
            y2.append(derived[2][i])
            y2.append(derived[2][i] + bias)
        for i in range(bias):
            x.append(derivedHorizonalSize + i + 1)
            y1.append(i + 1)
            y2.append(2 * bias - i)
        t = bias / 2
        posX = derivedHorizonalSize + bias
        while t > 0:
            for i in range(t):
                posX += 1
                for j in range(bias / t):
                    x.append(posX)
                    y1.append(i + 1 + j * t * 2)
                    y2.append(i + 1 + j * t * 2 + t)
            t /= 2
        return [x,y1,y2]
class SortingNetwork:
    def __init__(self):
        self.root = Tk()
        self.root.title('Sorting Network')
        self.root.geometry(str(resolutionX)+'x'+str(resolutionY))
        self.canvas = Canvas(self.root, height=512, width=1024, bg='cyan')
        self.canvas.pack()
        self.prompt = Label(self.canvas, text = 'Please input k:', bg = 'cyan', font = ('Arial', 14, 'bold'))
        self.prompt.place(x = 447, y = 210)
        self.input = StringVar()
        self.input.set('3')
        self.entry = Entry(self.canvas, textvariable = self.input)
        self.entry.place(x = 450, y = 240)
        self.button = Button(self.canvas, text = 'Confirm', command = self.draw)
        self.button.place(x = 492, y = 270)
        self.root.mainloop()
    def drawComparator(self, x, y1, y2):
        self.canvas.create_line(x, y1, x, y2)
        self.canvas.create_oval(x - self.rad, y1 - self.rad, x + self.rad, y1 + self.rad, fill = 'black')
        self.canvas.create_oval(x - self.rad, y2 - self.rad, x + self.rad, y2 + self.rad, fill = 'black')
    def draw(self):
        self.k = int(self.input.get())
        self.rad = radius(self.k)
        if self.k < 1:
            self.root.destroy()
        self.x = horizonalSize(self.k)
        self.y = int(pow(2, self.k))
        self.cellX = float(resolutionX) / (self.x + 1)
        self.cellY = float(resolutionY) / (self.y + 1)
        self.prompt.place_forget()
        self.entry.place_forget()
        self.button.place_forget()
        self.canvas.config(bg = 'white')
        for i in range(self.y):
            self.canvas.create_line(0, (i + 1) * self.cellY, resolutionX, (i + 1) * self.cellY)
        self.map = pairs(self.k)
        for i in range(numberOfComparators(self.k)):
            self.drawComparator(self.map[0][i] * self.cellX, self.map[1][i] * self.cellY, self.map[2][i] * self.cellY)
sortingnetwork = SortingNetwork()
