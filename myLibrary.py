#-*- coding:utf-8 -*-
#-*- name:myLibrary.py -*-
import sys,time,random,math,pygame
from pygame.locals import *

#print text using the supplied font
def print_text(font,x,y,text,color=(255,255,255)):
    imgText=font.render(text,True,color)
    screen=pygame.display.get_surface()
    screen.blit(imgText,(x,y))

#MySprite class extends pygame.sprite.Sprite
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.master_image=None
        self.frame=0
        self.old_frame=-1
        self.frame_width=1
        self.frame_height=1
        self.first_frame=0
        self.last_frame=0
        self.columns=1
        self.last_time=0
        self.direction=0
        self.velocity=Point(0,0)

    def _getX(self):
        return self.rect.x
    def _setX(self,value):
        self.rect.x=value
    X=property(_getX,_setX)

    def _getY(self):
        return self.rect.y
    def _setY(self,value):
        self.rect.y=value
    Y=property(_getY,_setY)

    def _getPos(self):
        return self.rect.topleft
    def _setPos(self,pos):
        self.rect.topleft=pos
    position=property(_getPos,_setPos)

    def load(self,filename,width,height,columns):
        self.master_image=pygame.image.load(filename).convert_alpha()
        self.frame_width=width
        self.frame_height=height
        self.rect=Rect(0,0,width,height)
        self.columns=columns
        rect=self.master_image.get_rect()
        self.last_frame=(rect.width//width)*(rect.height//height)-1

    def update(self,current_time,rate=30):
        if current_time>self.last_time+rate:
            self.frame+=1
            if self.frame>self.last_frame:
                self.frame=self.first_frame
            self.last_time=current_time
        #build current frame only if it changed
        if self.frame!=self.old_frame:
            frameX=(self.frame%self.columns)*self.frame_width
            frameY=(self.frame//self.columns)*self.frame_height
            rect=Rect(frameX,frameY,self.frame_width,self.frame_height)
            self.image=self.master_image.subsurface(rect)
            self.old_frame=self.frame

    def __str__(self):
        return str(self.frame)+","+str(self.first_frame)+\
            ","+str(self.last_frame)+","+str(self.frame_width)+\
            ","+str(self.frame_height)+","+str(self.columns)+\
            ","+str(self.rect)

#Point class
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
