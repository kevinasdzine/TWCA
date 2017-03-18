def ispalindrome(test):
    if len(test) < 2:
        return True
    first = test[0]
    last = test[-1]
    remainder = test[1:-1]
    if first == last and ispalindrome(remainder):
        return True
    return False

guess = input("Enter some text\n")
if ispalindrome(guess):
    print(guess + " is a palindrome")
else:
    print(guess + " is not a palindrome")
