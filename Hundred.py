''' Michelle Conway MCONWA02
   Coded Solutions to Hundred Game'''

import random

computer_score = 0
human_score = 0

def main():
    """ Hundred Game """
    instruction()
    computer_move(computer_score, human_score)
    human_move(computer_score, human_score)
    while False:
    is_game_over(computer_score, human_score)
    computer_move(computer_score, human_score)
    human_move(computer_score, human_score)
    else:
        show_results(computer_score, human_score)
        
def instruction():
    """Rules of the Game"""
        print("You will play a game against the computer")
        print("You will take turns to roll a die as many times or until 1 is rolled")
        print("Each number rolled, except a 1, is added to each players score")
        print("If 1 rolled, score for this turn will be zero, and turn ends")
        print("The first player to reach or exceed 100 wins")
        print("The computer will go first, so you get one more turn if the computer is the first to reach 100")
        print("If there is a tie with 100 or more, each gets another turn until the tie is broken")
    
    
def human_move(computer_score, human_score):
""" Tells the user current score and computer's score
and how far behind (or ahead) they are.
Then repeatedly asks whether the user wants to roll again until,
The user decides not to roll again or rolls a 1.
The function returns the result (either 0 or the total of the rolls) """
    print("Your current score is " + str(human_score))
    print("The computer's score is " +str(computer_score))
    if computer_score > human_score:
        print("You are behind the computer by " + str(computer_score -human_score) + " points")
    if computer_score < human_score:
        print("You are ahead of the computer by " + str(human_score - computer_score) + " points")
    turn_score = roll()
    turn_sum = turn_score
    n = 1
    while True and turn_score!= 1:
        ask_yes_or_no("Roll again?")
        score = roll()
        if score != 1:
            turn_sum += score
            n += 1
        else:
            turn_sum = 0
            break
    human_score = turn_sum
    if turn_sum ==0 or turn_score ==1:
        result = 0
    else:
        result = n
    return result             

def computer_move(computer_score, human_score):
"""The computer rolls some number of times, displays the result of each roll.
The function returns the result (either 0 or the total of the rolls) """
    turn_sum = 0
    n_rolls = random.randint(1,50)
    for n in range(n_rolls):
        score = roll()
        n = 1
        print(score)
        while score != 1: 
            turn_sum += score
            score = roll()
            n += 1
            print(score)
        else:
            turn_sum = 0
            break
    computer_score = turn_sum
    if turn_sum ==0:
        result = 0
    else:
        result = n
    return result
    
def is_game_over(computer_score, human_score):
""" Returns True if either player has 100 or more, and the players are not tied!
    otherwise it returns False. (Call this only after the human's move)"""
     if computer_score >= 100 or human_score >= 100 and (computer_score != human_score):
         return True
     else:
         return False

    
def roll():
    die_value = random.randint(1,6)
    return die_value


print(roll())          

def ask_yes_or_no(prompt):
""" Prints the prompt as a question, "Roll again?"
If responds starts with 'y' or 'Y' the function returns True.
If responds starts with 'n' or 'N' the function returns False.
Any other response will cause the question to be repeated"""
    print(prompt)
    s = input()
    if s[0]=="y" or s[0] == "Y":
        return True
    elif s[0]=="n" or s[0] == "N":
        return False
    else:
        print(prompt)
        s = input()
        while s[0]!="y" or s[0] != "Y" or s[0]!= "n" or s[0] != "N":
            print(prompt)
            s = input()
            if s[0] == "y" or s[0] == "Y":
                return  True
                break
            elif s[0] == "n" or s[0] == "N":
                return  False
                break

ask_yes_or_no("Roll again?")

def show_results(computer_score, human_score):
     """Declares weather the human won or lost"""
     while True:
        is_game_over(computer_score, human_score)    
        if computer_score > human_score:
            ans = print("You have lost the game by " + str(computer_score - human_score) + " points")
        elif human_score > computer_score:
            ans = print("You have won the game by " + str(human_score - computer_score) + " points")
        return ans
pytest
               
def main():
    return x + 1

def test_answer():
    assert main()

    



