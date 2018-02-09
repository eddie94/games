from source import *
from random import randint
from random import randrange

class rect():

    def __init__(self):

        self.size = [20,20]
        self.speed = 1
        self.surface = pg.Surface(self.size)
        self.rect = self.surface.get_rect()

    def move(self):

        up = (0,-self.speed)
        down = (0,self.speed)
        right = (self.speed,0)
        left = (-self.speed,0)

        pressed = pg.key.get_pressed()

        if pressed[pg.K_UP]:
            if self.rect.top <= 0:
                self.rect.top = 0
            else:
                self.rect = self.rect.move(up)
        if pressed[pg.K_DOWN]:
            if self.rect.bottom >= 600:
                self.rect.bottom = 600
            else:
                self.rect = self.rect.move(down)
        if pressed[pg.K_RIGHT]:
            if self.rect.right >= 600:
                self.rect.right = 600
            else:
                self.rect = self.rect.move(right)
        if pressed[pg.K_LEFT]:
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.rect = self.rect.move(left)

class obstacle():

    def __init__(self):

        self.size = (10,10)
        self.speed = [randrange(-4,4),randrange(-4,4)]
        self.surface = pg.Surface(self.size)
        self.rect = self.surface.get_rect()

    def check_inside(self):

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
        if self.rect.right >= 600:
            self.rect.right = 600
        if self.rect.left <= 0:
            self.rect.left = 0

    def move(self):

        if self.rect.top <= 0:
            if self.speed[1] > 0:
                self.speed[1] = -randint(1,4)
            elif self.speed[1] < 0:
                self.speed[1] = randint(1,4)
        if self.rect.bottom >= 600:
            if self.speed[1] > 0:
                self.speed[1] = -randint(1,4)
            elif self.speed[1] < 0:
                self.speed[1] = randint(1,4)
        if self.rect.right >= 600:
            if self.speed[0] > 0:
                self.speed[0] = -randint(1,4)
            elif self.speed[0] < 0:
                self.speed[0] = randint(1,4)
        if self.rect.left <= 0:
            if self.speed[0] > 0:
                self.speed[0] = -randint(1,4)
            elif self.speed[0] < 0:
                self.speed[0] = randint(1,4)

        self.rect = self.rect.move(self.speed)
        self.check_inside()