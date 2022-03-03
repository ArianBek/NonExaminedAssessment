#Import from the libraries needed for the code to Function
import pygame

class Window(): #Window Class Initialisied
    def __init__(self, question, answers): 
        
        self.question = question  #Gives the question
        
        self.options = list(answers)  #This gives all options
        self.answer = list(answers)[0] #This is the correct answer
        
        
    def getQ(self): #Function to return the Question to Client
        return self.question
        
    def getOptions(self): #Function to return the Incorrect Options to Client
        return self.options

    def getAnswers(self): #Function to return the Answer to Client
        return self.answer

    def draw(self, win):    #Function to Draw the window
        pygame.draw.rect(win, self.color, self.rect)

   

    def update(self):   #Function to update the look of the Window to Server/Client
        self.rect = (self.x, self.y, self.width, self.height)