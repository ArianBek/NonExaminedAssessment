#Imports from libraries needed for the code to Function
import pygame, sys
import time

from settings import Screen_height, Screen_width #Importing the Conents of the Settings File

class Banner(pygame.sprite.Sprite): #Banner Class
    def __init__(self,x,y,text,colour,size,width,height,Game):
        #Initialising the Banner Information
        pygame.sprite.Sprite.__init__(self)
        self.pressed = False
        self.image = pygame.Surface((width,height))
        self.colour = colour
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.game = Game
        self.text  = text
        self.font = pygame.font.Font(None,size)
        self.text_surf = self.font.render(self.text,True,(100,43,200)) #This gives all options
        self.text_rect = self.text_surf.get_rect()
        

    def draw(self): #Drawing Function
        self.rect.topleft = (self.x,self.y) #Setting Position of Banner to top left corner
        self.text_rect.center = self.rect.center #Setting Position of Banner to centre
        pygame.draw.rect(self.game.screen,self.colour,self.rect,border_radius= 12) #Drawing the Banner
        self.game.screen.blit(self.text_surf,self.text_rect)
        

       

class Button(pygame.sprite.Sprite): #Button Class
    def __init__(self,x,y,text,colour,size,width,height,correct_answer,Game):
        #Initialising the Button Information
        pygame.sprite.Sprite.__init__(self)
        self.pressed = False
        self.image = pygame.Surface((width,height))
        self.colour = colour
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.correct_answer = correct_answer
        self.returnvalues = (False,'')
        self.is_clicked = False
        self.validation = ''
        self.game = Game
        self.text  = text
        self.font = pygame.font.Font(None,size)
        self.text_surf = self.font.render(self.text,True,(100,43,200)) #This gives all options
        self.text_rect = self.text_surf.get_rect()

        
    def draw(self): #Drawing Function
        self.rect.topleft = (self.x,self.y) #Setting Position of Button to top left corner
        self.text_rect.center = self.rect.center  #Setting Position of Button to centre
        pygame.draw.rect(self.game.screen,self.colour,self.rect,border_radius= 12) #Drawing the Button
        self.game.screen.blit(self.text_surf,self.text_rect)
        self.check_click() #Checking for button click
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos() #Get position of users mouse
        
        if self.rect.collidepoint(mouse_pos): #If the users mouse and a button collide
            
            self.colour = '#47b51b' #Change colour to this
            if pygame.mouse.get_pressed()[0]: #If the answer is pressed
                self.pressed = True
            else:
                if self.pressed == True:
                    self.is_clicked = True
                    if self.text == self.correct_answer:
                        self.validation = "Correct" #Correct
                        self.pressed = False
                        
                    else:
                        self.validation = "Incorrect" #Incorrect
                        self.pressed = False
                       
                    
                    
                self.returnvalues =  (self.is_clicked, self.validation) #Returning the Values
        else:
            
            self.colour = '#52de1b' #Reset Button Colour after the mouse leaves
            self.is_clicked = False
        
            
    def getReturnValues(self): #Return the Values Function
        return self.returnvalues        
