import pygame
import random
from pygame.locals import*




#Functions
 
pygame.init()
 
window = pygame.display.set_mode((800,600))
 
pygame.display.set_caption("Collision Detection")
 
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)
 
clock = pygame.time.Clock()
 
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
 
    if (x2 + w2 >= x1 >= x2 and y2 +h2 >= y1 >= y2):
 
        return True
 
    elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):
 
        return True
 
    elif (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
 
        return True
 
    elif (x2 + w2 >= x1+ w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
 
        return True
 
    else:
 
        return False



    
pygame.init()

screen = pygame.display.set_mode((1000,1000))

pygame.display.set_caption("Battleship")

x = 50
y = 440
width = 10
height = 10
vel = 5

BattleshipX = 62.5
BattleshipY = 50
BattleshipWidth = 65.3
BattleshipHeight = 65.3


Location = list(range(1,49))

score = 0





run = True

while run:

            
    pygame.time.delay(50)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
    keys = pygame.key.get_pressed()


        

    if keys[pygame.K_a] and x > vel:
        x -= vel

    if keys[pygame.K_d] and x < 1000 - width - vel:
        x += vel

    if keys[pygame.K_w] and y > vel:
        y -= vel

    if keys[pygame.K_s] and y < 1000 - height - vel:
        y += vel

    collision = detectCollisions(x, y, width, height, BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight)
        
    screen.fill((0,0,0))    


    if Location == 1 or Location == 29:
        BattleshipX = 62.5
        BattleshipY = 50
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))
                         
    if Location == 2 or  Location == 4:
        BattleshipX = 125
        BattleshipY = 50
        BattleshipWidth = 65.3
        BattleshipHeight = 65.3
        Battleship2 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 3 or  Location == 17:
        BattleshipX = 187.5
        BattleshipY = 50
        BattleshipWidth = 65.3
        BattleshipHeight = 65.3
        Battleship3 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 4 or  Location == 36:
        BattleshipX = 250
        BattleshipY = 50
        BattleshipWidth = 65.3
        BattleshipHeight = 65.3
        Battleship4 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 5 or  Location == 12:
        BattleshipX = 312.5
        BattleshipY = 50
        BattleshipWidth = 65.3
        BattleshipHeight = 65.3
        Battleship5 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 6 or  Location == 1:
        BattleshipX = 375
        BattleshipY = 50
        BattleshipWidth = 65.3
        BattleshipHeight = 65.3
        Battleship6 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 7 or  Location == 30:
        BattleshipX = 437.5
        BattleshipY = 50
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship7 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 8 or Location == 46:
        BattleshipX = 62.5
        BattleshipY = 112.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship8 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 9 or Location == 41:
        BattleshipX = 125
        BattleshipY = 112.5
        BattleshipWidth  = 63.5
        BattleshipHeight = 63.5
        Battleship9 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 10 or Location == 21:
        BattleshipX = 187.5
        BattleshipY = 112.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship10 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 11 or Location == 18:
        BattleshipX = 250
        BattleshipY = 112.5
        BattleshipWidth = 63.5
        BattleHeight = 63.5
        Battleship11 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 12 or Location == 5:
        BattleshipX = 312.5
        BattleshipY = 112.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship12 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 13 or Location == 11:
        BattleshipX = 375
        BattleshipY = 112.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship13 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 14 or Location == 24:
        BattleshipX = 437.5
        BattleshipY = 112.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship14 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 15 or Location == 32:
        BattleshipX = 62.5
        BattleshipY = 175
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship15 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 16 or Location == 37:
        BattleshipX = 125
        BattleshipY = 175
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship16 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 17 or Location == 39:
        BattleshipX = 187.5
        BattleshipY = 175
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship18 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 18 or Location == 43:
        BattleshipX = 250
        BattleshipY = 175
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship19 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 19:
        BattleshipX = 312.5
        BattleshipY = 175
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship20 = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 20:
        BattleshipX = 375
        BattleshipY = 175
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship6b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 21:
        BattleshipX = 437.5
        BattleshipY = 175
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship6b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 22:
        BattleshipX = 62.5
        BattleshipY = 237.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 23:
        BattleshipX = 125
        BattleshipY = 237.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 24:
        BattleshipX = 187.5
        BattleshipY = 237.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    

    if Location == 25:
        BattleshipX = 250
        BattleshipY = 237.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 26:
        BattleshipX = 312.5
        BattleshipY = 237.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 27:
        BattleshipX = 375
        BattleshipY = 237.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 28:
        BattleshipX = 437.5
        BattleshipY = 237.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 29:
        BattleshipX = 62.5
        BattleshipY = 300
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 30:
        BattleshipX = 125
        BattleshipY = 300
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 31:
        BattleshipX = 187.5
        BattleshipY = 300
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 32:
        BattleshipX = 250
        BattleshipY = 300
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 33:
        BattleshipX = 312.5
        BattleshipY = 300
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 34:
        BattleshipX = 375
        BattleshipY = 300
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 35:
        BattleshipX = 437.5
        BattleshipY = 300
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 36:
        BattleshipX = 62.5
        BattleshipY = 362.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 37:
        BattleshipX = 125
        BattleshipY = 362.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 38:
        BattleshipX = 187.5
        BattleshipY = 362.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 39:
        BattleshipX = 250
        BattleshipY = 362.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 40:
        BattleshipX = 312.5
        BattleshipY = 362.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 41:
        BattleshipX = 375
        BattleshipY = 362.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 42:
        BattleshipX = 437.5
        BattleshipY = 362.5
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 43:
        BattleshipX = 62.5
        BattleshipY = 425
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 44:
        BattleshipX = 125
        BattleshipY = 425
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 45:
        BattleshipX = 187.5
        BattleshipY = 425
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 46:
        BattleshipX = 250
        BattleshipY = 425
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 47:
        BattleshipX = 312.5
        BattleshipY = 425
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))


    if Location == 48:
        BattleshipX = 375
        BattleshipY = 425
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    if Location == 49:
        BattleshipX = 437.5
        BattleshipY = 425
        BattleshipWidth = 63.5
        BattleshipHeight = 63.5
        Battleship1b = pygame.draw.rect(screen, (0, 0, 0), (BattleshipX, BattleshipY, BattleshipWidth, BattleshipHeight))

    
    


    
    Pointer = pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))

    pygame.draw.rect(screen, (255, 255, 255), (62.5, 50, 5, 440))
    pygame.draw.rect(screen, (255, 255, 255), (125, 50, 5, 440))
    pygame.draw.rect(screen, (255, 255, 255), (187.5, 50, 5, 440))
    pygame.draw.rect(screen, (255, 255, 255), (250, 50, 5, 440))
    pygame.draw.rect(screen, (255, 255, 255), (312.5, 50, 5, 440))
    pygame.draw.rect(screen, (255, 255, 255), (375, 50, 5, 440))
    pygame.draw.rect(screen, (255, 255, 255), (437.5, 50, 5, 440))
    pygame.draw.rect(screen, (255, 255, 255), (500, 50, 5, 440))
    pygame.draw.rect(screen, (255, 255, 255), (62.5, 50, 440, 5))
    pygame.draw.rect(screen, (255, 255, 255), (62.5, 112.5, 440, 5))
    pygame.draw.rect(screen, (255, 255, 255), (62.5, 175, 440, 5))
    pygame.draw.rect(screen, (255, 255, 255), (62.5, 237.5, 440, 5))
    pygame.draw.rect(screen, (255, 255, 255), (62.5, 300, 440, 5))
    pygame.draw.rect(screen, (255, 255, 255), (62.5, 362.5, 440, 5))
    pygame.draw.rect(screen, (255, 255, 255), (62.5, 425, 440, 5))
    pygame.draw.rect(screen, (255, 255, 255), (62.5, 487.5, 440, 5))



    if collision == False:
        pygame.draw.rect(screen,(255, 255, 255), (x, y, 10, 10))



    if keys[pygame.K_SPACE] and collision == False:
        print("Miss")
        pygame.draw.rect(screen,(255, 0, 0), (x, y, 10, 10))
        score = score - 1
        
        
    if keys[pygame.K_SPACE] and collision == True:
        print("Hit")

        score = score + 1 

        import random
        randomN = random.randint(1,49)
        Location = randomN


    if score == 3:
        print("You win!! With a score of ")
        print(score)
        Again = input("Try again?")

        if Again.lower() == 'yes':
            print ("Great")
            x = 50
            y = 440
            width = 10
            height = 10
            score = 0

        if Again.lower() == 'no':
            print("Okay, bye")
            run = False

    elif score == -3:
        print("You lose with a score of ")
        print(score)
        Again = input("Try again?")

        if Again.lower() == 'yes':
            print("Great")
            x = 50
            y = 440
            width = 10
            height = 10
            score = 0

        if Again.lower() == 'no':
            print("Okay, Bye")
            run = False

            
            


    pygame.display.update()



pygame.quit()

