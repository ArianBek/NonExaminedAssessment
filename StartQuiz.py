#Imports from libraries needed for the code to Function
from cProfile import label
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
import sys
import os

datax = {} #The Dicitonary where all the Questions will be stored and then sent to the server

from numpy import place, size
class MyWindow:
    def __init__(self, win):
        #Variables needed
        self.win = win
        self.filename = ""

        #Select File Function
        def open():
            global filename
            self.win.filenamez = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("csv files", "*.csv"),("all files", "*.*"))) #Opening the File Directory
            self.lbl6=Label(self.win, text=self.win.filenamez) #Displaying Selected FileName
           
            filedir = self.win.filenamez.split('/')[-1] #Name of File
            self.lbl6=Label(self.win, text=filedir) #Displaying Selected FileName
            self.lbl6.place(x=350,y=182) #Positioning the on Window Selected FileName
            print((self.win.filenamez).split(os.sep)[-1]) #Printing Path of File to Console


        #Initialising the Labels for the UI
        self.lbl1=Label(self.win, text='Your Teaching Name')
        self.lbl2=Label(self.win, text='Class Name')
        self.lbl3=Label(self.win, text='Quiz Name')
        self.lbl7=Label(self.win, text='Upload your responseSmart Quiz',font=("Arial", 30))
        self.lbl8=Label(self.win, text='Click the button below and select the file which holds your quiz.\n\nIf you would like to create or append a quiz click CLOSE to return to the main menu.')
        self.lbl11=Label(self.win, text='WARNING. Make sure all the fields have been entered correctly!\n\nMake sure you upload the quiz before starting the server!\n\nOnly click Upload Quiz once you have selected a file!',font=("Arial", 16))


        #Initialising the Entry Boxes for the UI
        self.t1=Entry(bd=3,width=60)
        self.t2=Entry(bd=3,width=60)
        self.t3=Entry(bd=3,width=60)


        #Positioning the Labels and Entry Boxes on the UI
        self.lbl1.place(x=140, y=260)
        self.t1.place(x=280, y=260)

        self.lbl2.place(x=170, y=300)
        self.t2.place(x=280, y=300)

        self.lbl3.place(x=170, y=340)
        self.t3.place(x=280, y=340)

        self.lbl11.place(x=290,y=420)

        self.lbl7.place(x=250,y=20)
        self.lbl8.place(x=260,y=80)

        #Linking the Buttons to Functions and Initialising them with Data
        self.b1=Button(self.win, text='Upload Quiz', command=self.uploadQuiz)
        self.b2=Button(self.win, text='Start Server', command=self.FetchEntry)
        self.b3=Button(self.win, text='Close',command=self.win.destroy)
        self.b4=Button(self.win, text='Open File',command=open)




        #Positioning the Buttons on the UI
        self.b1.place(x=170, y=600)
        self.b2.place(x=715, y=600)
        self.b3.place(x=463, y=600)
        self.b4.place(x=250, y=180)

    
    def FetchEntry(self): #Fetching the Created FileName 
        
            
        self.filename = (str(self.t2.get())+str(self.t3.get())+".csv") #Creating a FileName
        
        self.win.destroy()
        
    
        
        

    def getFilename(self): #Fetching the Filename of the Quiz
        return self.filename
        


    def uploadQuiz(self): #Uplaoding the Quiz to the Server
        print(self.win.filenamez)
        file_to_load = os.path.basename(self.win.filenamez)
        with open(file_to_load,'r') as data: #Opening the CSV File of the Question
            for line in csv.reader(data):
                try:
                    #Putting the Data from CSV file into Dictionary
                    new_key = line[0]
                    datax[new_key] = [line[1],line[2],line[3],line[4]]
                except IndexError:
                    pass
                
        return datax #Returning the Dictornary to the Server code






