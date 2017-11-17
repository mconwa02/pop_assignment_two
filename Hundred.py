''' Michelle Conway MCONWA02
   Coded Solutions to Hundred Game'''

import random

computer_score = 0
human_score = 0

def main():
    """ """
def instruction():
    """Rules of Game
Players take turns to roll a die as many times or until 1 is rolled.
Each number rolled, except a 1, is added to players score.
If 1 is rolled score for this turn is zero and turn ends.
At the end of each turn, the score for that turn is
added to the player's total score.
The first player to reach or exceed 100 wins.
"""
    computer move()
    
def human_move(computer_score, human_score):
""" Tells the user current score and computer's score
and how far behind (or ahead) they are.
Then repeatedly asks whether the user wants to roll again until,
The user decides not to roll again or rolls a 1.
The function returns the result (either 0 or the total of the rolls) """
    ask_yes_or_no("Do you want to roll? ", {"y", "Y"})
    if 



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


def roll():
    die_value = random.randint(1,7)
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
     if computor_score >100 and human_score < 100:
         print("Human lost the game by " + str(100 - human_score))
     elif human_score >= 100 and computer_score >= 100:
         print("Human won the game by" + str(human_score)

pytest
               
def main(x):
    return x + 1

def test_answer():
    assert main(3) == 5

    



