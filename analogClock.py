# -*- coding utf-8 -*-
import sys,random,math,pygame
from pygame.locals import *
from datetime import datetime,date,time

def print_text(font,x,y,text,color=(255,255,255)):
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))

pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Circle Demo")
screen.fill((0,0,100))
white=(255,255,255)
yellow=(255,255,0)
orange=(220,180,0)
pink=(255,100,100)
pos_x=300
pos_y=250
radius=200
angle=360
"""
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    #increment angle
    angle+=1
    if angle>360:
        angle=0
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        color=r,g,b
    x=math.cos(math.radians(angle))*radius
    y=math.sin(math.radians(angle))*radius

    #draw one step around the circle
    pos=(int(pos_x+x),int(pos_y+y))
    pygame.draw.circle(screen,color,pos,10,0)
    pygame.display.update()
"""
def wrap_angle(angle):
    return abs(angle%360)

font=pygame.font.Font(None,24)
if __name__ == '__main__':

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                sys.exit()
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        today = datetime.today()
        #clear center
        screen.fill((0, 0, 100))
        pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)
        for n in range(1, 13):
            angle = math.radians(n * (360 / 12) - 90)
            x = math.cos(angle) * (radius - 20) - 10
            y = math.sin(angle) * (radius - 20) - 10
            print_text(font, pos_x + x, pos_y + y, str(n))
        #draw second
        second=today.second
        sec_angle=wrap_angle(second*(360/60)-90)
        sec_angle=math.radians(sec_angle)
        sec_x=math.cos(sec_angle)*(radius-40)
        sec_y=math.sin(sec_angle)*(radius-40)
        target=(pos_x+sec_x,pos_y+sec_y)
        pygame.draw.line(screen,yellow,(pos_x,pos_y),target,6)
        #draw minute
        minute=today.minute
        minu_angle1=wrap_angle(minute*(360/60)-90+second/10)
        minu_angle=math.radians(minu_angle1)
        minu_x=math.cos(minu_angle)*(radius-60)
        minu_y=math.sin(minu_angle)*(radius-60)
        target=(pos_x+minu_x,pos_y+minu_y)
        pygame.draw.line(screen,orange,(pos_x,pos_y),target,12)
        #draw hour
        hour=today.hour%12
        hour_angle=wrap_angle(hour*(360/12)-90+minu_angle1/12)
        hour_angle=math.radians(hour_angle)
        hour_x=math.cos(hour_angle)*(radius-80)
        hour_y=math.sin(hour_angle)*(radius-80)
        target=(pos_x+hour_x,pos_y+hour_y)
        pygame.draw.line(screen,pink,(pos_x,pos_y),target,25)
        #cover the center
        pygame.draw.circle(screen,white,(pos_x,pos_y),20)
        print_text(font,0,0,str(hour)+":"+str(minute)+":"+str(second))
        pygame.display.update()