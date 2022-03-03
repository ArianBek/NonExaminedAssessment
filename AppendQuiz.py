#Imports from libraries needed for the code to Function
from cProfile import label
from fileinput import close, filename
from logging import root
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from ast import Pass, Return
from genericpath import isfile
from ntpath import join
from re import X
from unittest import addModuleCleanup
from csv import writer
import os

from numpy import place, size
class MyWindow:
    def __init__(self, win):
        #Variable needed
        self.win = win

        #Select File Function
        def open():
            global filename
            self.win.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("csv files", "*.csv"),("all files", "*.*"))) #Opening the File Directory
            self.lbl6=Label(self.win, text=self.win.filename) #Displaying Selected FileName
            filedir = self.win.filename.split('/')[-1] #Name of File
            self.lbl6=Label(self.win, text=filedir) #Displaying Selected FileName
            self.lbl6.place(x=350,y=182) #Positioning the on Window Selected FileName
            print((self.win.filename).split(os.sep)[-1]) #Printing Path of File to Console

        #Initialising the Labels for the UI
        self.lbl1=Label(self.win, text='Question')
        self.lbl2=Label(self.win, text='Answer')
        self.lbl3=Label(self.win, text='Option 1')
        self.lbl4=Label(self.win, text='Option 2')
        self.lbl5=Label(self.win, text='Option 3')
        self.lbl7=Label(self.win, text='Welcome to the responseSmart Quiz Creator',font=("Arial", 30))
        self.lbl8=Label(self.win, text='To add more questions to an exisiting file, select the file using the button below.\n\nOtherwise click CLOSE to return to the main menu to create a new file.')
        self.lbl11=Label(self.win, text='WARNING. Make sure all the fields have been entered correctly!\n Once you click Save Question you can not edit the question and it will be saved to your file.\nOnly click Save Question once, clicking it more times with make the same question reoccur!')


        #Initialising the Entry Boxes for the UI
        self.t1=Entry(bd=3,width=60)
        self.t2=Entry(bd=3,width=60)
        self.t3=Entry(bd=3,width=60)
        self.t4=Entry(bd=3,width=60)
        self.t5=Entry(bd=3,width=60)

        #Positioning the Labels and Entry Boxes on the UI
        self.lbl1.place(x=170, y=260)
        self.t1.place(x=280, y=260)

        self.lbl2.place(x=170, y=300)
        self.t2.place(x=280, y=300)

        self.lbl3.place(x=170, y=340)
        self.t3.place(x=280, y=340)

        self.lbl4.place(x=170, y=380)
        self.t4.place(x=280, y=380)

        self.lbl5.place(x=170, y=420)
        self.t5.place(x=280, y=420)

        self.lbl11.place(x=220,y=480)

        self.lbl7.place(x=150,y=20)
        self.lbl8.place(x=260,y=80)
        
        #Linking the Buttons to Functions and Initialising them with Data
        self.b1=Button(self.win, text='Save Question', command=self.saveQuestion)
        self.b2=Button(self.win, text='New Question', command=self.nextQuestion)
        self.b3=Button(self.win, text='Close',command=self.win.destroy)
        self.b4=Button(self.win, text='Open File',command=open)




        #Positioning the Buttons on the UI
        self.b1.place(x=170, y=600)
        self.b2.place(x=715, y=600)
        self.b3.place(x=463, y=600)
        self.b4.place(x=250, y=180)

    
    def nextQuestion(self): #New Question Function
        #Clearing all the Entry Boxes
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.t4.delete(0, END)
        self.t5.delete(0, END)


    def saveQuestion(self): #Save Question Function
        #Linking the data from the entry boxes to variables
        question = str(self.t1.get())
        answer = self.t2.get()
        option1 = self.t3.get()
        option2 = self.t4.get()
        option3 = self.t5.get()
        enlist = [question,answer,option1,option2,option3] #Placing all the data from entry boxes into a List
        print(enlist)

        file_to_load = (self.win.filename).split(os.sep)[-1] #Filename needed to load CSV file

        writetoCSV = ','.join(enlist) #Turning the List into a CSV Format
        print(writetoCSV)
        with open(file_to_load, 'a') as f: #Appending to the CSV File
            w = writer(f)
            w.writerow(enlist) #Writing the list for each row






