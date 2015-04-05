#!/usr/bin/env python 
# -*- coding: utf-8 -*-
' Learn and improve the paddle_ball game in the book '
__author__ = 'mota'
from tkinter import*
import random
import time
tk=Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
# ball
    def __init__(self,canvas,paddle,full_game,color):
        self.canvas = canvas
        self.paddle = paddle
        self.full_game = full_game
        self.id = 0
        self.random_speed = []
        self.x = 0
        self.y = 0
        self.lifes = 0
        self.new_ball(color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.full_game.hit_score()
                if not self.full_game.scores%2:
                    self.random_speed = [speed - 1 for speed in self.random_speed]
                return True
        return False
    
    def new_ball(self,color):
        self.canvas.delete(self.id)
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        self.random_speed = [-4,-3,-2,-1]
        self.x = random.choice(self.random_speed)
        self.y = -2
        self.lifes = self.lifes + 1
            
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = -self.y
        if pos[1] == self.canvas_height/2 and self.y < 0:
            self.y = random.choice(self.random_speed)
            self.x = random.choice(self.random_speed)
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            self.y = -(self.y)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = -self.x

class Paddle:
# paddle
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos [2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        self.x = -5
    def turn_right(self,evt):
        self.x = 5
       
class Full_game:
#   Display Lifes and Scores
#   Control Start Game
    def __init__(self,canvas):
        self.scores = 0
        self.canvas = canvas
        self.lifes = 0
        self.running = False
        self.id = canvas.create_text(30,10,text='Score:   %d'%0,fill='brown')
        self.lifeid = canvas.create_text(30,25,text='Lifes:   %d'%0,fill='brown')
        self.canvas.bind_all('<Button-1>',self.game_start)
        self.game_over = canvas.create_text(250,200,text='Game Over',fill='red',font=('Times',30),state='hidden')

    def hit_score(self):
        self.scores = self.scores + 1
        canvas.itemconfig(self.id,text='Score:   %d'%self.scores)
    def reset_score(self):
        self.scores = 0
        canvas.itemconfig(self.id,text='Score:   0')
    def add_lifes(self):
        self.lifes = self.lifes + 1
        canvas.itemconfig(self.lifeid,text='Lifes:   %d'%self.lifes)
    def game_start(self,evt):
        self.running = True
        self.reset_score()
        self.add_lifes()
        canvas.itemconfig(self.game_over,state='hidden')
        
full_game = Full_game(canvas)
paddle = Paddle(canvas,'green')
ball = Ball(canvas,paddle,full_game,'blue') 

def main():
#   main
    if __name__ == '__main__':            
        while 1:
            if full_game.running:
                if ball.hit_bottom:
                    full_game.running = False
                    ball.new_ball('blue')            
                ball.draw()
                paddle.draw()
            if ball.hit_bottom and not full_game.running:
                ball.hit_bottom = False
                canvas.itemconfig(full_game.game_over,state='normal')        
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
main()
