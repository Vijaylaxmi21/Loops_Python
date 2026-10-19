secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))

    if guess < secret:
        print("Try a bigger number")
    elif guess > secret:
        print("Try a smaller number")
    else:
        print("Correct guess!")
