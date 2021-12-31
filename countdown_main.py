import countdown_game as cg

def isInputNumber(userInput):
    try:
        val = int(userInput)
        return True
    except ValueError:
        return False

userInput = None
numbers = None

while (userInput != ''):
    userInput = input("Target sum: ")
    if (isInputNumber(userInput)):
        targetSum = int(userInput)

        userInput = input("N: ")
        if (isInputNumber(userInput)):
            n = int(userInput)
            numbers = [0 for i in range(n)]
            i = 0

            while (i < n):
                userInput = input(f'numbers[{i}]: ')
                if (isInputNumber(userInput)):
                    numbers[i] = int(userInput)
                    i += 1
                else:
                    print("Error: Please enter a number.\n")
            
            countdown = cg.Countdown(targetSum, numbers)
            path = countdown.search()
            print(path, end="\n\n")

        else:
            print("Error: Please enter a number.\n")
    else:
        print("Error: Please enter a number.\n")