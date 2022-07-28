from re import X
import pygame
import random

#pygame init
pygame.init()

#Pygame Window Name
pygame.display.set_caption('Bind - The Game of Luck')

#clock
clock = pygame.time.Clock()

#Images in Game
Die1 = pygame.image.load('Die-1.png')
Die2 = pygame.image.load('Die-2.png')
Die3 = pygame.image.load('Die-3.png')
Die4 = pygame.image.load('Die-4.png')
Die5 = pygame.image.load('Die-5.png')
Die6 = pygame.image.load('Die-6.png')

#Set Icon
pygame.display.set_icon(Die2)

#creating surface with dimension
surface = pygame.display.set_mode(( 1200, 900 ))

#import font
font = pygame.font.Font('freesansbold.ttf', 30)
font1 = pygame.font.Font('freesansbold.ttf', 45)
font2 = pygame.font.Font('freesansbold.ttf', 100)

#Running variable to control while True loop
running = True

#2d array
arr = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
x_coordinate = 0
y_coordinate = 0

#Die number
CurrentDie = 1
Rolling = False
Cycles = 0
Can_Roll = True

Score = 0

Die_number = {"1": True, "2": False, "3": False, "4": False, "5": False, "6": False}

Gameover = False
Reset = False
Stop = False

while running:

    #background colour
    surface.fill((253, 188, 180))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Reset:
                Reset = False
                Can_Roll = True
                Score = 0
                for q in range(5):
                    for p in range(5):
                        arr[q][p] = 0
        if event.type == pygame.MOUSEBUTTONDOWN:

            if 60.0 <= mouse[0] <= 260.0 and 550.0 <= mouse[1] <= 610.0:
                if Can_Roll:
                    Rolling = True
                    Rolled = random.randint(1, 6)
            if 300.0 <= mouse[0] < 1200.0 and 0 <= mouse[1] < 900 and Rolling == False and Can_Roll == False:
                x_coordinate = (mouse[0] - 300)//180
                y_coordinate = (mouse[1])//180
                if arr[x_coordinate][y_coordinate] == 0:
                    arr[x_coordinate][y_coordinate] = Rolled
                    Can_Roll = True
                    Score += 1

        if event.type == pygame.QUIT: #If Press Quit, Then Shut Down Window
            running = False

    #Rolling a die
    if Rolling:
        if CurrentDie == 1:
            Die_number["6"] = False
            Die_number["1"] = True
            clock.tick(20)
        elif CurrentDie == 2:
            Die_number["1"] = False
            Die_number["2"] = True
            clock.tick(20)
        elif CurrentDie == 3:
            Die_number["2"] = False
            Die_number["3"] = True
            clock.tick(20)
        elif CurrentDie == 4:
            Die_number["3"] = False
            Die_number["4"] = True
            clock.tick(20)
        elif CurrentDie == 5:
            Die_number["4"] = False
            Die_number["5"] = True
            clock.tick(20)
        elif CurrentDie == 6:
            Die_number["5"] = False
            Die_number["6"] = True
            clock.tick(20)

        if Cycles == 3 and CurrentDie == Rolled:
            Cycles = 0
            Rolling = False
            Can_Roll = False

        else:
            CurrentDie += 1

        if CurrentDie == 7:
            CurrentDie = 1
            Cycles += 1

    if Die_number["1"]:
        surface.blit(Die1, (100, 350))

    if Die_number["2"]:
        surface.blit(Die2, (100, 350))

    if Die_number["3"]:
        surface.blit(Die3, (100, 350))

    if Die_number["4"]:
        surface.blit(Die4, (100, 350))

    if Die_number["5"]:
        surface.blit(Die5, (100, 350))

    if Die_number["6"]:
        surface.blit(Die6, (100, 350))

    mouse = pygame.mouse.get_pos()

    #Roll feature
    pygame.draw.rect(surface, ((254, 219, 121)), [60, 550, 200, 60], 0)
    surface.blit(font.render("Roll", True , (0, 0, 0)), (125, 565))

    #Board Display
    for i in range (5):
        for n in range (5):
            if arr[i][n] is not 0:
                surface.blit(font2.render(str(arr[i][n]), True, (0, 0, 0)), (i*180 + 365, n*180 + 45))

    #Score Display
    surface.blit(font.render("Score: " + str(Score), True, (0, 0, 0)), (0, 850))

    #Division
    pygame.draw.line(surface, ((0, 0, 0)), (300, 0), (300, 900), 3)
    pygame.draw.line(surface, ((0, 0, 0)), (480, 0), (480, 900), 3)
    pygame.draw.line(surface, ((0, 0, 0)), (660, 0), (660, 900), 3)
    pygame.draw.line(surface, ((0, 0, 0)), (840, 0), (840, 900), 3)
    pygame.draw.line(surface, ((0, 0, 0)), (1020, 0), (1020, 900), 3)
    pygame.draw.line(surface, ((0, 0, 0)), (1200, 0), (1200, 900), 3)

    pygame.draw.line(surface, ((0, 0, 0)), (300, 180), (1200, 180), 3)
    pygame.draw.line(surface, ((0, 0, 0)), (300, 360), (1200, 360), 3)
    pygame.draw.line(surface, ((0, 0, 0)), (300, 540), (1200, 540), 3)
    pygame.draw.line(surface, ((0, 0, 0)), (300, 720), (1200, 720), 3)
    pygame.draw.line(surface, ((0, 0, 0)), (300, 900), (1200, 900), 3)

    #5 in a row
    for k in range(5):
        if arr[k][0] == arr[k][1] == arr[k][2] == arr[k][3] == arr[k][4] and arr[k][0] != 0:
            Score += 5
            for l in range(5):
                arr[k][l] = 0
        if arr[0][k] == arr[1][k] == arr[2][k] == arr[3][k] == arr[4][k] and arr[0][k] != 0:
            Score += 5
            for l in range(5):
                arr[l][k] = 0
    
    #Gameover detection
    for b in range(5):
        for c in range(5):
            if arr[b][c] != 0 and Stop == False:
                Gameover = True
                Stop = False
            else:
                Gameover = False
                Stop = True
    Stop = False
    if Gameover:
        Can_Roll = False
        Reset = True
        surface.blit(font1.render("Game Over", True, (0, 0, 0)), (0, 700))
        surface.blit(font.render("Press Space to reset", True, (0, 0, 0)), (0, 800))

    #tick
    clock.tick(60)

    #update
    pygame.display.update()

pygame.quit()