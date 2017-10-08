# This script implements a command-line blackjack game 

import random

def win(player_point, dealer_point):
    """
    Decide who wins. 
    """
    print "player_point:{}".format(player_point)
    print "dealer_point:{}".format(dealer_point)
    # if player_point > 21, player busts and lose
    if player_point > 21:
        print "You lose.."
        return -1
        
    if player_point <= 21:
        if dealer_point > 21:
            print "You win!"
            return 1
        elif player_point > dealer_point:
            print "You win!"
            return 1
        elif player_point == dealer_point:
            print "Push.."
            return 0
        else:
            print "You lose.."
            return -1
            
            
def shuffle():
    """Shuffle the cards"""
    cards = ['A', '2', '3', '4','5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    random.shuffle(cards)
    return cards
    
    
def distribute_card(cards):
    """Dealer distributes cards to herself and players"""   
    if len(cards) > 0:
        return cards.pop()
    else:
        return "No cards.."
        
def points_sum(*args):
    """Calculate the sum of points"""
    points = 0
    count_A = 0
    soft_17 = None
    print args
    for arg in args:
        try:
            points += int(arg)
        except:
            if arg in ('J', 'Q', 'K'):
                points += 10
            else:
                count_A += 1
    if count_A == 1:
        if points <= 10:
            points += 11
        else:
            points += 1
    elif count_A == 2:
        if points <= 9:
            points += 12
        else:
            points += 2           
    elif count_A == 3:
        if points <= 8:
            points += 13
        else:
            points += 3
    elif count_A == 4:
        if points <= 7:
            points += 14
        else:
            points += 4
    if points == 17:
        if count_A > 0:
            soft_17 = True
        else:
            soft_17 = False
    return points, soft_17
           
def enter():
    while True:
        begin = raw_input("Play again? (Y/N)")
        if begin.lower() == "n":
            print "Thanks for coming! See you next time!"
            return False
        elif begin.lower() == "y":
            return True 
        else:      
            print "Invalid input..Please input Y or N."  
            
def first_enter():
    while True:
        begin = raw_input("Do you want to begin? (Y/N)")
        if begin.lower() == "n":
            print "Thanks for coming! See you next time!"
            return False
        elif begin.lower() == "y":
            return True 
        else:      
            print "Invalid input..Please input Y or N."  
            
           

if __name__ == '__main__':
    print "#################################"
    print "#                               #"
    print "#   Welcome to Qishi Casino~~~  #"
    print "#                               #"
    print "#################################"
    begin = first_enter()
    if begin:
        print "Let's begin~~"
        ROUND = 1 # count the round
        
        while True:
            print ""
            print "---------- ROUND {} -----------".format(ROUND)
            if ROUND % 6 == 1:
                print "Shuffle the cards.."
                cards = shuffle() # shuffle the cards
            player_point, dealer_point = 0, 0
            player_cards, dealer_cards = [], []
        
            player_card_one = distribute_card(cards) # player's 1st card
            print "Your first card is: {}".format(player_card_one)
            # player_point += player_card_one
            player_cards.append(player_card_one)
        
            dealer_card_one = distribute_card(cards) # dealer's 1st card, facedown
            dealer_cards.append(dealer_card_one)
        
            player_card_two = distribute_card(cards) # player's 2nd card
            print "Your second card is: {}".format(player_card_two)
            # player_point += player_card_two
            player_cards.append(player_card_two)
        
            dealer_card_two = distribute_card(cards) # dealer's 2nd card, facedown
            print "Dealer's second card is: {}".format(dealer_card_two)
            # dealer_point += dealer_card_two
            dealer_cards.append(dealer_card_two)
        
            # Player's turn
        
            while True:
            # Player decides to hit or stand.
                hit = raw_input("Your turn: hit or stand? (H/S)")
            
                if hit.lower() == "h":
                    player_card = distribute_card(cards) # player's nth card
                    player_cards.append(player_card)
                    print "Your {}th card is: {}".format(len(player_cards), player_card)
                
                    player_point, _ = points_sum(*player_cards) 
                
                    if player_point > 21:
                        # print "You lose.."
                        break
                elif hit.lower() == "s":
                    print "You decide to stand."
                    break
                else:
                    print "Please enter H or S.."
                    
            player_point, _ = points_sum(*player_cards) 
            if player_point > 21:
                print "You lose.."
                play_again = enter()
                if not play_again:
                    break
                ROUND += 1
                continue
            # dealer's turn
            print "Dealer's turn."
            print "Dealer's first card is: {}".format(dealer_card_one)
            dealer_point, soft_17 = points_sum(*dealer_cards)
        
            # if dealer's points < 17 or soft 17, hit 
            while dealer_point < 17 or (dealer_point == 17 and soft_17):
                dealer_card = distribute_card(cards)
                dealer_cards.append(dealer_card)
                print "Dealer's {}th card is: {}".format(len(dealer_cards), dealer_card)
                dealer_point, soft_17 = points_sum(*dealer_cards)
            
            sign = win(player_point, dealer_point)
            
#             if sign == 1:
#                 print "You win!"
#             elif sign == 0:
#                 print "Push.."
#             else:
#                 print "You lose.."
            
            play_again = enter()
            if not play_again:
                break
            
            # increase the round by 1
            ROUND += 1        
        
        
        
        
        
        