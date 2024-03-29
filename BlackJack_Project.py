import random
import BlackJackArt
import os
import time

#Function to clear the screen after each user inputs information.
def screen_clear() :
    """Clears the screen according to users operating system."""
    if os.name == 'posix' :
        _ = os.system('clear')
    else :
        _ = os.system('cls')

#Function to deal cards.
def deal_card(number, hand) :
    """Returns a random card from the deck."""
    for i in range(number) :
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        hand.append(card)

play_again = True

#Function that restarts the game if user desires.
def play_again_function() :
    play_again_prompt = input("Would you like to play again? Type 'y' or 'n': " )

    if play_again_prompt == 'y' :
        play_again = True
        screen_clear()
        game_play()
    elif play_again_prompt == 'n' :
        print("Thanks for playing!")
        time.sleep(3)
        quit()

#The main function which involves the game play attributes.
def game_play() :
    while play_again :

        #Prints the logo for blackjack.
        print(BlackJackArt.logo)
        user_hand = []
        computer_hand = []

        #Deals user and computer two initial cards at the start of the game.
        deal_card(2, user_hand)
        deal_card(2, computer_hand)

        #Calculates user and computer scores.
        user_score = sum(user_hand)
        computer_score = sum(computer_hand)

        #Prints the current hand and score for user, and only first card for computer/dealer hand.
        def hand_and_score() :
            print(f"Your cards: {user_hand}, current score: {user_score}")
            print(f"Computer's first card: {computer_hand[0]}.")

        #Prints the final score and final hand for user and computer.
        def final_hand_and_score() :
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

        hand_and_score()

        hit = True

        while hit :

            #Checks for blackjack after initial deal.
            if user_score == 21 :
                final_hand_and_score()
                print("BlackJack! You win!")
                play_again_function()
            elif computer_score == 21 :
                final_hand_and_score()
                print("Computer has a BlackJack! You lose!")
                play_again_function()

            #Checks for aces in user hand, changes value to 1 if over 21.
            if user_score > 21 :
                if 11 in user_hand :
                    eleven_position = user_hand.index(11)
                    user_hand[eleven_position] = 1
                    user_score = sum(user_hand)
                    if user_score > 21 :
                        final_hand_and_score()
                        print("Bust! You lose!")
                        play_again_function()
                    elif user_score < 21 :
                        hand_and_score()
                else :
                    final_hand_and_score()
                    print("Bust! You lose!")
                    play_again_function()

            #Asks user if they would like another card.
            hit_prompt = input("Would you like another card? Type 'y' or 'n': ").lower()

            #Deals card or skips if depending on users response to hit_prompt.
            if hit_prompt == 'y' :
                deal_card(1, user_hand)
                user_score = sum(user_hand)
                hand_and_score()
                hit = True
                continue
            elif hit_prompt == 'n' :
                hit = False
                break

        #Deals cards to computer until over 17 per blackjack rules. If 11 in hand and score is > 21,
        #11 is changed to 1 per blackjack rules.
        while computer_score < 17 :
            deal_card(1, computer_hand)
            user_score = sum(user_hand)
            computer_score = sum(computer_hand)
            if computer_score > 21 :
                if 11 in computer_hand :
                    eleven_position = computer_hand.index(11)
                    computer_hand[eleven_position] = 1
                    computer_score = sum(computer_hand)
                    if computer_score > 21 :
                        final_hand_and_score()
                        print("Computer went bust! You win!")
                        play_again_function()
                    elif user_score < 21 :
                        hand_and_score()
                else :
                    final_hand_and_score()
                    print("Computer went bust! You win!")
                    play_again_function()

        hand_and_score()

        #Determines winner.
        if computer_score > user_score :
            final_hand_and_score()
            print("You lose!")
            play_again_function()
        elif computer_score < user_score :
            final_hand_and_score()
            print("You win!")
            play_again_function()
        elif computer_score == user_score :
            final_hand_and_score()
            print("Draw!")
            play_again_function()

#Executes game_play.
game_play()
