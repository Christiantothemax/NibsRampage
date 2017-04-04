import pygame
import time
import random
import math



pygame.init()




display_width = 1000
display_height = 600
char_width = 41








roomone = pygame.image.load("F:\\Python\\Programs\\Firstgame\\Images\\roomone.png")
    
roomtwo = pygame.image.load("F:\\Python\\Programs\\Firstgame\\Images\\roomwithexit.png")

roomthree = pygame.image.load("F:\\Python\\Programs\\Firstgame\\Images\\roomthree.png")

roomfour = pygame.image.load("F:\\Python\\Programs\\Firstgame\\Images\\roomfour.png")

characterImage = pygame.image.load("F:\\Python\\Programs\\Firstgame\\Images\\main character1.png")



annoyingmonsternoise = pygame.mixer.Sound("F:\\Python\\Programs\\annoying_monster_noise.wav")

annoyingmonsternoise2 = pygame.mixer.Sound("F:\\Python\\Programs\\annoying_monster_noise2.wav")

pygame.mixer.music.load("F:\Python\Programs\divineinspiration.wav")
pygame.mixer.music.play(loops=-1)

screen = pygame.display.set_mode((display_width, display_height))



white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)

bright_red = (255,0,0)
bright_green = (0,255,0)

clock = pygame.time.Clock()


nibsImg = pygame.image.load("F:\\Python\\Programs\\Firstgame\\Images\\nibsthemonster.png")
nibs2Img = pygame.image.load("F:\\Python\\Programs\\Firstgame\\Images\\nibsthemonster.png")
nibs3lilImg = pygame.image.load("F:\\Python\\Programs\\Firstgame\\Images\\lilnibs.png")
nibs4Img = pygame.image.load("F:\\Python\\Programs\\Firstgame\\Images\\nibsthemonster.png")


nibs_width = 64
nibs_height = 70

lilnibs_width = 33
lilnibs_height = 36

def character(xx,yy):
    screen.blit(characterImage,(xx,yy))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
        
#def things_dodged(count):
#    font = pygame.font.SysFont(None, 25)
#    text = font.render("dodged: "+str(count), True, black)
#    gameDisplay.blit(text, (0,0))



def instructions_display(instructions):
    largeText = pygame.font.SysFont('arial',19)
    TextSurf, TextRect = text_objects(instructions, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(7)

   
   
def border():
    pygame.draw.line(screen, green, (0,0), (display_width, 0), 5)
    pygame.draw.line(screen, green, (display_width, 0), (display_width, display_height), 5)
    pygame.draw.line(screen, green, (display_width, display_height),(0, display_height),5)
##    pygame.draw.line(screen, green, (5,display_height),(5,400),5)
##    pygame.draw.line(screen, green, (5,0),(5,200),5)

def border2():
    
    pygame.draw.line(screen, green, (0,0), (display_width, 0), 5)
    pygame.draw.line(screen, green, (0,0), (0, display_height), 5)
    pygame.draw.line(screen, green, (display_width, display_height),(0, display_height),5)
##    pygame.draw.line(screen, green, (5,display_height),(5,400),5)
##    pygame.draw.line(screen, green, (5,0),(5,200),5)
    


def message_display(text):
    largeText = pygame.font.SysFont('arial',100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)

    game_loop() 



def dead():
    message_display("dead")

def runcredits():
    instructions_display("Credits:")
    screen.blit(roomone, (0,0))
    instructions_display("Castle Art - http://www.pd4pic.com/images/castle-knights-castle-stone-wall-tower.png")
    screen.blit(roomone, (0,0))
    instructions_display("Divine Inspiration by - free Songs for Game Developers at http://soundclick.com/share.cfm?id=12009927")
    screen.blit(roomone, (0,0))
    instructions_display("Special thanks to:")
    screen.blit(roomone,(0,0))
    instructions_display("Sentdex at youtube.com/Sentdex")
    screen.blit(roomone,(0,0))
    instructions_display(".. and Shields, for telling me I should learn python.")
    


def winner():
    instructions_display("You Win")
    screen.blit(roomone, (0,0))
    runcredits()
    game_intro()
    
    


def monster():



    # find normalized direction vector (dx, dy) between enemy and player
    #dx = x - xx
    #dist = math.hypot(dx, dy)
    #dx, dy = dx / dist, dy / dist
    # move along this normalized vector towards the player at current speed
    #x += dx * nibs_speed
    #y += dy * nibs_speed
    print()
 

    

def nibs(x,y):
    
 
    screen.blit(nibsImg, (x,y))

def nibs2(x_2,y_2):


    screen.blit(nibs3lilImg, (x_2,y_2))


def nibs3(x_3,y_3):


    screen.blit(nibs3lilImg, (x_3,y_3))

def nibs4(x_4,y_4):

  
    screen.blit(nibs4Img, (x_4,y_4))




def boxboss1(Lx, Ly):
    pygame.draw.rect(screen, blue, [Lx, Ly, 300, 300])

    return

def boxboss2(Lx_2, Ly_2):
    pygame.draw.rect(screen, blue, [Lx_2, Ly_2, 300, 300])

    return


def quitgame():
    pygame.quit()
    quit()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()

            
        
    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))




    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y +(h/2)))
    screen.blit(textSurf, textRect)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
        screen.blit(roomone,(0,0))
        largeText = pygame.font.SysFont('arial',55)
        TextSurf, TextRect = text_objects("NIBS RAMPAGE", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont('arial',55)
        TextSurf, TextRect = text_objects("(Press \"i\" in game for help)", largeText)
        TextRect.center = ((display_width/2),(display_height/1.5))
        screen.blit(TextSurf, TextRect)



        button("Start!",150,450,100,50,green,bright_green, game_loop)
        button("Quit",750,450,100,50,red,bright_red, quitgame)
        





        
        pygame.display.update()
        clock.tick(15)
 
def game_loop():


    
    char_height=50
    char_width=41
    nibs_speed= 7
    x=500
    y=100
    z=0
    x_2= 150
    x_3 = 400
    x_4 = -500
    y_2 = 1100
    y_3 = 700
    y_4 = 700

    Lx=0
    Ly=0
    Ly_2=-400
    Lx_2=-400
    xx=250
    yy=display_height-char_height -10



    x_change = 0
    y_change = 0

    

        
    Exit=False







    while not Exit:
        
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        
        
    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change += -15
                elif event.key == pygame.K_RIGHT:
                    x_change += 15
                elif event.key == pygame.K_UP:
                    y_change += -15
                elif event.key == pygame.K_DOWN:
                    y_change += 15

            #Pause
                if event.key == pygame.K_i:
                    instructions_display("Nibs is trying to get you! Find the safe zone and wait for nibs in order to trap him!")

                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0



        

        dx = xx-x
        dy = yy-y
        dist = math.hypot(dx, dy)
        dx = dx/dist
        dy = dy/dist
        x += dx * nibs_speed 
        y += dy * nibs_speed 



        
        xx += x_change
        yy += y_change


        



        if z == 0:
            screen.blit(roomone, (0,0))
            border2()

            if xx < 0:
                dead()
        
        if z == 1:
            screen.blit(roomtwo, (0,0))

            if x >= 780 - nibs_height and y < 380 and y > 196:
                x = 780 - nibs_height
                y = 300
                z=2
                
            border()
        

            if yy + char_width > display_height or yy < 0:
                dead()
        




        

# GAME PART 2 (NESTED)

        
        while z == 2:
            screen.blit(roomthree, (0,0))


            


            border()
            

        

            xx += x_change
            yy += y_change
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change += -17
                    elif event.key == pygame.K_RIGHT:
                        x_change += 17
                    elif event.key == pygame.K_UP:
                        y_change += -17
                    elif event.key == pygame.K_DOWN:
                        y_change += 17
                #Pause
                    if event.key == pygame.K_i:
                        instructions_display("Now try to get past lil' Nibs! Don't touch the green border!")
                        
        

        #NIBS2 (AKA lil'NIBS 2)
            dx_2 = xx-x_2
            dy_2 = yy-y_2
            dist_2 = math.hypot(dx_2, dy_2)
            dx_2 = dx_2/dist_2
            dy_2 = dy_2/dist_2
            x_2 += dx_2 * .07 * nibs_speed
            y_2 += dy_2 * 2.3 * nibs_speed
            

        #NIBS3 (AKA lil' NIBS)
            dx_3 = xx-x_3
            dy_3 = yy-y_3
            dist_3 = math.hypot(dx_3, dy_3)
            dx_3 = dx_3/dist_3
            dy_3 = dy_3/dist_3
            x_3 += dx_3 * .005 * nibs_speed
            y_3 += dy_3 * 2 * nibs_speed

            
        #NIBS4
            dx_4 = xx-x_4
            dy_4 = yy-y_4
            dist_4 = math.hypot(dx_4, dy_4)
            dx_4 = dx_4/dist_4
            dy_4 = dy_4/dist_4  
            x_4 += dx_4 * 2 * nibs_speed
            #Temporarily excluded             y_4 += dy_4 * .03 * nibs_speed

            







######GAME PART 3 NESTED

            if xx < 0:
                z += 1
                xx = display_width - char_width
                




                
            while z>=3:
                screen.blit(roomone, (0,0))

                xx += x_change
                yy += y_change






                
                
                if Lx <= 1080 and Lx >= 970:
                    Ly += 50
                if Ly <= 700 and Ly >= 570:
                    Lx -= 50
                if Lx >= -200 and Lx <= 20:
                    Ly -= 20
                if Ly >= -200 and Ly <= 20:
                    Lx+= 10


                if Lx_2 <= 680 and Lx_2 >= 570:
                    Ly_2 += 50
                if Ly_2 <= 300 and Ly_2 >= 170:
                    Lx_2 -= 50
                if Lx_2 >= -600 and Lx_2 <= -380:
                    Ly_2 -= 20
                if Ly_2 >= -600 and Ly_2 <= -380:
                    Lx_2 += 20


            #collision check for boxboss1
                if yy > Ly and yy < Ly + 300 or yy + char_height > Ly and yy + char_height <Ly+300:
                    print ("ycross")
                    if xx > Lx and xx < Lx + 300 or xx +char_width > Lx and xx + char_width < Lx +300:
                        dead()
                        

            #collision check for boxboss2
                if yy > Ly_2 and yy < Ly_2 + 300 or yy + char_height > Ly_2 and yy + char_height <Ly_2 + 300:
                    print ("ycross")
                    if xx > Lx_2 and xx < Lx_2 + 300 or xx + char_width > Lx_2 and xx + char_width < Lx_2 + 300:
                        dead()
                        


            #collision check walls
                if xx + char_width > display_width:
                    dead()
                if yy < 0 or yy + char_height > display_height:
                    dead()


                

                border()
                boxboss1(Lx, Ly)
                boxboss2(Lx_2, Ly_2)

                if xx < 0:
                    winner()
                    
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    
                
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x_change += -15
                        elif event.key == pygame.K_RIGHT:
                            x_change += 15
                        elif event.key == pygame.K_UP:
                            y_change += -15
                        elif event.key == pygame.K_DOWN:
                            y_change += 15

                    #pause
                        if event.key == pygame.K_i:
                            instructions_display("You're almost there! Make it past the magic defense blocks nibs created in order to make it home!")

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                            x_change = 0
                            y_change = 0


                        
                character(xx,yy)
                pygame.display.update()
                clock.tick(40)


#####END OF GAME PART 3

#END OF GAME PART 2



                
            
            nibs(x,y)
            nibs2(x_2,y_2)
            nibs3(x_3,y_3)
            nibs4(x_4,y_4)            
            character(xx,yy)
            pygame.display.update()
            clock.tick(40)


#NIBS2 KILL

            if xx + char_width > x_2 and xx < x_2 + lilnibs_width:
                print("x_2 crossover")
                if yy + char_height > y_2 and yy < y_2 + lilnibs_height:
                    print("dead")


                    annoyingmonsternoise2.play(loops=0, maxtime=0)
                    dead()


#NIBS3 KILL

            if xx + char_width > x_3 and xx < x_3 + lilnibs_width:
                 print("x_3 crossover")
                 if yy + char_height > y_3 and yy < y_3 + lilnibs_height:
                    print("dead")
                
                    annoyingmonsternoise2.play(loops=0, maxtime=0)
                    dead()

#NIBS 4KILL
            if xx + char_width > x_4 and xx < x_4 + nibs_width:
                print("x_4 crossover")
                if yy + char_height > y_4 and yy < y_4 + nibs_height:
                    print("dead")
                    
                    annoyingmonsternoise.play(loops=0, maxtime=0)
                    dead()
            


















                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0







            

            else:
               Exit = True
                    
                
            
        if xx >  display_width and z == 0:
            z+=1
            xx = char_width +6
            x -= display_width +6

                #collision check walls
        elif xx + char_width > display_width and z >=1:
           dead()
        elif yy < 5 or yy + char_height > display_height-5:
           dead()



        
            
        nibs(x,y)
        character(xx,yy)
        pygame.display.update()
        clock.tick(40)

        if xx + char_width > x and xx < x + nibs_width:
            print("x crossover")
            if yy + char_height > y and yy < y + nibs_height:
                print("dead")
                
                annoyingmonsternoise.play(loops=0, maxtime=0)
                dead()
                




game_intro()
game_loop()
pygame.quit()
quit()

