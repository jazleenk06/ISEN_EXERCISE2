def guessing_game():
    '''
    Guess a number between 1 and 100
    '''
    answer = 42
    guess = int(input("Guess a number between 1 and 100: "))
    while guess != answer:
        if guess < answer:
            print("Too low")
        else:
            print("Too high")
        guess = int(input("Guess again: "))
    print("You got it!")
