# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 19:47:31 2017

@author: zabdom
"""

import pygame, pygame.mixer
from pygame import *
import random
from pygame.locals import *
import sys

pygame.init()
okno = pygame.display.set_mode((800,600))
pygame.display.set_caption('Whac-a-Vader')
#iconIMG = pygame.image.load('/UBUNTU/Games/Images/icon1.png')
#pygame.display.set_icon(iconIMG)
pygame.display.update()
BLACK = (0,0,0)
WHITE = (255,255,255)

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()
clock = pygame.time.Clock()
pkt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
p = 2
score = pkt[p]

def display():
     pygame.display.update()

def score_view(count):
    font = pygame.font.SysFont(None, 45)
    text = font.render(str(count), True, WHITE)
    okno.blit(text,(190,33))
    display()

def button(x,y,w,h,action = None):
     mouse1 = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x+w > mouse1[0] > x and y+h > mouse1[1] > y:
         if click[0] == 1 and action != None:
             action()

def resume():
    global pause
    pause = False
    
def pause(): 
    global pause
    pauseIMG = pygame.image.load('./pictures/pause1.jpg')
 
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        okno.fill(BLACK)
        okno.blit(pauseIMG, (0,0))
        display()
     
        button(282,311,258,60, resume)
        button(310,385,258,60, main)
        
def rules(): 
    while rules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        display()
        okno.fill(BLACK)
        rulesIMG = pygame.image.load('./pictures/rules.jpg')
        okno.blit(rulesIMG, (0,0))
        display()
        button(19,13,116,60, main)

    
def hit(x,y):
     global clock,score,p
     music = pygame.mixer.Sound('./music/blaster.wav')
     vaderIMG = pygame.image.load('./pictures/icon.png')
     okno.blit(vaderIMG,(x+14,y+14))
     display()
     score_view(str(score))
     for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
               music.play()
               score += 1
     display()
'''
     for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
              music.play()
              mouse = pygame.mouse.get_pos()
              click = pygame.mouse.get_pressed()
              if x+87 > mouse[0] > x and y+87 < mouse[1] < y:
                   if click[0] == 1:
                        p += 1
'''
     #clock.tick(60)
     #display()
         
'''
def vader(x,y):
     vaderIMG = pygame.image.load('/Images/icon.png')
     okno.blit(vaderIMG,(x,y))
     display()
'''     

def random_hit1():                
     global clock,score,p
     random.seed()
     r = random.randrange(4)
     if r == 1:
          clock.tick(1)
          hit(289,286)
          clock.tick(2)
     elif r == 2:
          clock.tick(1)
          hit(442,286)
          clock.tick(2)
     elif r == 3:
          clock.tick(1)
          hit(289,385)
          clock.tick(2)
     else:
          clock.tick(1)
          hit(442,385)
          clock.tick(2)

def random_hit2():
     global clock,score,p
     random.seed()
     r = random.randrange(6)
     if r == 1:
          clock.tick(1)
          hit(224,284)
          clock.tick(2)
     elif r == 2:
          clock.tick(1)
          hit(367,284)
          clock.tick(2)
     elif r == 3:
          clock.tick(1)
          hit(502,284)
          clock.tick(2)
     elif r == 4:
          clock.tick(1)
          hit(224,385)
          clock.tick(2)
     elif r == 5:
          clock.tick(1)
          hit(365,385)
          clock.tick(2)
     else:
          clock.tick(1)
          hit(502,385)
          clock.tick(2)

def random_hit3():
     global clock,score,p
     random.seed()
     r = random.randint(1,9)
     if r == 1:
          clock.tick(1)
          hit(228,184)
          clock.tick(2)
     elif r == 2:
          clock.tick(1)
          hit(368,184)
          clock.tick(2)
     elif r == 3:
          clock.tick(1)
          hit(502,184)
          clock.tick(2)
     elif r == 4:
          clock.tick(1)
          hit(228,286)
          clock.tick(2)
     elif r == 5:
          clock.tick(1)
          hit(368,286)
          clock.tick(2)
     elif r == 6:
          clock.tick(1)
          hit(502,286)
          clock.tick(2)
     elif r == 7:
          clock.tick(1)
          hit(228,386)
          clock.tick(2)
     elif r == 8:
          clock.tick(1)
          hit(368,386)
          clock.tick(2)
     else:
          clock.tick(1)
          hit(502,386)
          clock.tick(2)

def quit_game():
     pygame.quit()
     quit()
     
'''
def come_back():
     pygame.mixer.music.stop()
     pygame.mixer.music.load('/UBUNTU/Game/come_back.wav')
     pygame.mixer.music.play(0)
     pygame.mixer.music.stop()
     pygame.mixer.music.load('/UBUNTU/Game/breath.wav')
     pygame.mixer.music.play(5)
     
     gameExit = False

     while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
                 pygame.quit()
                 quit()
                 
             display()
             okno.fill(BLACK)
             come_backIMG = pygame.image.load('/UBUNTU/Game/Images/come_back.jpg')
             okno.blit(come_backIMG,(0,0))
             display()
             button(282,454,258,60, game_mode)
'''             

def game_mode():
     gameExit = False

     while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
                 pygame.quit()
                 quit()

             okno.fill(BLACK)
             game_mode = pygame.image.load('./pictures/game_mode.jpg')
             okno.blit(game_mode,(0,0))
             display()
             button(303,258,267,68, game_loop1)
             button(303,340,267,68, game_loop2)
             button(303,421,267,68, game_loop3)
             button(670,14,100,65, main)
    

def game_loop1():
     global clock,mouse,click,score,p
          
     pygame.mixer.music.stop()
     pygame.mixer.music.load('./music/breath.wav')
     pygame.mixer.music.play(-1)
     score = 0
     gameExit = False

     while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
                 pygame.quit()
                 quit()

             display()
             FPSclock = pygame.time.Clock()
             FPSclock.tick(60)
             okno.fill(BLACK)
             loopIMG1 = pygame.image.load('./pictures/game_loop1.jpg')
             okno.blit(loopIMG1,(0,0))
             display()
             button(257,498,305,69, pause)
             button(688,14,89,65, main)
             random_hit1()
             display()
             
             
def game_loop2():
     global clock,mouse,click,score,p
     
     pygame.mixer.music.stop()
     pygame.mixer.music.load('./music/breath.wav')
     pygame.mixer.music.play(-1)
     gameExit = False

     while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
                 pygame.quit()
                 quit()

             display()
             FPSclock = pygame.time.Clock()
             FPSclock.tick(60)
             okno.fill(BLACK)
             loopIMG2 = pygame.image.load('./pictures/game_loop2.jpg')
             okno.blit(loopIMG2,(0,0))
             display()
             button(257,498,305,69, pause)
             button(688,14,89,65, main)
             random_hit2()
             display()
             
def game_loop3():
     global clock,mouse,click,score,p
     
     pygame.mixer.music.stop()
     pygame.mixer.music.load('./music/breath.wav')
     pygame.mixer.music.play(-1)
     gameExit = False

     while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
                 pygame.quit()
                 quit()

             display()
             FPSclock = pygame.time.Clock()
             FPSclock.tick(60)
             okno.fill(BLACK)
             loopIMG3 = pygame.image.load('./pictures/game_loop3.jpg')
             okno.blit(loopIMG3,(0,0))
             display()
             button(257,498,305,69, pause)
             button(688,14,89,65, main)
             random_hit3()
             display()
     
def main():
     display()
     pygame.mixer.music.load('./music/march.wav')
     pygame.mixer.music.play(-1)
     gameExit = False

     while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
                 pygame.quit()
                 quit()
                
             display()
             FPSclock = pygame.time.Clock()
             FPSclock.tick(60)
             display()
             okno.fill(BLACK)
             intro = pygame.image.load('./pictures/obraz.jpg')
             okno.blit(intro,(0,0))
             display()
             button(282,311,258,60, game_mode)
             button(282,383,258,60, rules)
             button(282,454,258,60, quit_game)
   
main()        
