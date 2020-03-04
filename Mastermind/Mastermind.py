"""At the start of the program, the 4 numbers to be used in the game are generated
The variable game_Over is in place to keep the game running untill the user has guessed the numbers
The function in_game() takes the 4 numbers in game_list, and the users guess, (stored in user_guess)
and runs it through a number of checks,  if it finds that the user has matched their number with the
numbers generated, the game is over and a winning message and the users ammounts of guesses is displayed
"""

import random

game_list = list()
while len(game_list) < 4:        
    num = str(random.randint(0,9))
    if num not in game_list[:]:
        game_list.append(num)

#print(game_list)

game_Over = False
tries = 0

def in_game(game_list, user_guess):
    
    correct_num = 0
    num_in_list = 0        
    duplicate = 0

    if (len(user_guess) != 4):
        if (len(user_guess) > 4):
            print("Too long!")
        else:
            print("Too short!")
    else:        
        for i in range(4):            
            if user_guess[i] == game_list[i]:
                correct_num += 1
            if user_guess[i] in game_list[:]:
                num_in_list += 1
            if(user_guess.count(user_guess[i]) > 1 and user_guess[i] in game_list[:]):
                duplicate += 1
        if (duplicate > 1):
            num_in_list -= (duplicate - 1)    
        if(num_in_list > 0):
            print("\nYou guessed", num_in_list, "correct number(s)")      
        if(correct_num > 0):
            print("\nYou guessed", correct_num, "number(s) in the correct place\n")        
        if(correct_num == 0 and num_in_list <= 0):
            print("You didn't find any numbers in the sequence\n")
        if(correct_num == 4):            
            return correct_num

while game_Over == False:        
    tries += 1    
    user_guess = str(input("Enter your guess in 4 digits (eg. 1234): "))

    if(in_game(game_list,user_guess) == 4):
        game_Over = True

print("\nYou guessed correctly")
print("It took you", tries, "tries")