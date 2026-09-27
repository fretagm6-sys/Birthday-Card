import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greetings Card")

img=pygame.image.load("images/backgroundone.jpg")

while True:
    font=pygame.font.SysFont("Times New Roman",72)
    screen.fill(255,255,255)
    screen.blit(img,(0,0))
    text1=font.render("Happy",True,(0,0))
    text2=font.render("Birthday",True,(0,0))
    screen.blit(text1,(210,180))
    screen.blit(text2,(180,261))
    pygame.display.update()
    time.sleep(2)
    
    

