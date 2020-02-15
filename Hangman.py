import random
from tkinter import*
import csv

def initialization():
    global word, counter, counterText, wordLetters, completedLettersList, entryWidget, finishedGame
    finishedGame=False
    destroyGUI()
    entryWidget.pack()
    resetButton.pack()
    word=words[random.randint(0, len(words)-1)]
    counter=MAX_NUMBER_OF_LIVES
    updateCounter()
    guessedLetters.clear()
    wordLetters = list(word)
    completedLettersList=['_']*len(wordLetters)
    wordUpdate()

def wordUpdate():
    global wordText, completedLettersList,entryWidget
    for wordLetter in range(0, len(wordLetters)):
        if wordLetters[wordLetter] in guessedLetters:
            completedLettersList[wordLetter]=wordLetters[wordLetter]
    displayWord=" ".join(completedLettersList)
    wordText.pack_forget()
    wordText=Label(tk, text=displayWord, bg="black", fg="white")
    wordText.pack()
    if ('_' in completedLettersList)==False:
        text = "You Win! The word was " + word
        finalScreen(text)

def finalScreen(txt):
    global resetButton, winOrLoseText, counterText, finishedGame
    finishedGame=True
    destroyGUI()
    text=txt
    winOrLoseText=Label(tk, text=text, bg="black", fg="white")
    winOrLoseText.pack()
    resetButton = Button(tk, text="Reset Game", command=initialization)
    resetButton.pack()
    counterText.pack()
    wordText.pack()
    textGuessedLetters.pack()

def destroyGUI():
    global entryWidget, resetButton, counterText, wordText, textGuessedLetters, winOrLoseText
    entryWidget.pack_forget()
    resetButton.pack_forget()
    counterText.pack_forget()
    wordText.pack_forget()
    textGuessedLetters.pack_forget()
    winOrLoseText.pack_forget()

def checkLetter(guessedLetter):
    global notification, counter
    notificationText=""
    if guessedLetter in guessedLetters:
        notificationText="This letter was already guessed!"
    elif guessedLetter in wordLetters:
        notificationText="This letter is in the word!"
        guessedLetters.append(guessedLetter)
        updateGuessedLetters()
        wordUpdate()
    else:
        notificationText="This letter is wrong!"
        guessedLetters.append(guessedLetter)
        counter-=1
        updateGuessedLetters()
        updateCounter()
        wordUpdate()
    notification.pack_forget()
    notification=Label(tk, text=notificationText, bg="black", fg="white")
    if finishedGame:
        return
    notification.pack()

def updateGuessedLetters():
    global textGuessedLetters
    textGuessedLetters.pack_forget()
    text="Guessed letters: "+" ".join(guessedLetters)
    textGuessedLetters=Label(tk, text=text, bg="black", fg="white")
    textGuessedLetters.pack()

def updateCounter():
    global counterText, counter
    counterText.pack_forget()
    counterText = Label(tk, text=("Number Of Guesses Left: " + str(counter)), bg="black", fg="white")
    counterText.pack()
    if counter<1:
        text="You Lose! The word was " + word
        finalScreen(text)

def takeInput(event):
    global notification
    input=entryWidget.get().lower()
    if len(input)!=1:
        notification.pack_forget()
        notification=Label(tk, text="Please enter only one character!", bg="black", fg="white")
        notification.pack()
    else:
        checkLetter(input)


#words=["APPLE", "BANANA", "COOKIE", "DOG", "EAT"]
file=open("words.csv", "r")
listOfWords=file.read()
file.close()
words=listOfWords.split("\n")



word=''
counter=0
MAX_NUMBER_OF_LIVES=9
guessedLetters=[]
wordLetters=[]
completedLettersList=[]
displayGuessedLetters=[]

tk=Tk()
tk.geometry("300x300")
tk.title("Hangman")
tk.bind('<Return>', takeInput)
tk.configure(background="black")
labelOfGame=Label(tk, text="H A N G M A N", bg="black", fg="white")
labelOfGame.pack()
entryWidget=Entry(tk)
entryWidget.pack()
resetButton=Button(tk, text="Reset Game", command=initialization)
resetButton.pack()
counterText=Label(tk)
wordText=Label(tk)
notification=Label(tk)
textGuessedLetters=Label(tk)
textGuessedLetters=Label(tk, text="Guessed Letters: ", bg="black", fg="white")
textGuessedLetters.pack()
winOrLoseText=Label(tk)
finishedGame=False
initialization()


tk.mainloop()
