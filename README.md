# countdown-numbers-game
Python program to solve questions in the style of the numbers game from the British game show Countdown. Using n given integers, construct a target number M through addition, subtraction, multiplication, or division of those numbers. Each number can be used at most once, and not all numbers must be used.

# How To Run
1. Open countdown_main.py using Python Launcher, or run "python path/to/countdown_main.py" or "python3 path/to/countdown_main.py" in the Terminal (Mac/Linux) or Command Line (Windows)
2. Input an integer target sum. Input nothing to exit.
3. Input an integer N denoting how many numbers there are in the list of numbers to be used in the game. Input nothing to exit.
4. Input N integers listing the numbers to be used in the game.
5. The program will print one solution to the command line, if any are found. Order of operations is left-to-right where addition, subtraction, multiplication, division all have the same level of priority. E.g. the solution "8+19\*16-6/3" is interpreted as "((((8+19)\*16)-6)/3)"
