import os
import random
import sys
import signal

#comments to check git commit
#user choses rock so this happens
def rock(comp_choice):
    if comp_choice == 'PAPER':
        print('\nYOU LOSE')
    elif comp_choice == 'ROCK':
        print('\nDRAW')
    else:
        print('\nYOU WIN')


#user choses paper so this happens
def paper(comp_choice):
    if comp_choice == 'PAPER':
        print('\nDRAW')
    elif comp_choice == 'ROCK':
        print('\nYOU WIN')
    else:
        print('\nYOU LOSE')


#user choses scissor so this happens
def scissor(comp_choice):
    if comp_choice == 'PAPER':
        print('\nYOU WIN')
    elif comp_choice == 'ROCK':
        print('\nYOU LOSE')
    else:
        print('\nDRAW')



#taking input from user and asking for input agin if the input is worng
def take_user_input():
    while True:
        user_choice = input('ROCK PAPER SCISSOR\n\n>>> ').lower()
        print(f'\nYou chose {(user_choice).upper()}')
        if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissor':
            break
        else:
            print('\nThis is not a valid choice. Please choose from "Rock", "Paper" or "Scissor"\n')
            continue
    return user_choice



#this is the brain
def rockpaperscissor():

    cont = True
    while cont is True:
        
        user_choice = take_user_input()
        comp = random.randint(1,4)  #generating a random number from 1 to 3 and assigning each number to an entity
        if comp == 1:
            comp_choice = 'ROCK'
        elif comp == 2:
            comp_choice = 'PAPER'
        else:
            comp_choice = 'SCISSOR'


        print(f'\nComputer chose {comp_choice}')
        
        
        if user_choice == 'rock':  #calling the appropriate function based on what the user chose        
            rock(comp_choice)
        elif user_choice == 'paper':
            paper(comp_choice)
        else:
            scissor(comp_choice)

        ch = input('\nWant to play another round? (Y/N)\n').lower()  #asking whether to play another round or not
        if ch == 'y':
            cont = True
            os.system('clear')
        else:
            cont = False
            os.kill(os.getppid(), signal.SIGHUP)  #closes the terminal


if __name__ == "__main__":
    rockpaperscissor()
