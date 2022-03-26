# A simple rock, papers, scissors game with a bot
# with a simple while loop to keep playing the game
import random

# The main method.
def main() : 
    print("Wanna play rock, paper, scissors?")
    playGame = input("Input: ")
    print()
    
    # Keep playing the game when condition is met.
    while playGame.lower() == "yes" :
        print(gameMatch())
        # Set a sentinel to determine if we want to keep playing the game/continue the loop.
        playGame = input("\nPlay again? Yes or no: ")
        print()

    # Print when the player ends the game.
    print("\nThanks for playing! Hope you had fun!")

# This function initiates a game and determines if the user wins, loses, or ties the game.
# @param userMove   moves chosen by the user
# @param botMove    the bot's random pre-defined moveset
# @func isWin       a function that determines if the player wins
# @return           a text displaying the result of the game
def gameMatch() :
    userMove = input("Rock, paper, or scissors? ")
    
    # Bot choice of moves
    botMove = random.choice(["rock", "paper", "scissors"])
    
    print("You:", userMove)
    print("Bot:", botMove)
    print()
    
    if userMove == (botMove) :
        return "It's a tie\n!"
    elif isWin(userMove, botMove) :
        return "You win!\n"
    else : 
        return "You lose!\n"

        
# This function determins if the user wins the game
# @return   True if the user wins or meets any of the condition, False if not
def isWin(userMove, botMove) :
    # Determine winning conditions
    if ((userMove == "rock" and botMove == "scissors") or (userMove == "paper" and botMove == "rock") or (userMove == "scissors" and botMove == "paper")) :
        return True
    
# Start the program.
main()
