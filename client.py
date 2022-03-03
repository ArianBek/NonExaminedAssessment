#Imports from libraries needed for the code to Function
from numpy import empty
import pygame as pg
from network import Network #Importing the Network data from the network file
from window import Window #Importing the Window data from the window file
from button import Button as B #Importing the Button Class from the button file
from button import Banner #Importing the Banner Class from the button file
from settings import * #Importing the Conents of the Settings File
import random
from clientLobby import MyWindow as clientwindow #Importing the Conents of the clientLobby File
from tkinter import *
import time

class Game(): #Creating the Game Class
    def __init__(self):
        pg.init()
        #Setting all the Variables from the Self Initialisation Function
        self.screen = pg.display.set_mode((Screen_width, Screen_height))
        pg.display.set_caption(Caption)
        self.clock = pg.time.Clock()
        #self.font_name  = pg.font.match_font(font)
        self.answered_questions = []
        self.question_number = 1
        self.exit_mode = False
        self.answered_correctly = 0
        self.answered_incorrectly = 0
        self.totalquestion = 0
        self.startime = time.time()

    def get_Question_Srom_Server(self): #Getting Data from Server Function
        self.network = Network()
        
        self.starting_info = self.network.getQuestions() #Get the information sent from the server
        self.questions = self.starting_info #This is the whole question dictionary given from the server
        print(self.questions)
        
        self.totalquestion = len(self.questions)
        self.question_list = list(self.questions) #We turn all the keys (the questions) and put them all in a list
        
        

    def new(self): #Initalising the new Function
        while len(self.question_list) != 0: #When the length of the Questions list is NOT Zero
            random_question = random.randint(0,(len(self.questions)-1)) #Randomising the Question order
          
            question_selected = self.question_list[random_question] #Selecting a Random Question from the List
               
            self.window = Window(list(self.questions.keys())[random_question],list(self.questions.values())[random_question]) #Sending all the infomration to the Window for display
            print(question_selected) #Print the Question Selelcted to Console
            print(self.questions) #Print the Question data
            del self.questions[str(question_selected)] #Delete the Question from Dicitonary
            self.question_list.pop(random_question) #Pop the Question from the initial List of Questions
            question = self.window.getQ() #Get the Question from the Window
            answer = self.window.getAnswers() #Get the Answer from the Window
            options = self.window.getOptions() #Getting the Options from the Window

            shuffled_options = random.sample(options,len(options)) #Shuffling the Options (including answer) displayed to the Student
        
            self.banner_text = Banner(Screen_width*0,Screen_height*0.024,question,'#52de1b',30,Screen_width*1,Screen_height*0.206,self) #Writing to the Banner

            #Initialising the Option Buttons 
            self.optionA_button = B(Screen_width*0.021,Screen_height*0.343,shuffled_options[0],'#52de1b',30,Screen_width*0.452,Screen_height*0.206,answer,self)
            self.optionB_button = B(Screen_width*0.021,Screen_height*0.608,shuffled_options[1],'#52de1b',30,Screen_width*0.452,Screen_height*0.206,answer,self)
            self.optionC_button = B(Screen_width*0.527,Screen_height*0.343,shuffled_options[2],'#52de1b',30,Screen_width*0.452,Screen_height*0.206,answer,self)
            self.optionD_button = B(Screen_width*0.527,Screen_height*0.608,shuffled_options[3],'#52de1b',30,Screen_width*0.452,Screen_height*0.206,answer,self)

            self.buttonSprites = pg.sprite.Group() #Create a sprite group where you will sotre all the button sprites in one go so you can manipulate them easier
            self.buttonSprites.add(self.optionA_button,self.optionB_button,self.optionC_button,self.optionD_button) 
            self.running()

        
    # SEND ALL INFORMATION BACK TO SERVER FROM CLIENT

    def running(self): #The running function to check if the client is still at task
        self.run = True
        while self.run: #If the code is still running then everything below occurs
            self.clock.tick(fps)
            self.events()
            self.draw()
          
    def send_to_server(self): #Function to send the data to the server
        print(self.answered_questions) 
        self.answered_correctly = self.answered_questions.count("Correct") #Combining the Total number of Correct Answers
        self.answered_incorrectly = self.answered_questions.count("Incorrect") #Combining the Total number of Incorrect Answers
        self.timetaken = self.endtime-self.startime #Totalling the time taken for client to complete the quiz
        self.client_details = [self.student_name,self.answered_correctly,self.answered_incorrectly,self.timetaken] #Combining all of the Data from the client to a List
        self.network.send(self.client_details) #Sending the List to the Server


    def events(self): #Events Function
        
        for button in self.buttonSprites:
            button.draw() #Drawing each Button
            clicked = button.getReturnValues() #Reciving the Data from each button clicked
            
            
            if clicked[0]: #If the answer is clicked
                self.answered_questions.append(clicked[1]) #Append the students Answer to the Answered_Questions list
                self.question_number +=1 #Increment Question Number
                self.buttonSprites.empty() #Clear all the data in the buttons
                self.run = False
            
        for event in pg.event.get(): 
            if event.type == pg.QUIT: #If the Client Quits
                self.run = False #Stop running the code
                pg.quit() #Quit the UI
        
        if self.question_number-1 == self.totalquestion: #If All questions ahve been answered
            self.endtime = time.time() #Set the end time of the Time Taken to complete Quiz
            self.send_to_server() #Send the data to the server
            
            self.show_end_screen() #Show the End Screen UI
            

    def draw(self): #Drawing Function
        self.screen.fill((99, 173, 160)) #Background Fill
        self.banner_text.draw() #Drawing the Banner
        for button in self.buttonSprites: 
            button.draw() #Draw each Question

        
        question_no = str(self.question_number)+'/'+str(self.totalquestion) #The Question Indicator
        self.draw_text(question_no,60,(100,43,200),Screen_width/2,15*Screen_height/16) #Displaying the Question Indicator
        
        pg.display.update() #Updating the UI


    def draw_text(self, text, size, colour, x,y): #Drawing the Text Boxes
        #Initialising all of the Text box Attributes
        self.fonte = pg.font.match_font(writeFormat)
        self.font_forui = pg.font.Font(self.fonte, size)
        self.text_surface = self.font_forui.render(text, True, colour)
        self.text_rect= self.text_surface.get_rect()
        self.text_rect.center = (x,y)
        self.screen.blit(self.text_surface, self.text_rect)


    def show_menu(self): #The Student Lobby UI Function
        window=Tk()
        mywin=clientwindow(window)

        #Initialising the Window/Frame
        window.title('responseSmart | Student Lobby')
        window_width = 1000
        window_height = 700

        #Get the screen dimension
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        #Find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        #Set the position of the window to the center of the screen
        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        window.resizable(False, False)
        window.mainloop()

        #Setting the Student Name and Network Data from Join Code
        self.student_name = mywin.student_name
        self.network = mywin.JoinCode

        if mywin.joinQuiz: 
            return



       
    def show_end_screen(self): #End Screen UI Function
        self.screen.fill(bgcolour) #Initialising the Background
        #Initialising the Text Labels
        self.draw_text("The quiz has ended", 23, (0,0,0),Screen_width/2,Screen_height/4)
        self.draw_text(("You scored "+str(self.answered_correctly)+"out of "+str(self.answered_correctly+self.answered_incorrectly)), 23, (0,0,0),Screen_width/2,Screen_height/2)
        
        
        pg.display.flip()
        

        self.wait_for_key() #Calling the Waiting for the Input Function
       

        #Returning back to the Lobby
        self.run = False
        self.exit_mode = True
        pg.quit()
        quit()
        

    def wait_for_key(self): #Creating the  Waiting for the Input Function
        waiting = True
        while waiting:
            
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.run = False
                    quit()
                if event.type == pg.KEYUP:
                    waiting = False

game = Game() #Calling the Game Function
game.show_menu() #Calling the clientLobby UI
game.get_Question_Srom_Server() #Calling the Data from the Server

while not game.exit_mode: 

    print("new game is made") #Once the Client starts this is printed
    game.new()
    
