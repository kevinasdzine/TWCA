import random
import tkinter

random.seed()

rangeStart = 1
rangeEnd = 10
number = random.randint(1,10)
notGuessed = True
numberGuessed = 0
guessCount = 0

def tryGuess():
    global numberGuessed
    global guessCount
    userEntered = inputField.get()
    try:
        numberGuessed = int(userEntered)
    except ValueError:
        label["text"] = "Invalid number. Try again."
        return
    guessCount += 1
    if numberGuessed == number:
        label["text"] = "{0} was the number. It took you {1} guesses".format(numberGuessed, guessCount)
        return
    else:
        if numberGuessed < rangeStart or numberGuessed > rangeEnd:
            label["text"] = "That number is not between {0} and {1}".format(rangeStart, rangeEnd)
            return
        if numberGuessed < number:
            label["text"] = "That number is too low"
            return
        if numberGuessed > number:
            label["text"] = "That number is too high"
            return


root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack(padx=10,pady=10)
title = tkinter.Label(frame)
title["text"] = "Pick a number between {0} and {1}".format(rangeStart, rangeEnd)
title.grid(row=0, column=0)
inputField = tkinter.Entry(frame)
inputField.grid(row=1, column=0)
button = tkinter.Button(frame, text = "Guess", command = tryGuess)
button.grid(row=2, column=0)
label = tkinter.Label(frame)
label.grid(row=3, column=0)
root.mainloop()
