__author__ = 'epq_008'
#!usr/bin/env python

from Tkinter import *
import random
import sys
import os
from os.path import *
from tkFileDialog import *
import string


__doc__ = """Classic arcade game Snake coded in Python, and then Optimized to show the benefits of python programming."""

class PythonGui(object):
    def __init__(self, parent) :
        """Constructor for GUI, as well as creating game objects"""
        self.parent = parent
        self.container = Frame(parent)
        self.container.pack()

        self.snake_ids = []
        self.snake_direction = ['UP'] #UP is initial value
        self.food_id = 0
        self.countdown_list = []

        self.Paused = False
        self.score = StringVar()
        self.score.set(str(0))
        self.GameOver = False
        self.speed = 100

        #setup File menu
        self.menubar = Menu(self.parent)
        self.file_menu = Menu(self.menubar, tearoff=0)
        #---------------------OPTIMIZED-------------------------#
        menu_items = [("New Game", self.newGame), ("Save Game", self.saveGame), ("Load Game", self.loadGame), ("Pause Game (P)", self.pauseGame), ("Quit", self.quitGame)]
        for list in menu_items:
            self.file_menu.add_command(label=list[0], command=list[1])
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.parent.config(menu=self.menubar)

        #setup Canvas
        self.canvas = Canvas(self.container, height=400, width=400)
        self.canvas.bind("w", lambda event, dir='UP', anti='DOWN': self.move(dir, anti))
        self.canvas.bind("a", lambda event, dir='LEFT', anti='RIGHT': self.move(dir, anti))
        self.canvas.bind("s", lambda event, dir='DOWN', anti='UP': self.move(dir, anti))
        self.canvas.bind("d", lambda event, dir='RIGHT', anti='LEFT': self.move(dir, anti))
        self.canvas.bind("<Left>", lambda event, dir='LEFT', anti='RIGHT': self.move(dir, anti))
        self.canvas.bind("<Right>", lambda event, dir='RIGHT', anti='LEFT': self.move(dir, anti))
        self.canvas.bind("<Up>", lambda event, dir='UP', anti='DOWN': self.move(dir, anti))
        self.canvas.bind("<Down>", lambda event, dir='DOWN', anti='UP': self.move(dir, anti))
        self.canvas.bind("p", self.pauseGame)
        self.canvas.pack(side=TOP)
        self.canvas.focus_force()
        id = self.canvas.create_oval(180, 180, 200, 200, fill="green", outline="black")
        self.snake_ids.append(id)
        self.createFood()

        #setup score label
        self.score_label = Label(textvariable=self.score)
        self.score_label.pack(side=BOTTOM)

    def saveGame(self, event=None):
        """
Method to save all relevant information into a file 'PythonGame#', where # is the next available
number. Items saved (in this order) are: snake coordinates, direction of each snake-body, the countdown
to determine when to change snake directions, the food coordinates, and the score"""
        if self.GameOver == False: #game is NOT over
            save_file = []
            #snake coords first
            for id in self.snake_ids:
                (x0, y0, x1, y1) = self.canvas.coords(id)
                temp = str(x0) + " " + str(y0) + " " +  str(x1) + " " + str(y1) + "\n"
                save_file.append(temp)
            save_file.append("---\n")
            #directions
            for dir in self.snake_direction:
                save_file.append(dir + "\n")
            save_file.append("---\n")
            #countdown
            for x in self.countdown_list:
                save_file.append(str(x) + "\n")
            save_file.append("---\n")
            #food id
            (x0, y0, x1, y1) = self.canvas.coords(self.food_id)
            temp = str(x0) + " " + str(y0) + " " +  str(x1) + " " + str(y1)
            save_file.append(temp + "\n")
            save_file.append("---\n")
            #score
            save_file.append(self.score.get() + "\n")
            i = 1
            while(1):
                file_name = "PythonGame" + str(i)
                if exists(file_name):
                    i += 1
                else:
                    f = open(file_name, 'w')
                    f.writelines(save_file)
                    f.flush()
                    f.close()
                    break

    def loadGame(self, event=None):
        """
Method to load a saved python game via a dialog box. Items loaded (in this order) are: snake coordinates, direction
of each snake-body, the countdown to determine when to change snake directions, the food coordinates, and the
score"""
        for id in self.canvas.find_all():
            self.canvas.delete(id)
        self.food_id = 0
        self.countdown_list = []
        self.snake_ids = []
        file = askopenfile(mode='r').readlines()
        #get rid of newline character
        for x in xrange(0, len(file)):
            file[x] = file[x][:-1]
        self.snake_ids = []
        x = 0
        #get snake ids
        while file[x] != '---':
            coords = string.split(file[x])
            self.snake_ids.append(self.canvas.create_oval(float(coords[0]), float(coords[1]), float(coords[2]), float(coords[3]), fill="green", outline="black"))
            x += 1
        x += 1
        #get snake directions
        self.snake_direction = []
        while file[x] != '---':
            self.snake_direction.append(file[x])
            x += 1
        x += 1
        #get countdown
        while file[x] != '---':
            self.countdown_list.append(int(file[x]))
            x += 1
        x += 1
        #get coords of food
        coords = string.split(file[x])
        self.food_id = self.canvas.create_oval(float(coords[0]), float(coords[1]), float(coords[2]), float(coords[3]), fill="red")
        x += 2
        #get score
        self.score.set(file[x])
        self.Paused = True
        self.GameOver = False

    def newGame(self, event=None):
        """Resets the game and score for a new game"""
        self.createFood()
        id = self.canvas.create_oval(180, 180, 200, 200, fill="green", outline="black")
        self.snake_ids.append(id)
        self.GameOver = False
        self.score.set('0')
        self.Paused = False
        self.autoMove()

    def pauseGame(self, event=None):
        """Pauses the game by setting the global variable Paused to true"""
        if self.GameOver == False:
            if self.Paused == False:
                #Game is NOT paused - these events will pause the game
                self.Paused = True
            else :
                #Game is paused - these events will unpause the game
                self.Paused = False
                self.autoMove()

    def quitGame(self, event=None):
        """quits the game by destorying root"""
        self.parent.destroy()

    #--------------------------OPTIMIZED-----------------------#
    def move(self, dir, anti):
        """Optimzied move method. Every key press passes in the direction intended to go and the direction opposite
it. The code then executes the same way for every button press."""
        if self.Paused == False and self.GameOver == False: #game NOT paused or over
            if self.snake_direction[0] != dir and self.snake_direction[0] != anti:
                self.countdown_list.append(len(self.snake_ids))
                self.snake_direction[0] = dir

    def gameOver(self):
        """stops the game and resets all variables. erases the canvas and sets score to 'GAME OVER'"""
        self.score.set('GAME OVER')
        self.GameOver = True
        for id in self.canvas.find_all():
            self.canvas.delete(id)
        self.snake_direction = ['UP']
        self.countdown_list = []
        self.snake_ids = []
        self.GameOver = True

    def createFood(self):
        """creates new food item at random coordinate on screen"""
        start_x = random.randint(10, 390)
        start_y = random.randint(10, 390)
        self.food_x0 = start_x
        self.food_y0 = start_y
        self.food_x1 = start_x + 20
        self.food_y1 = start_y + 20
        id_list = self.canvas.find_overlapping(self.food_x0, self.food_y0, self.food_x1, self.food_y1)
        if len(id_list) == 0:
            if self.food_x0 >= 0 or self.food_x1 <= 400 or self.food_y0 >= 0 or self.food_y1 <= 400:
                self.canvas.delete(self.food_id)
                self.food_id = self.canvas.create_oval(self.food_x0, self.food_y0, self.food_x1, self.food_y1, fill="red")
            else :
                self.createFood()
        else :
            self.createFood()

    def testCollision(self, python_id):
        """tests collision against food, itself, and wall. If collided with food, increments score, creates new
food, and creates another tail or snake. If wall or itself, calls gameOver(). Optimized the if statements with
a dictionary that has the directions as keys, and a tuple of the (x, y) changes as the value. For example,
'LEFT': (20, 0) means that moving left changes the x value by 20 and the y value by 0"""
        (x1, y1, x2, y2) = self.canvas.coords(python_id)
        id_list = self.canvas.find_overlapping(x1+5, y1+5, x2-5, y2-5)
        #Test collision with food
        if self.food_id in id_list:
            #create new food
            self.createFood()
            #increment score
            self.score.set(str(int(self.score.get()) + 10))

            #create next snake
            #--------------------OPTIMIZED----------------#
            dirs = {'LEFT': (20, 0), 'RIGHT': (-20, 0), 'UP': (0, 20), 'DOWN': (0, -20)}
            (x0, y0, x1, y1) = self.canvas.coords(self.snake_ids[-1])
            cur_dir = self.snake_direction[-1]
            id = self.canvas.create_oval(x0+dirs[cur_dir][0], y0+dirs[cur_dir][1], x1+dirs[cur_dir][0], y1+dirs[cur_dir][1], fill="green", outline="black")
            self.snake_ids.append(id)
            self.snake_direction.append(self.snake_direction[-1])
            for x in xrange(0, len(self.countdown_list)):
                self.countdown_list[x] += 1

        #test collision with self
        for id in id_list:
            if id in self.snake_ids:
                if id != self.snake_ids[0]:
                    self.gameOver()

        #test collision with wall
        if x1 < 0 or x2 > 400 or y1 < 0 or y2 > 400:
            self.gameOver()

    def autoMove(self):
        """method called to move the snake and update the canvas. Calls testCollision at end of method. Same
optimization used in this method as in testCollison() - dictionary with directions as keys and (x, y) changes as
values."""
        if self.Paused == False and self.GameOver == False: #Game NOT paused or over
            #Move head of snake
            #-------------OPTIMIZED-------------#
            dirs = {'LEFT': (-20, 0), 'RIGHT': (20, 0), 'UP': (0, -20), 'DOWN': (0, 20)}
            id = self.snake_ids[0] #get head of snake
            cur_dir = self.snake_direction[0]
            self.canvas.move(id, dirs[cur_dir][0], dirs[cur_dir][1])

            #Move tails. Perpetuate last direction through snake while countdown != 0
            for x in xrange(1, len(self.snake_direction)):
                id = self.snake_ids[x]
                cur_dir = self.snake_direction[x]
                self.canvas.move(id, dirs[cur_dir][0], dirs[cur_dir][1])

            #Update tail snake direction
            for x in xrange(0, len(self.countdown_list)):
                if self.countdown_list[x] > 1:
                    list = self.countdown_list[x]
                    self.snake_direction[-list + 1] = self.snake_direction[-list]
                self.countdown_list[x] -= 1

            #Always try to remove 0 from list. If 0 not there, catch exception but do nothing
            try:
                self.countdown_list.remove(0)
            except ValueError, e:
                pass

            #Test collision and reset timer
            id = self.snake_ids[0]
            self.testCollision(id)
            self.canvas.after(self.speed, self.autoMove)


#main loop
root = Tk()
gui = PythonGui(root)
gui.autoMove()
root.mainloop()
