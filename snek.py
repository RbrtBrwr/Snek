# SNEK.PY 
# by Robert Brewer
# Caracas, Venezuela

import pygame
import random
import math
import time

pygame.init()
pygame.font.init()

random.seed(round(time.time()))
width = 500
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('SNEK')

clock = pygame.time.Clock()

class sneky(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.fast = 6
        self.hitbox = (0,0,12,12)
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.len = 1
        self.position = []
        self.bodyParts = []
        self.body = []

    def draw(self, win, direction):
        if direction == 'up':
            self.p1 = self.x - 6
            self.p2 = self.y + 12
            self.p3 = self.x + 6
            self.p4 = self.y + 12
            self.hitbox = (self.p1, self.y, 12, 12)
            
        elif direction == 'down':
            self.p1 = self.x - 6
            self.p2 = self.y - 12
            self.p3 = self.x + 6
            self.p4 = self.y - 12
            self.hitbox = (self.p1, self.p2, 12, 12)


        elif direction == 'left':
            self.p1 = self.x + 12
            self.p2 = self.y - 6
            self.p3 = self.x + 12
            self.p4 = self.y + 6
            self.hitbox = (self.x, self.p2, 12, 12)

        elif direction == 'right':
            self.p1 = self.x - 12
            self.p2 = self.y - 6
            self.p3 = self.x - 12
            self.p4 = self.y + 6
            self.hitbox = (self.p1, self.p2, 12, 12)
            
        
        for x in self.bodyParts:
            pygame.draw.polygon(screen, (0, 222, 0), [(x[0], x[1]), (x[2], x[3]), (x[4], x[5])], 0)






class froot(object):
    def __init__(self):
        self.frutX = random.randint(10, width - 10)
        self.frutY = random.randint(10, height - 10)
        self.hitbox = (self.frutX - 5, self.frutY - 5, 10, 10)

    def draWfroot(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.frutX, self.frutY), 5)

    def ate(self):
        self.frutX = random.randint(10, width - 10)
        self.frutY = random.randint(10, height - 10)
        self.hitbox = (self.frutX - 5, self.frutY - 5, 10, 10)

def text(message, xpos, ypos, color):
    Tfont = pygame.font.Font('freesansbold.ttf', 25)
    message = Tfont.render(message, True, color)
    screen.blit(message, [xpos, ypos])

def drawScore(score, xpos, ypos, size):
    scoretxt = pygame.font.Font('freesansbold.ttf', size)
    scr = scoretxt.render("Score: " + str(score) , True, (0,0,255))
    screen.blit(scr, [xpos, ypos])

def draWin():
    screen.fill((0,0,0))
    snek.draw(screen, snek.direction)

def startScreen():
    screen.fill((0,0,0))
    text("PRESS 'UP' TO START", width/4 - 10, height/3, (255, 255, 255))
    snek.p1 = snek.x - 6
    snek.p2 = snek.y + 12
    snek.p3 = snek.x + 6
    snek.p4 = snek.y + 12
    pygame.draw.polygon(screen, (0, 222, 0), [(snek.x, snek.y), (snek.p1, snek.p2), (snek.p3, snek.p4)], 0) 
    pygame.display.update()

def reset():
    snek = sneky(width/2, height/2, 'up')
    frut = froot()
    snek.len = 0
    mainloop()


def mainloop():
    youLose = False
    snekHit = False
    gameStart = True

    moveX = 0
    moveY = 0

    score = 0

    snek.len = 1
    snek.fast = 6
    snek.bodyParts = []
    snek.position = []
    snek.body = []

    while not youLose:
        clock.tick(20)
        
        while gameStart == True:

            pygame.draw.polygon(screen, (0, 222, 0), [(snek.x, snek.y), (snek.p1, snek.p2), (snek.p3, snek.p4)], 0)
            startScreen()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        moveY = -snek.fast
                        moveX = 0
                        gameStart = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snek.direction != 'right':
                    moveX = -snek.fast
                    moveY = 0
                        
                    snek.direction = 'left'
                
                elif event.key == pygame.K_RIGHT and snek.direction != 'left':
                    moveX = snek.fast
                    moveY = 0

                    snek.direction = 'right'
                    
                elif event.key == pygame.K_UP and snek.direction != 'down':
                    moveY = -snek.fast
                    moveX = 0

                    snek.direction = 'up'

                elif event.key == pygame.K_DOWN and snek.direction != 'up':
                    moveY = snek.fast
                    moveX = 0
                        
                    snek.direction = 'down'

        snek.x += moveX
        snek.y += moveY

        snek.position = []

        snek.position.append(snek.x)
        snek.position.append(snek.y)
        snek.position.append(snek.p1)
        snek.position.append(snek.p2)
        snek.position.append(snek.p3)
        snek.position.append(snek.p4)
        snek.bodyParts.append(snek.position)

        snek.body.append(snek.hitbox)
        
        if len(snek.bodyParts) > snek.len:
            snek.bodyParts.pop(0)
        
        if len(snek.body) > snek.len:
            snek.body.pop(0)

        draWin()
        frut.draWfroot()

        if snek.x >= width or snek.x <= 0 or snek.y >= height or snek.y <= 0:    
            draWin()
            moveX = 0
            moveY = 0
            snekHit = True

        for x in snek.body[:-5]:
            if snek.hitbox[0] < x[0] + x[3] and snek.hitbox[0] + snek.hitbox[3] > x[0] and snek.hitbox[1] < x[1] + x[3] and snek.hitbox[1] + snek.hitbox[3] > x[1]:
                draWin()
                moveX = 0
                moveY = 0
                snekHit = True

        while snekHit == True:
            text("PRESS 'Q' TO QUIT, 'UP' TO RESTART", 25, height/4, (255, 255, 255))
            text('YOU LOSE', width/3 + 15, height/8, (255, 0, 0))
            drawScore(score, width/3 + 20, height/4 + 50, 30)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                    if event.key == pygame.K_UP:
                        snek.direction = 'up'
                        snek.x = width/2
                        snek.y = height/2
                        reset()
                        snekHit = False



        if snek.hitbox[0] < frut.hitbox[0] + frut.hitbox[3] and snek.hitbox[0] + snek.hitbox[3] > frut.hitbox[0] and snek.hitbox[1] < frut.hitbox[1] + frut.hitbox[3] and snek.hitbox[1] + snek.hitbox[3] > frut.hitbox[1]:
            draWin()
            frut.ate()
            score += 1
            snek.len += 5

            if score <= 10:
                snek.fast += 0.25
            elif score > 10:
                snek.fast += 0.1

        drawScore(score, 10, 10, 20)
        pygame.display.update()



snek = sneky(width/2, height/2, 'up')
frut = froot()
mainloop()
