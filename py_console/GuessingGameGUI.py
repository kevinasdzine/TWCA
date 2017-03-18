import random
import tkinter

random.seed()

range_start = 1
range_end = 10
number = random.randint(1,10)
not_guessed = True
number_guessed = 0
guess_count = 0

def try_guess():
    global number_guessed
    global guess_count
    user_entered = inputField.get()
    try:
        number_guessed = int(user_entered)
    except ValueError:
        label["text"] = "Invalid number. Try again."
        return
    guess_count += 1
    if number_guessed == number:
        label["text"] = "{0} was the number. It took you {1} guesses".format(number_guessed, guess_count)
        return
    else:
        if number_guessed < range_start or number_guessed > range_end:
            label["text"] = "That number is not between {0} and {1}".format(range_start, range_end)
            return
        if number_guessed < number:
            label["text"] = "That number is too low"
            return
        if number_guessed > number:
            label["text"] = "That number is too high"
            return


root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack(padx=10,pady=10)
title = tkinter.Label(frame)
title["text"] = "Pick a number between {0} and {1}".format(range_start, range_end)
title.grid(row=0, column=0)
inputField = tkinter.Entry(frame)
inputField.grid(row=1, column=0)
button = tkinter.Button(frame, text = "Guess", command = try_guess)
button.grid(row=2, column=0)
label = tkinter.Label(frame)
label.grid(row=3, column=0)
root.mainloop()
