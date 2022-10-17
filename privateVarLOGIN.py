from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("Private Variable Login")
root.config(bg="#36413E")

name = Label(root, text="Name", fg="#D7D6D6", bg="#36413E", font=("Comic Sans MS", "23", "bold"))
name.place(relx=0.25, rely=0.2, anchor=CENTER)

nameEntry = Entry(root, fg="#D7D6D6", font=("Comic Sans MS", "23", "bold"))
nameEntry.place(relx=0.57, rely=0.2, anchor=CENTER)

password = Label(root, text="Password", fg="#D7D6D6", bg="#36413E", font=("Comic Sans MS", "23", "bold"))
password.place(relx=0.25, rely=0.4, anchor=CENTER)

passwordEntry = Entry(root, fg="#D7D6D6", font=("Comic Sans MS", "23", "bold"))
passwordEntry.place(relx=0.59, rely=0.4, anchor=CENTER)

captcha = Label(root, text="Captcha", fg="#D7D6D6", bg="#36413E", font=("Comic Sans MS", "23", "bold"))
captcha.place(relx=0.25, rely=0.6, anchor=CENTER)

captchaEntry = Entry(root, fg="#D7D6D6", font=("Comic Sans MS", "23", "bold"))
captchaEntry.place(relx=0.58, rely=0.6, anchor=CENTER)

usernameDisplay = Label(root, fg="#D7D6D6", bg="#36413E", font=("Comic Sans MS", "23", "bold"))
usernameDisplay.place(relx=0.5, rely=0.8, anchor=CENTER)

passwordDisplay = Label(root, fg="#D7D6D6", bg="#36413E", font=("Comic Sans MS", "23", "bold"))
passwordDisplay.place(relx=0.5, rely=0.875, anchor=CENTER)

captchaDisplay = Label(root, fg="#D7D6D6", bg="#36413E", font=("Comic Sans MS", "23", "bold"))
captchaDisplay.place(relx=0.5, rely=0.95, anchor=CENTER)

class userDB():
    def __init__(self, username, password, captcha):
        self.__username = username
        self.__password = password
        self.__captcha = captcha

    def showUser(self):
        usernameDisplay['text'] = "Name: " + self.__username
        passwordDisplay['text'] = "Password: " + self.__password
        captchaDisplay['text'] = "Captcha: " + self.__captcha
        
userDB = userDB(nameEntry.get(), passwordEntry.get(), captchaEntry.get())

def addUser():
    global userDB
    userDB.username = nameEntry.get()
    userDB.password = passwordEntry.get()
    userDB.captcha = captchaEntry.get()
    usernameDisplay['text'] = "Name: " + nameEntry.get()
    passwordDisplay['text'] = "Password: " + passwordEntry.get()
    captchaDisplay['text'] = "Captcha: " + captchaEntry.get()
    print("Details Updated")

button1 = Button(root, text="Update Login Info", height = 1, width=15, fg="#D7D6D6", bg="#BEB2C8", font=("Comic Sans MS", "15", "bold"), command=userDB.showUser)
button1.place(relx=0.3, rely=0.7, anchor=CENTER)

button2 = Button(root, text="Display Login Info", height = 1, width=15, fg="#D7D6D6", bg="#BEB2C8", font=("Comic Sans MS", "15", "bold"), command=addUser)
button2.place(relx=0.7, rely=0.7, anchor=CENTER)

root.mainloop()