#-*- coding:utf-8 -*-
import sys,pygame
from pygame.locals import *
"""
file=open("data2.txt","w")
file.write("Sample file writing\n")
file.write("This is line 2\n")
file.close()
text_lines=["Chapter 3\n",
            "Sample text data file\n",
            "This is the third line of text\n",
            "The fourth line looks like this\n",
            "Edit the file with any text editor\n"]
file=open("data.txt","w")
file.writelines(text_lines)
file.close()

file=open("data.txt","r")
char=file.read(10)
print(char)
all_data=file.read()
print(all_data)
one_line=file.readline()
print(one_line)
all_data=file.readlines()
print(all_data)
"""
pygame.init()
screen=pygame.display.set_mode((6600,500))
pygame.display.set_caption("The Trivia Game")
font1=pygame.font.Font(None,40)
font2=pygame.font.Font(None,24)
white=255,255,255
cyan=0,255,255
yellow=255,255,0
purple=255,0,255
green=0,255,0
red=255,0,0

def print_text(font,x,y,text,color=(255,255,255),shadow=True):
    if shadow:
        imgText=font.render(text,True,(0,0,0))
        screen.blit(imgText,(x-2,y-2))
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))
class Trivia(object):
    def __init__(self,filename):
        self.data=[]
        self.current=0
        self.total=0
        self.correct=0
        self.score=0
        self.scored=False
        self.failed=False
        self.wronganswer=0
        self.restart=0
        self.colors=[white,white,white,white]
        #read trivia data from file
        f=open(filename,"r")
        trivia_data=f.readlines()
        f.close()
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total+=1

    def show_question(self):
        print_text(font1,210,5,"TRIVIA GAME")
        print_text(font2,190,500-20,"Press Keys (1-4) To Answer",purple)
        print_text(font2,530,5,"SCORE",purple)
        print_text(font2,550,25,str(self.score),purple)
        self.correct=int(self.data[self.current+5])
        question=self.current
        print_text(font1,5,80,"QUESTION "+str(question))
        print_text(font2,20,120,self.data[self.current],yellow)

        if self.scored:
            self.colors=[white,white,white,white]
            self.colors[self.correct-1]=green
            print_text(font1,230,380,"CORRECT",green)
            print_text(font2,170,420,"Press ENTER for next question",green)
        elif self.failed:
            self.colors=[white,white,white,white]
            self.colors[self.wronganswer-1]=red
            self.colors[self.correct-1]=green
            print_text(font1,220,380,"INCORRECT",red)
            print_text(font2,170,420,"Press Enter For Next Question",red)
        print_text(font1,5,170,"ANSWER")
        print_text(font2,20,210,"1 - "+self.data[self.current+1],self.colors[0])
        print_text(font2, 20, 240, "2 - " + self.data[self.current + 2], self.colors[1])
        print_text(font2, 20, 270, "3 - " + self.data[self.current + 3], self.colors[2])
        print_text(font2, 20, 300, "4 - " + self.data[self.current + 4], self.colors[3])
        if self.current == (self.total - 6) and (self.scord or self.failed):
            self.final_question()

    def handle_input(self,number):
        if not self.scored and not self.failed:
            if number==self.correct:
                self.scored=True
                self.score+=1
            elif number==self.restart:
                self.current=self.total
                self.next_question()
            else:
                self.failed=True
                self.wronganswer=number

    def next_question(self):
        if self.scored or self.failed:
            self.scord=False
            self.failed=False
            self.correct=0
            self.colors=[white,white,white,white]
            self.current+=6
            if self.current>=self.total:
                self.current=0

    def final_question(self):
        print_text(font2, 170, 440, "Press F5 to restart game,ESE to quit the game", red)

trivia=Trivia("trivia_data.text")
while True:
    for event in pygame.event.get():
        if event.Type==QUIT:
            sys.exit()
        elif event.Type==KEYUP:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            elif event.key==pygame.K_1:
                trivia.handle_input(1)
            elif event.key == pygame.K_2:
                trivia.handle_input(2)
            elif event.key == pygame.K_3:
                trivia.handle_input(3)
            elif event.key == pygame.K_4:
                trivia.handle_input(4)
            elif event.key==pygame.K_RETURN:
                trivia.next_question()
            elif event.key==pygame.K_F5:
                trivia.handle_input(0)
        screen.fill((0,0,200))
        trivia.show_question()
        pygame.display.update()