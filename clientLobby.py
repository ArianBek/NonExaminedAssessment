#Imports from libraries needed for the code to Function
from cProfile import label
from fileinput import filename
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
        #Variables needed
        self.win = win
        self.joinQuiz = False

        #Initialising the Labels for the UI
        self.lbl1=Label(self.win, text='Your Full Name')
        self.lbl2=Label(self.win, text='Join Code')
        self.lbl7=Label(self.win, text='responseSmart | Student Lobby',font=("Arial", 30))
        self.lbl8=Label(self.win, text='Join the responseSmart Quiz here!',font=("Arial", 20))
        self.lbl10=Label(self.win, text='Once you click Join Quiz the questions will begin.')
        self.lbl11=Label(self.win, text='To join the quiz please enter your Full name.\n\nPlease also enter the Join Code, your teacher should have this for you.')

        #Initialising the Entry Boxes for the UI
        self.t1=Entry(bd=3,width=60)
        self.t2=Entry(bd=3,width=60)

        #Positioning the Labels and Entry Boxes on the UI
        self.lbl1.place(x=170, y=260)
        self.t1.place(x=280, y=260)

        self.lbl2.place(x=170, y=300)
        self.t2.place(x=280, y=300)


        self.lbl10.place(x=350,y=350)
        self.lbl11.place(x=290,y=130)

        self.lbl7.place(x=315,y=20)
        self.lbl8.place(x=360,y=80)
        
        #Linking the Buttons to Functions and Initialising them with Data
        self.b1=Button(self.win, text='Leave Lobby', command=self.win.destroy)
        self.b2=Button(self.win, text='Join Quiz',command=self.FetchEntry)





        #Positioning the Buttons on the UI
        self.b1.place(x=170, y=400)
        self.b2.place(x=715, y=400)



    def FetchEntry(self): #Fetching the Entry
        print("Joining Quiz")
        #Linking the data from the entry boxes to variables
        self.student_name = self.t1.get() #
        self.JoinCode = self.t2.get()
        self.joinquiz = True
        self.win.destroy()

    def joinQuiz(self): #Joining Quiz Function
        return self.joinquiz
        
        




