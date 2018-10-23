#-*- coding:utf-8 -*-
import random,math,pygame,sys
from pygame.locals import *
from datetime import datetime,date,time
from analogClock import wrap_angle,print_text
font=pygame.font.Font(None,18)
class Point(object):
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,value):
        self.__x=value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,value):
        self.__y=value

    def __str__(self):
        return "{X:"+"{:.0f}".format(self.__x)+ \
    ",Y:"+"{:.0f}".format(self.__y)+"}"

class Ship(object):
    pygame.init()
    def __init__(self,path,radius):
        self.__ship = pygame.image.load(path).convert_alpha()
        self.__ship = pygame.transform.smoothscale(self.__ship, (width // 2, height // 2))
        self.__pos=Point(0,0)
        self.__oldPos=Point(0,0)
        self.__angle=-90.0
        self.__radius=radius
        self.scratch_ship=self.__ship
        self.__rangled=0
        self.__second = datetime.today().second

    def move(self):
        #顺时针转动
        self.__angle=wrap_angle(self.__angle+0.1)
        self.__pos.x=math.cos(math.radians(self.__angle))*self.__radius
        self.__pos.y=math.sin(math.radians(self.__angle))*self.__radius

    def rotate(self):
        delta_x=self.__pos.x-self.__oldPos.x
        delta_y=self.__pos.y-self.__oldPos.y
        rangle=math.atan2(delta_y,delta_x)
        self.__rangled=wrap_angle(-math.degrees(rangle))
        self.scratch_ship=pygame.transform.rotate(self.__ship,self.__rangled)

    def scale(self):
        width,height=self.scratch_ship.get_size()
        #飞船在球的右边
        if 360>self.__rangled>=180 and datetime.today().second-self.__second==1:
            self.__ship=pygame.transform.smoothscale(self.__ship,(int(width*1.01),int(height*1.01)))
        else:
            if datetime.today().second-self.__second==1:
                self.__ship = pygame.transform.smoothscale(self.__ship, (int(width / 1.01),int(height / 1.01)))

    def draw(self,screen):
        width,height=self.scratch_ship.get_size()
        x=400+self.__pos.x-width//2
        y=300+self.__pos.y-height//2
        screen.blit(self.scratch_ship,(x,y))

        print_text(font,0,0,"Orbit: "+"{:.0f}".format(self.__angle))
        print_text(font, 0, 20, "Rotation: " + "{:.2f}".format(self.__rangled))
        print_text(font, 0, 40, "Position: " + str(self.__pos))
        print_text(font, 0, 60, "Old Pos: " + str(self.__oldPos))

    def nextShip(self,screen):
        self.move()
        self.rotate()
        #self.scale()
        self.draw(screen)
        self.__oldPos.x=self.__pos.x
        self.__oldPos.y=self.__pos.y
        self.__second=datetime.today().second

#main program begins
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Orbit Demo")
space=pygame.image.load("code/code/chap06/space.png").convert()
planet=pygame.image.load("code/code/chap06/planet2.png").convert_alpha()
width,height=planet.get_size()
myship=Ship("code/code/chap06/freelance.png",250)
#repeating loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    screen.blit(space,(0,0))
    screen.blit(planet, (400 - width / 2, 300 - height / 2))
    myship.nextShip(screen)
    pygame.display.update()