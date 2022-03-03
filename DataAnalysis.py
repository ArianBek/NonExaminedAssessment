#Imports from libraries needed for the code to Function
from cProfile import label
from calendar import c
from cgitb import text
from logging import root
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from ast import Pass, Return
from genericpath import isfile
from ntpath import join
from re import X
from unittest import addModuleCleanup
from csv import reader
import csv
import os
import matplotlib.pyplot as plt


datax = {} #The Dicitonary where all the Questions will be stored and then sent to the server


from numpy import place, size
class MyWindow:
    def __init__(self, win):
        #Variables needed
        self.win = win

        #Select File Function
        def openStudent():
            global Studentfilename
            self.win.Studentfilename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("csv files", "*.csv"),("all files", "*.*"))) #Opening the File Directory
            filedir = self.win.Studentfilename.split('/')[-1] #Displaying Selected FileName
            self.lbl6=Label(self.win, text=filedir) #Name of File
            self.lbl6.place(x=350,y=182) #Positioning the on Window Selected FileName
            print((self.win.Studentfilename).split(os.sep)[-1]) #Printing Path of File to Console

        #Opening File button Initialisation and Placing and linking to Function
        self.b4=Button(win, text='Open Student File',command=openStudent)
        self.b4.place(x=200, y=180)


        #Initialising the Labels for the UI
        self.lbl7=Label(self.win, text='responseSmart | Data Analysis',font=("Arial", 30))
        self.lbl8=Label(self.win, text='At the end of each quiz you have hosted, a file is  genereated; the StudentAnalysis File.\n\nUpload the file below to generate a report.')
        self.lbl11=Label(self.win, text='WARNING. Make sure you have uploaded the file before generating the data report!',font=("Arial", 16))
        self.lbl12=Label(self.win, text='You can only access one report at a time. Close a report to open another.',font=("Arial", 13))

        #Positioning the Labels and Entry Boxes on the UI
        self.lbl11.place(x=200,y=240)
        self.lbl12.place(x=275,y=400)
        self.lbl7.place(x=240,y=20)
        self.lbl8.place(x=230,y=80)
        
        #Linking the Buttons to Functions and Initialising them with Data
        self.b1=Button(self.win, text='Student Scores', command=self.StudentsScore)
        self.b3=Button(self.win, text='Close',command=self.win.destroy)
        self.b4=Button(self.win,text='Number of Incorrect Answers',command=self.StudentsIncorrect)
        self.b5=Button(self.win,text='Calculated Percentage Score',command=self.ResultPercentage)
        self.b6=Button(self.win,text='Time Taken to Complete',command=self.TimeTakenToComplete)
        self.b7=Button(self.win,text='Time Spent per Question',command=self.TimeTakenPerQ)
        self.b8=Button(self.win,text='Overall Decisiveness Report',command=self.DecisiveReport)




        #Positioning the Buttons on the UI
        self.b1.place(x=140, y=300)
        self.b3.place(x=463, y=600)
        self.b4.place(x=300, y=300)
        self.b5.place(x=545, y=300)
        self.b6.place(x=140, y=350)
        self.b7.place(x=400, y=350)
        self.b8.place(x=665, y=350)




    def DecisiveReport(self): #Decisive Report Function
        
        z = (self.win.Studentfilename).split(os.sep)[-1] #Filename
        counter = 0 
        with open(z,'r') as data: #Opening the File
            for line in csv.reader(data):
                counter = counter + 1 #Incrementing the Counter for Average

        x = [] #X co-ordinate list
        y = [] #Y co-ordinate list
        total = 0 #Total of all the data
        average = 0 #Initialising the Average Variable


        with open(z,'r') as data: #Opening the File
            for line in csv.reader(data): #For each row in the File
                try:

                    percentage = (int(line[1])+int(line[2])/(float(line[3])/counter)) #Calculation for Decivieness
                    x.append(line[0]) #Append Student Name to x-coordinate list
                    y.append(percentage) #Append Calculation to y-coordinate list
                    total = total + percentage #Calculating the Total of calcuations for all students
                except IndexError:
                    pass
            average = total/counter #Calculating the Average

        
        #Plotting the points
        plt.stem(x, sorted(y))
        
        #Naming the x axis
        plt.xlabel('Student Names')
        plt.xticks(rotation=90)
        #Naming the y axis
        plt.ylabel('Percentage')
        
        #Giving a title to the graph
        plt.suptitle('Calculated Percentage of Decisiveness')
        #Displaying the average to the graph
        title = ('Average Percentage;',str(average)+'%')
        plt.title(title)
        
        #Function to show the plot
        plt.show()

    def TimeTakenPerQ(self) : #Time Taken per Question Report Function

        z = (self.win.Studentfilename).split(os.sep)[-1] #Filename
        counter = 0
        with open(z,'r') as data: #Opening the File
            for line in csv.reader(data):
                counter = counter + 1 #Incrementing the Counter for Average

        x = [] #X co-ordinate list
        y = [] #Y co-ordinate list
        total = 0 #Total of all the data
        average = 0 #Initialising the Average Variable


        with open(z,'r') as data: #Opening the File
            for line in csv.reader(data): #For each row in the File
                try:
                   
                
                    x.append(line[0]) #Append Student Name to x-coordinate list
                    y.append(float(line[3])/counter) #Calculation for Time Taken Per Question 
                    total = total + (float(line[3])/counter) #Calculating the Total of calcuations for all students
                except IndexError:
                    pass
            average = total/counter #Calculating the Average

        
        #Plotting the points
        plt.stem(x, sorted(y))
        
        #Naming the x axis
        plt.xlabel('Student Names')
        plt.xticks(rotation=90)
        #Naming the y axis
        plt.ylabel('Time Taken per Question')
        
        #Giving a title to my graph
        plt.suptitle('Time Taken per Question')
        #Displaying the average to the graph
        title = ('Average Time to answer a Question;',str(average),'seconds')
        plt.title(title)
        
        #Function to show the plot
        plt.show()

    def TimeTakenToComplete(self): #Time Taken to complete Quiz Report Function

        x = [] #X co-ordinate list
        y = [] #Y co-ordinate list
        counter = 0 #Initialising the Counter Variable
        total = 0 #Total of all the data
        average = 0 #Initialising the Average Variable

        z = (self.win.Studentfilename).split(os.sep)[-1] #Filename
        with open(z,'r') as data: #Opening the File
            for line in csv.reader(data): #For each row in the File
                try:
                    
                
                    counter = counter + 1 #Increment Counter
                    x.append(line[0]) #Append Student Name to x-coordinate list
                    y.append(line[3]) #Append Time Taken to Complete to y-coordinate list
                    total = total + float(line[3]) #Calculating the Total of calcuations for all students
                except IndexError:
                    pass
            average = total/counter #Calculating the Average

        
        #Plotting the points
        plt.stem(x, sorted(y))
        
        #Naming the x axis
        plt.xlabel('Student Names')
        plt.xticks(rotation=90)
        #Naming the y axis
        plt.ylabel('Time to complete the Quiz')
        
        #Giving a title to my graph
        plt.suptitle('Time Taken to complete the Quiz')
        #Displaying the average to the graph
        title = ('Average Time over Correct Answers;',str(average),'seconds')
        plt.title(title)
        
        #Function to show the plot
        plt.show()

    
    def ResultPercentage(self): #Result Percentage Quiz Report Function

        x = [] #X co-ordinate list
        y = [] #Y co-ordinate list
        counter = 0 #Initialising the Counter Variable
        total = 0 #Total of all the data
        average = 0 #Initialising the Average Variable

        z = (self.win.Studentfilename).split(os.sep)[-1] #Filename
        with open(z,'r') as data: #Opening the File
            for line in csv.reader(data): #For each row in the File
                try:
                    
                
                    counter = counter + 1 #Increment Counter

                    percentage = (100*((int(line[1]))/(int(line[1])+int(line[2])))) #Calculation for Percentage
                    x.append(line[0]) #Append Student Name to x-coordinate list
                    y.append(percentage)  #Append Calculation to y-coordinate list
                    total = total + percentage #Calculating the Total of calcuations for all students
                except IndexError:
                    pass
            average = total/counter #Calculating the Average

        
        #Plotting the points
        plt.stem(x, sorted(y))
        
        #Naming the x axis
        plt.xlabel('Student Names')
        plt.xticks(rotation=90)
        #Naming the y axis
        plt.ylabel('Percentage')
        
        #Giving a title to my graph
        plt.suptitle('Calculated Percentage Score')
        #Displaying the average to the graph
        title = ('Average Percentage Score;',str(average)+'%')
        plt.title(title)
        
        #Function to show the plot
        plt.show()


    def StudentsScore(self): #Student Score Report Function

        x = [] #X co-ordinate list
        y = [] #Y co-ordinate list
        counter = 0 #Initialising the Counter Variable
        total = 0 #Total of all the data
        average = 0 #Initialising the Average Variable

        z = (self.win.Studentfilename).split(os.sep)[-1] #Filename
        with open(z,'r') as data: #Opening the File
            for line in csv.reader(data): #For each row in the File
                try:
                    counter = counter + 1 #Increment Counter

                    x.append(line[0]) #Append Student Name to x-coordinate list
                    y.append(line[1]) #Append Number of Correct Answers to Complete to y-coordinate list
                    total = total + int(line[1]) #Calculating the Total of calcuations for all students
                except IndexError:
                    pass
                
            average = total/counter #Calculating the Average

        
        #Plotting the points
        plt.stem(x, sorted(y))
        
        #Naming the x axis
        plt.xlabel('Student Names')
        plt.xticks(rotation=90)
        #Naming the y axis
        plt.ylabel('Scores')
        
        #Giving a title to my graph
        plt.suptitle('Student Scores')
        #Displaying the average to the graph 
        title = ('Average Student Score;',str(average))
        plt.title(title)
        
        #Function to show the plot
        plt.show()


    def StudentsIncorrect(self): #Student Incorrect Score Report Function


        x = [] #X co-ordinate list
        y = [] #Y co-ordinate list
        counter = 0 #Initialising the Counter Variable
        total = 0 #Total of all the data
        average = 0 #Initialising the Average Variable

        z = (self.win.Studentfilename).split(os.sep)[-1] #Filename
        with open(z,'r') as data: #Opening the File
            for line in csv.reader(data): #For each row in the File
                try:
                    
                
                    counter = counter + 1 #Increment Counter

                    x.append(line[0]) #Append Student Name to x-coordinate list
                    y.append(line[2])  #Append Number of Incorrect Answers to Complete to y-coordinate list
                    total = total + int(line[2]) #Calculating the Total of calcuations for all students
                except IndexError:
                    pass
            average = total/counter #Calculating the Average

        
        #Plotting the points
        plt.stem(x, sorted(y))
        
        #Naming the x axis
        plt.xlabel('Student Names')
        plt.xticks(rotation=90)
        #Naming the y axis
        plt.ylabel('Number of Answers Incorrect')
        
        #Giving a title to my graph
        plt.suptitle('Student Incorret Scores')
        #Displaying the average to the graph 
        title = ('Average Incorrect Score;',str(average))
        plt.title(title)
        
        #Function to show the plot
        plt.show()







