import Tkinter as tk
import tkMessageBox
from PIL import ImageTk, Image
import os
import random

class a():
    def __init__(self):
        self.Captcha = ''           #To hold the image name of the CAPTCHA that is selected randomly 
        self.Window = ''            #Main Window
        self.CaptchaLabel = ''      #Label to display the CAPTCHA
        self.CaptchaImg = ''        #To import the Image
        self.ReCaptchaButton = ''   #Recaptcha Button
        self.ReCaptchaImg = ''      #Recaptcha image that will be displayed on Recaptcha button
        self.WrongCaptchaCount = 0  #To store the count of Wrong Captcha that is entered by the user which is restricted to max value of 3
        self.ReCaptchaCount = 0     #To store the count of Recaptcha that is selected by the user which is restricted to max value of 3
        self.WrongPasswordCount = 0 #To store the count of wrong password that is entered by the user which is restricted to max value of 3
        self.Path = 'D:\Mini Project\Captchas\\'                       #To store the path of Captchas
        self.ReCaptchaPath = 'D:\Mini Project\Captchas\\recaptcha.gif'  #To store the path of Recaptcha image
        self.BgImagePath = 'D:\Mini Project\Captchas\\'  #To store the path of Background Image
        self.BgImage = ''       #To import Background Image 
        self.CaptchaPath = ''   #To store the path of randomly selected Captcha
        self.BgLabel = ''       #Label to display the background image
        self.CaptchaEntry = ''  #Entry to take the text in the Captcha
        self.CLabel = ''        #Label to display Captcha
        self.UIDEntry = ''      #Entry to take the User ID from the user
        self.UIDLabel = ''      #Label to display the "User ID"
        self.CaptchaCode = ''   #To store the Captcha Code entered by the user
        self.UID = ''           #To store the User ID eneterd by the user
        self.UIDText = ''       #To store the User ID eneterd by the user
        self.PasswordLabel = '' #Label to display the "password"
        self.PasswordEntry = '' #Entry to take the password from the user


    #Function which creates the Main Window and calls other function to create entries and labels
    def MainWindow(self):
        self.Window = tk.Tk()
        self.Window.title( 'Login' )
        self.BgImg()
        self.IPLabels()
        self.LoadCaptcha()
        self.Window.mainloop()
        

    #Function which creates background image in the Main Window
    def BgImg(self):
        self.BgImagePath = self.BgImagePath + random.choice(['Background1.gif','Background2.jpg'])
        self.BgImg = ImageTk.PhotoImage( Image.open( self.BgImagePath ) )
        self.BgLabel = tk.Label( self.Window, image=self.BgImg, width=444, height=250)
        self.BgLabel.grid(row=0,column=0)


    #Function which creates various Labels, Entries and Buttons
    def IPLabels(self):
        self.UIDLabel = tk.Label( self.BgLabel, text = 'User ID: ',bg="white", font = 'Times 10 bold')
        self.UIDLabel.grid( row = 0, column = 0, padx=(10,25), pady=(5,10))
        self.UID = tk.StringVar()
        self.UIDEntry = tk.Entry( self.BgLabel, textvariable = self.UID, bd=1 )
        self.UID.set(self.UIDText)
        self.UIDEntry.grid( row = 0, column = 1, padx=(30,35), pady=(5,10) )
        self.CLabel = tk.Label( self.BgLabel, text = 'Enter the text in above Captcha* ',bg="black",fg="white")
        self.CLabel.grid( row = 2, column = 1, padx=(27,27), pady=(10,10) )
        self.CaptchaCode = tk.StringVar()
        self.CaptchaEntry = tk.Entry( self.BgLabel, textvariable = self.CaptchaCode, bd=1 )
        self.CaptchaEntry.grid( row = 3, column = 1, padx=(5,5) )
        self.Submit = tk.Button( self.BgLabel, text = 'SUBMIT', command = self.VerifyCaptcha )
        self.Submit.grid( row = 4, column = 1, pady=(10,10))


    #Function to verify the Captcha entered by the User
    def VerifyCaptcha(self):
        self.UIDText = self.UID.get()
        CaptchaCodeText = self.CaptchaCode.get()
        if self.UIDText == '' :
            tkMessageBox.showinfo( 'Credentials', 'User ID can\'t be empty!!!' )
    
        elif CaptchaCodeText == '' :
            tkMessageBox.showinfo( 'Credentials', 'CAPTCHA can\'t be empty!!!' )
            
        elif CaptchaCodeText == self.Captcha[:-4] :
            tkMessageBox.showinfo( 'Sucess', 'Correct Captcha' )
            self.NewMainWindow()
            
        else :
            self.WrongCaptchaCount+=1
            tkMessageBox.showwarning( 'CAPTCHA', 'Wrong CAPTCHA' )
            if self.WrongCaptchaCount < 4 :
                self.CaptchaCodeText = ''
                self.LoadCaptcha()
                
            else :
                self.ExceededWrongCaptcha()


    #Function to refresh the current window and creates new labels and entries and prompts the user to enter password to login      
    def NewMainWindow(self):
        self.BgLabel.grid_forget()
        self.BgLabel = tk.Label( self.Window, image=self.BgImg, width=444, height=250)
        self.BgLabel.grid(row=0,column=0)
        self.UIDLabel = tk.Label( self.BgLabel, text = 'User ID:', font = 'Times 10 bold',bg="white" )
        self.UIDLabel.grid( row = 0, column = 0, padx=(10,25), pady=(10,15) )
        self.UIDEntry = tk.Label( self.BgLabel, text = self.UIDText, font = 'Times 10 bold', relief = 'solid',bg="white" )
        self.UIDEntry.grid( row = 0, column = 1, padx=(30,50), pady=(10,15) )
        self.PasswordLabel = tk.Label( self.BgLabel, text = 'Password: ',bg="white")
        self.PasswordLabel.grid( row = 1, column = 0)
        self.Password = tk.StringVar()
        self.PasswordEntry = tk.Entry( self.BgLabel, show='*', textvariable = self.Password)
        self.Password.set('')
        self.PasswordEntry.grid( row = 1, column = 1)
        self.Submit = tk.Button( self.BgLabel, text = 'Login', command = self.VerifyPassword )
        self.Submit.grid( row = 2, column = 1)
        

    #Function to verify the password entered by the user
    def VerifyPassword(self):
        Password = self.Password.get()
        if Password == '':
            tkMessageBox.showwarning( 'Credentials', 'Password can\'t be empty!!!' )
            
        elif Password == 'asdfg' :
            tkMessageBox.showinfo( 'Sucess', 'Login Successful' )
            self.Destroy()

        else :
            self.WrongPasswordCount+=1
            tkMessageBox.showwarning( 'Password', 'Wrong Password!!!' )
            if self.WrongPasswordCount > 3 :
                tkMessageBox.showerror( 'Limit', 'Wrong Password Limit Exceeded' )
                self.Destroy()
            else :
                self.NewMainWindow()
                

    #Function to import the image of the Captcha and the display it in the main window
    def LoadCaptcha(self):
        self.IPLabels()
        self.SelectCaptcha()
        self.CaptchaImg = ImageTk.PhotoImage( Image.open( self.CaptchaPath ) )
        self.CaptchaLabel = tk.Label( self.BgLabel, image = self.CaptchaImg, width=250, height=50 )
        self.CaptchaLabel.grid( row = 1, column = 1 )
        self.LoadReCaptcha()


    #Function to select the random Captcha
    def SelectCaptcha(self):
        self.Captcha = random.choice( os.listdir( self.Path ) )
        self.CaptchaPath = self.Path + '/' + self.Captcha
        if self.Captcha == 'recaptcha.gif' or self.Captcha == 'Background1.gif' or self.Captcha == 'Background2.jpg' or self.Captcha == 'Text Captcha Mini Project.py' :
            self.SelectCaptcha()


    #Function to import recaptcha image and put it on the button
    def LoadReCaptcha(self):
        self.ReCaptchaImg = ImageTk.PhotoImage( Image.open(self.ReCaptchaPath ) )
        self.ReCaptchaButton = tk.Button( self.BgLabel, image = self.ReCaptchaImg, width=30, height=30, relief='raised', command=self.CheckReCaptcha )
        self.ReCaptchaButton.grid( row = 1, column = 2, padx=(5,5) )


    #Function to check whether the Recaptcha Limit exceeded or not which gets called when Recaptcha button is pressed
    def CheckReCaptcha(self):
        self.ReCaptchaCount+=1
        if self.ReCaptchaCount>0 and self.ReCaptchaCount<4 :
            self.UIDText = self.UID.get()
            self.LoadCaptcha()
            
        else :
            self.ExceededReCaptcha()


    #Function to display the error message when Recaptcha Limit is exceeded
    def ExceededReCaptcha(self):
        tkMessageBox.showerror( 'Limit', 'Recaptcha Limit Exceeded' )
        self.Destroy()


    #Function to display error message when Wrong Captcha Limit is exceeded
    def ExceededWrongCaptcha(self):
        tkMessageBox.showerror( 'CAPTCHA', 'Wrong Captcha Limit Exceeded!!!' )
        self.Destroy()


    #Function to Destroy main window
    def Destroy(self) :
        self.Window.destroy()

b=a()
b.MainWindow()