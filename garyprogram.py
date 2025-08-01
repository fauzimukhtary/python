import random
import msvcrt
import time
import main
import zeelibrary as zee
from zeelibrary import slprt


def start():

    zee.garywelcome(1.7, 0.005)

    slprt("\nPlease enter your name : ", 0.015)
    player_name = input()
    while not player_name:
        slprt("\nName can't left blank! Please re-enter your name : ", 0.001)
        player_name = input()
    
    slprt(f"\nHi {player_name}, welcome to the game!\n", 0.015)
    while True:
            slprt("\nAre you ready to play? [ Y / N ]\n\n", 0.015)
            confirm_ready = input().lower()
            if confirm_ready == "y":
                break
            elif confirm_ready == "n":
                slprt("\nOkay, game stopped!\n\nReturning to Main Menu...\n", 0.015)
                time.sleep(2)
                if __name__ != '__main__':
                    main.mainmenu()
                exit()
            else:
                slprt("\nInvalid answer!\n", 0.015)

    slprt(zee.okay, 0.005)

    def gameplay() :

        correct_answer = random.randint(1,5)
        single_hole = "(_)"
        multiple_hole = [single_hole] * 5
        tmp_multiple_hole = multiple_hole.copy()
        hole_with_gary = "(🦫)"
        tmp_multiple_hole[correct_answer - 1] = hole_with_gary

        slprt("\nMeet our new friend, Gary the mole~\nTo meet Gary, you have to guess where does he is!\n\nLook at these holes!\n", 0.015)
        slprt("   ".join(multiple_hole), 0.015)
        slprt("\n 1     2     3     4     5\n\nGuess which hole is Gary in? [ 1 / 2 / 3 / 4 / 5 ]\n", 0.015)

        def answer(): 
            while True:
                try:
                    slprt("\nYour Answer = ", 0.015)
                    player_answer = int(input())
                    if player_answer in range(1,6):
                        return player_answer
                    else:
                        slprt("\nAnswer must between 1-5!\n", 0.001)
                except ValueError:
                    slprt("\nInvalid answer! Please input numbers only!\n", 0.001)

        def confirm_answer(player_answer):
            while True:
                slprt("\nAre you sure with your answer? [ Y / N ]\n\n", 0.015)
                confirm_answer = input().lower()
                if confirm_answer == "y":
                    return player_answer
                elif confirm_answer == "n":
                    while True:
                        slprt("\nDo you want to re-input your answer? [ Y / N ]\n\n", 0.015)
                        confirm_reinput = input().lower()
                        if confirm_reinput == "n":
                            return player_answer
                        elif confirm_reinput == "y":
                            slprt("\nYou will re-input your answer.\n", 0.015)
                            player_answer = answer()
                            break
                        else:
                            slprt("\nInvalid answer!\n", 0.015)
                else:
                    slprt("\nInvalid answer!\n", 0.015)
        
        player_answer = answer()
        player_answer = confirm_answer(player_answer)
        
        slprt("\nOkay! Let's see...\n", 0.015)
        slprt("   ".join(tmp_multiple_hole), 0.015)
        slprt("\n 1     2     3     4     5 \n", 0.015)
        
        while True:
            if player_answer == correct_answer:
                slprt(f"\nCongrats, {player_name}, you won!🏆\nGary is in hole {correct_answer}!\n", 0.015)
                return
            else:
                slprt(f"\nUh-oh, looks like you lost, {player_name}!❌\nGary is in hole {correct_answer}!\n", 0.015)
                return

    def confirm_restart():
        while True:
            slprt("\nWanna play again? [ Y / N ]\n\n", 0.015)
            confirm_restart = input().lower()
            if confirm_restart == "n":
                slprt("\nOkay, thank you for playing!\n", 0.015)
                return False
            elif confirm_restart == "y":
                slprt("\nOkay, game will restart!\n", 0.015)
                return True
            else:
                slprt("\nInvalid answer!\n", 0.015)

    def rating():
        slprt(zee.garyrating, 0.005)
        while True:
            try:
                slprt("\nYour rating = ", 0.015)
                rating = int(input())
                if rating in range(1,11):
                    return rating
                else:
                    slprt("\nThe answer must between 1-10!\n", 0.005)
            except ValueError:
                slprt("\nInvalid answer! Please input numbers only!", 0.005)

    def rating_feedback(rating):

        if rating in range(1,6):
            slprt(zee.garysorry, 0.015)
            while True:
                try:
                    slprt("\nYour Answer = ", 0.015)
                    ratresp = int(input())
                    if ratresp in range (1,5):
                        slprt("\nThank you for your feedback! We will improve that aspect as possible as we can!\n", 0.015)
                        return
                    elif ratresp == 5:
                        while True:
                            slprt("\nWhat is the other aspect that can we improve?\n\nYour answer = ", 0.015)
                            feedbackother = input()
                            if feedbackother == "":
                                slprt("\nThis can't left blank!\n", 0.005)
                            else:
                                slprt("\nThank you for your feedback! We will improve that aspect as possible as we can!", 0.015)
                                break
                        return feedbackother
                    else:
                        slprt("\nInvalid number!\n", 0.005)
                except ValueError:
                    slprt("\nInvalid answer! Please input numbers only!\n\n", 0.005)
        
        elif rating in range(6,11):
            slprt(f"\nGreat, {player_name}! Thank you for rating us {rating}/10!", 0.015)
            return

    while True:
        gameplay()
        if not confirm_restart():
            rating = rating()
            rating_feedback(rating)
            slprt("\n\nReturning to ZEE Main Menu... \n", 0.015)
            time.sleep(2)
            if __name__ != '__main__':
                main.mainmenu()
            exit()
        
if __name__ == "__main__":
    start()