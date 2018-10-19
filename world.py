from random import randint
from mouse import Mouse
from vector import Vector2
from ball import Ball
from pygame.locals import *
import pygame
import collision


class World:
    def __init__(self,screen_length,screen_width):
        self.things = {}
        self.thing_index = 0
        self.screen_length = screen_length
        self.screen_width = screen_width
        self.background_color = (255,255,255)
        #self.mouse = Mouse()
        
    def set_ball_list(self,n):
        ball_count = n
        balls = []
        for i in range(ball_count):
            radius = 20
            x_pos = randint(0+radius,self.screen_width-radius)
            y_pos = randint(0+radius,self.screen_length-radius)
            x_vel = randint(0,200)
            y_vel = randint(0,200)
            if i<ball_count/2:
                color = (255, 0, 0)
            else:
                color = (0, 0, 255)
            self.things[self.thing_index] = Ball(Vector2(x_pos,y_pos),Vector2(x_vel,y_vel),radius,color)
            self.thing_index += 1
        
    def check_for_collision(self):
        for i in range(self.thing_index):
            b1 = self.things[i]
            for j in range(i):
                b2 = self.things[j]
                if collision.peer_contact(b1,b2):
                    collision.peer_collision(b1,b2)
            collision.manage_wall_contact(b1,self.screen_width,self.screen_length)
            #if collision.mouse_contact(self.mouse,b1):
            #    collision.mouse_collision(self.mouse,b1)

    def update(self,time_passed):
        for key in self.things.keys():
            self.things[key].update(time_passed)
        #self.mouse.update(time_passed)
        self.check_for_collision()

    def render(self,screen):
        screen.fill(self.background_color)
        for key in self.things.keys():
            self.things[key].render(screen)
        #self.mouse.render(screen)
