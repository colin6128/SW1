# CamJam Edukit 1 - Basics
# Worksheet 6 - Buzzer

# Import Libraries
import os         # Gives Python access to Linux commands
import time       # Proves time related commands
from gpiozero import Buzzer  # The GPIO Zero button functions

# Set pin 22 as a buzzer
buzzer = Buzzer(22)


# Define some 'user-defined functions'
def dot():   # A single morse dot
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
    time.sleep(0.2)


def dash():  # A single morse dash
    buzzer.on()
    time.sleep(0.3)
    buzzer.off()
    time.sleep(0.1)


def letterspace():  # The space between letters
    time.sleep(1)   # Originally 0.2 seconds


def wordspace():   # The space between words
    time.sleep(2)  # Originally 0.6 seconds


def morseA():  # The Morse for A,....
    dot()
    dash()
    letterspace()


def morseB():  # The Morse for B,....
    dash()
    dot()
    dot()
    dot()
    letterspace()


def morseC():  # The Morse for C,....
    dash()
    dot()
    dash()
    dot()
    letterspace()


def morseD():  # The Morse for D,....
    dash()
    dot()
    dot()
    letterspace()


def morseE():  # The Morse for E,....
    dot()
    letterspace()


def morseF():  # The Morse for F,....
    dot()
    dot()
    dash()
    dot()
    letterspace()


def morseG():  # The Morse for G,....
    dash()
    dash()
    dot()
    letterspace()


def morseH():  # The Morse for H,....
    dot()
    dot()
    dot()
    dot()
    letterspace()


def morseI():  # The Morse for I,....
    dot()
    dot()
    letterspace()


def morseJ():  # The Morse for J,....
    dot()
    dash()
    dash()
    dash()
    letterspace()


def morseK():  # The Morse for K,....
    dash()
    dot()
    dash()
    letterspace()


def morseL():  # The Morse for L,....
    dot()
    dash()
    dot()
    dot()
    letterspace()


def morseM():  # The Morse for M,....
    dash()
    dash()
    letterspace()


def morseN():  # The Morse for N,....
    dash()
    dot()
    letterspace()


def morseO():  # The Morse for O,....
    dash()
    dash()
    dash()
    letterspace()


def morseP():  # The Morse for P,....
    dot()
    dash()
    dash()
    dot()
    letterspace()


def morseQ():  # The Morse for Q,....
    dash()
    dash()
    dot()
    dash()
    letterspace()


def morseR():  # The Morse for R,....
    dot()
    dash()
    dot()
    letterspace()


def morseS():  # The Morse for S, ....
    dot()
    dot()
    dot()
    letterspace()


def morseT():  # The Morse for T,....
    dash()
    letterspace()


def morseU():  # The Morse for U, ....
    dot()
    dot()
    dash()
    letterspace()


def morseV():  # The Morse for V, ....
    dot()
    dot()
    dot()
    dash()
    letterspace()


def morseW():  # The Morse for W, ....
    dot()
    dash()
    dash()
    letterspace()


def morseX():  # The Morse for X, ....
    dash()
    dot()
    dot()
    dash()
    letterspace()


def morseY():  # The Morse for Y, ....
    dash()
    dot()
    dash()
    dash()
    letterspace()


def morseZ():  # The Morse for Z, ....
    dash()
    dash()
    dot()
    dot()
    letterspace()


os.system('clear')  # Clears the terminal window

print("Morse code")


# Prompt the user for input
def translate():
    msg = raw_input('MESSAGE: ')

    for char in msg:
        print CODE[char.upper()],
    raw_input("When done, press [ENTER]")


if __name__ == "__main__":
    main()


# Added code from web, not functional
loop_count = input("How many times would you like THOMAS to loop? ")
loop_count = int(loop_count)  # Convert text input into an integer
while loop_count > 0:  # Loop around the chosen number of times
    morseT()
    letterspace()
    morseH()
    letterspace()
    morseO()
    letterspace()
    morseM()
    letterspace()
    morseA()
    letterspace()
    morseS()
    letterspace()
    wordspace()
    loop_count = loop_count - 1
