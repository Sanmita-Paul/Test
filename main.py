import pygame
import random
#Initialization
pygame.init()
#create screen
screen=pygame.display.set_mode((1550,800))
running=True
#Background
back=pygame.image.load('back.jpg')           #loading the image you want to set as an icon
pygame.display.set_icon(back)
#Title and icon
pygame.display.set_caption("Space Invader")  #title of the window
icon=pygame.image.load('ship.png')           #loading the image you want to set as an icon
pygame.display.set_icon(icon)                #inserting the icon
#player
playerimg=pygame.image.load('ufo.png')
playerx=750             #x-coordinate of the ufo
playery=650             #y-coordinate of the ufo
playerx_change=0
def player(x,y):
    screen.blit(playerimg,(x,y))

#enemy
eimg=pygame.image.load('alien.png')
ex=random.randint(0,1550)            #x-coordinate of the alien
ey=random.randint(50,150)            #y-coordinate of the alien
ex_change=0.3
ey_change=40

#bullet
#ready: bullet is in position
#fire:bullet is fired
bimg=pygame.image.load('bullet.png')
bx=0
by=650
bx_change=0
by_change=10
b_state="ready"
def fire_b(x,y):
    global b_state
    b_state="fire"
    screen.blit(bimg,(x+16,y+10))
def enemy(x,y):
    screen.blit(eimg,(x,y))
#Gaming loop
while running:
    # RGB values for the screen background
    screen.fill((0, 0, 0))
    #back image
    screen.blit(back,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #to check whether the key pressed is left or right
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerx_change=-0.5
            if event.key == pygame.K_RIGHT:
                playerx_change=0.5
            if event.key==pygame.K_SPACE:
                fire_b(playerx,by)
            if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change=0
    playerx+=playerx_change
    #checking boundary for ufo
    if playerx<=0:
        playerx=0
    elif playerx>=1480:
        playerx=1480

    ex += ex_change
    #checking boundary for alien
    if ex <= 0:
        ex_change = 0.3
        ey+=ey_change
    elif ex >= 1480:
        ex_change = -0.3
        ey += ey_change
    #bullet movement
    if b_state is "fire":
        fire_b(playerx,by)
        by-=by_change

    player(playerx,playery)
    enemy(ex,ey)
    pygame.display.update()