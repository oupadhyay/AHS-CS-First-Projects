#Hangman Game
#Created By Devang Bhatnagar
#Random is used to randomly select words. Tkinter is used to create GUI. CSV is used to get words.
import random
from tkinter import*
import csv

#This function starts/resets the game. It starts with a clean GUI and a randomly selected word. Lives are reset. Guessed letters are cleared.
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

#This function takes the player's input. It only accepts the player's input if the player's input is only one character long.
def takeInput(event):
    global notification
    input=entryWidget.get().lower()
    if len(input)!=1:
        notification.pack_forget()
        notification=Label(tk, text="Please enter only one character!", bg="black", fg="white")
        notification.pack()
    else:
        checkLetter(input)

#This function checks the player's input and gives a response based on that. It tells the player if the letter was already guessed,
#if the letter is in the word, or if the letter is not in the word.
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

#This function updates the progress on the completion of finding a word. Unfound letters are marked as a "_" while found letters
#are written in their letters.
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

#This function updates the number of lives displayed on screen.
def updateCounter():
    global counterText, counter
    counterText.pack_forget()
    counterText = Label(tk, text=("Number Of Guesses Left: " + str(counter)), bg="black", fg="white")
    counterText.pack()
    if counter<1:
        text="You Lose! The word was " + word
        finalScreen(text)

#This function updates the list of guessed letters.
def updateGuessedLetters():
    global textGuessedLetters
    textGuessedLetters.pack_forget()
    text="Guessed letters: "+" ".join(guessedLetters)
    textGuessedLetters=Label(tk, text=text, bg="black", fg="white")
    textGuessedLetters.pack()

#This function is used to clean the GUI of the window.
def destroyGUI():
    global entryWidget, resetButton, counterText, wordText, textGuessedLetters, winOrLoseText
    entryWidget.pack_forget()
    resetButton.pack_forget()
    counterText.pack_forget()
    wordText.pack_forget()
    textGuessedLetters.pack_forget()
    winOrLoseText.pack_forget()

#This function is used to either display a win or lose message. It has clean UI and gives the player an option to replay the game.
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

#This piece of code reads a csv file and scraps words from that file to be stored in an array called words.
file=open("words.csv", "r")
listOfWords=file.read()
file.close()
words=listOfWords.split("\n")


#These variables are used to set up the game.
word=''
counter=0
MAX_NUMBER_OF_LIVES=9
guessedLetters=[]
wordLetters=[]
completedLettersList=[]
displayGuessedLetters=[]
finishedGame=False

#This piece of code sets up the game's GUI.
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

#This piece of code calls the function initialization to start the game as soon as the application launches.
initialization()

#This piece of code needs to be present to make sure GUI works properly.
tk.mainloop()
