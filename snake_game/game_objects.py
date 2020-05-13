import math
import random
import pygame

class cube(object):
    def __init__(self, start, rows, w, color = (255, 0, 0)):
        self.pos   = start
        self.rows  = rows
        self.w     = w
        self.dirnx = 1
        self.dirny = 0
        self.color = color

        
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1,j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius,j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)
        


class snake(object):
    body = []
    turns = {}
    def __init__(self, rows, w, color, pos):
        self.color = color
        self.rows = rows
        self.w = w
        self.head = cube(pos, rows, w)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def get_length(self):
    	return len(self.body)

    def move(self, flag_new_event = False, dirnx = 0, dirny = 0):
        if flag_new_event:
            self.dirnx = dirnx
            self.dirny = dirny
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        else: 
            for i, c in enumerate(self.body):
                p = c.pos[:]
                if p in self.turns:
                    turn = self.turns[p]
                    c.move(turn[0],turn[1])
                    if i == len(self.body) - 1:
                        self.turns.pop(p)
                else:
                    if c.dirnx == -1 and c.pos[0] <= 0:
                        c.pos = (c.rows-1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows - 1: 
                        c.pos = (0,c.pos[1])
                    elif c.dirny == 1 and c.pos[1] >= c.rows - 1: 
                        c.pos = (c.pos[0], 0)
                    elif c.dirny == -1 and c.pos[1] <= 0: 
                        c.pos = (c.pos[0],c.rows - 1)
                    else: c.move(c.dirnx, c.dirny)
        

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1


    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny


        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1]), self.rows, self.w))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1]), self.rows, self.w))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1), self.rows, self.w))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1), self.rows, self.w))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
        

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def randomSnack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
        
    return (x,y)