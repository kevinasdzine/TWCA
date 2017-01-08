import random

random.seed()

rangeStart = 1
rangeEnd = 10
number = random.randint(1,10)

print("Pick a number between {0} and {1}".format(rangeStart, rangeEnd))

notGuessed = True
guessCount = 0
while notGuessed:
    userEntered = input()
    try:
        numberGuessed = int(userEntered)
        guessCount += 1
    except ValueError:
        print("Invalid number. Try again.")
        continue
    if numberGuessed == number:
        print("{0} was the number. It took you {1} guesses".format(numberGuessed, guessCount))
        notGuessed = False
    else:
        if numberGuessed < rangeStart or numberGuessed > rangeEnd:
            print("That number is not between {0} and {1}".format(rangeStart, rangeEnd))
            continue
        if numberGuessed < number:
            print("That number is too low")
            continue
        if numberGuessed > number:
            print("That number is too high")
            continue