#Imports from libraries needed for the code to Function
import socket
from _thread import *
import pygame
from pyparsing import empty
from button import Button as B #Importing the Button Class from the button file
import pickle
from AppendQuiz import MyWindow as AppendWindow #Importing the Conents of the AppendQuiz File
from CreateQuiz import MyWindow as CreateWindow #Importing the Conents of the CreateQuiz File
from StartQuiz import MyWindow as StartWindow #Importing the Conents of the StartQuiz File
from DataAnalysis import MyWindow as Datawindow #Importing the Conents of the DataAnalysis File
from tkinter import *
from settings import * #Importing the Conents of the Settings File
from csv import writer


hostname = socket.gethostname()  #This gets the hostname 
ip_address = socket.gethostbyname(hostname) #This gets the IP Address
server = str(ip_address) #This shows the server
port = 5555 #Port to connect



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

class Server(): #The server class
        def __init__(self):
                #Initialising the Window/Frame
                pygame.init()
                self.screen = pygame.display.set_mode((Screen_width, Screen_height))
                pygame.display.set_caption(Caption)
                self.clock = pygame.time.Clock()
                self.run = True
                self.datax = ''
                
        


        def show_menu(self): #Menu procedure
                #Menu Initialisation
                self.screen.fill(bgcolour) #BG Colour
                self.draw_text(Caption, int(Screen_width*0.05) , black,Screen_width/2,Screen_height/4) #The Caption at the Top of the Window
               
                self.draw_text(("Join Code: "+server),int(Screen_width*0.05),black,Screen_width/2,Screen_height/8) #Where the Server UI displays the Join Code
                
                #Creating the Buttons for the Server UI
                self.Create_button = B(Screen_width*0.021,Screen_height*0.343,"CREATE A QUIZ",'#52de1b',30,Screen_width*0.452,Screen_height*0.206,"",self)
                self.Append_button = B(Screen_width*0.521,Screen_height*0.643,"APPEND TO A QUIZ",'#52de1b',30,Screen_width*0.452,Screen_height*0.206,"",self)
                self.Start_button = B(Screen_width*0.021,Screen_height*0.643,"START YOUR QUIZ",'#52de1b',30,Screen_width*0.452,Screen_height*0.206,"",self)
                self.Data_button = B(Screen_width*0.521,Screen_height*0.343,"DATA ANALYSIS",'#52de1b',30,Screen_width*0.452,Screen_height*0.206,"",self)
                self.Quit_button = B(Screen_width*0.42,Screen_height*0.9,"QUIT",'#52de1b',30,Screen_width*0.152,Screen_height*0.05,"",self)

                
                pygame.display.flip()       
                self.buttons = []

                #Initalising Buttons
                self.buttons.append(self.Create_button)
                self.buttons.append(self.Append_button)
                self.buttons.append(self.Start_button)
                self.buttons.append(self.Data_button)
                self.buttons.append(self.Quit_button)

               
                #Waiting for the Buttons to be clicked
                self.wait_for_click(self.buttons)

                self.buttons.clear()

                if self.Create_button.pressed: #If the Create Button is Pressed this will happen
                    
                    window=Tk()
                    mywin=CreateWindow(window)

                    #Initalising the Window/Frame
                    window.title('responseSmart | Create a Quiz')
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


                if self.Append_button.pressed : #If the Append Button is Pressed this will happen
                  

                    window=Tk()
                    mywin= AppendWindow(window)

                    #Initialising the Window/Frame
                    window.title('responseSmart | Append a Quiz')
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


                if self.Start_button.pressed: #If the Start Button is Pressed this will happen
                    
                        window=Tk()
                        startwin=StartWindow(window)

                        #Initalising the Window/Frame
                        window.title('responseSmart | Start Quiz')
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

                        
                        #Trying to get the filename
                        if not startwin.filename: 
                            pass
                        else:
                            self.filename = startwin.getFilename() #Getting the Ffilename
                            print('This is on server', self.filename)
                            self.run = False
                            self.datax = startwin.uploadQuiz() #Creating the Dicitonary for Questions
                            return

                        


                            
                if self.Data_button.pressed: #If the Data Analysis Button is Pressed this will happen
                    window=Tk()
                    mywin=Datawindow(window)

                    #Initalising the Window/Frame
                    window.title('responseSmart | Data Analysis')
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


                
                if self.Quit_button.pressed: #If the Quit Button is Pressed this will happen
                    pygame.quit() #Quits the code
                    quit()

        def draw_text(self,text, size, colour, x,y): #Draw Function for the UI
                self.fonte = pygame.font.match_font(writeFormat)
                self.font_forui = pygame.font.Font(self.fonte, size)
                self.text_surface = self.font_forui.render(text, True, colour)
                self.text_rect= self.text_surface.get_rect()
                self.text_rect.center = (x,y)
                self.screen.blit(self.text_surface, self.text_rect)
                
        def wait_for_click(self,buttons): #Waiting for Click Function
            waiting = True 
            while waiting:
                    
                self.clock.tick(60)
                for button in buttons:
                    button.draw() #Drawing the Buttons
                
                
                    if button.pressed:
                        waiting = False #If a Button is pressed, the buttons are no longer be redrawn
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: #If the UI is quit, the buttons will no longer be redrawn
                            waiting = False
                            self.run = False
                            quit()
                
                pygame.display.flip()




serverer = Server() #Calling on the Server
while serverer.run:

    serverer.show_menu() #Showing the Server UI once the code is started
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #If the Quit Button is Pressed this will happen
                
                pygame.quit() #The code is stopped, we QUIT the application



try: #Trying to connect to the clients
    s.bind((server, port)) #Binding to each client via the Network
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started") #Displayed once the server starts

questions = serverer.datax #The questions are eqaul to the Datax dicitionary located in serverer


idCount = 0 


def threaded_client(conn): #Function for sending the data
    global idCount
    conn.send(pickle.dumps(questions)) #Sending all the Questions to all Clients
    
    while True: 
        try:
            try:
                data = pickle.loads(conn.recv(2048)) #Recieving the Data from Client once quiz has ended
                studentname = data[0] #The Key of our dicitonary is the student name
                correct = data[1] #The First part of the definition is the Number of Correct Answers
                timetaken = round(data[3]) #The last part of the definition is the Time Taken to complete the Quiz

            except Exception as e:
                print(e)
            
            if not data: #Error reciving data from the client
                print("Error connecting with Student")
                break
            else:
                #Appending the recieived data from the client to a CSV file for the teahcer
                with open(serverer.filename, 'a') as f: 
                    w = writer(f)
                    w.writerow(data)
                break
        except:
            break

    conn.sendall(pickle.dumps("game ended")) #Telling the Client that their session has ended

    
    print("Lost connection with student" , studentname,'\n', correct," questions answered correctly\n",'Time taken to complete quiz',timetaken) #Server Side information
    idCount -= 1
    conn.close()




while True:
    conn, addr = s.accept() #Accepting connection to clients
    print("Connected to:", addr) #Prints who the server has connected to, show their address
    idCount +=1

    start_new_thread(threaded_client, (conn,))

