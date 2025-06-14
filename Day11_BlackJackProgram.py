import random

from Day11_BlackJackArt import logo

def deal_card():
    '''Give a random card from card list'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    ''' Return the sum of all the cards'''
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)

def compare(u_score, c_score):
    if u_score==c_score:
        print("Draw")
    elif u_score == 0 :
        print("You Win with BlcakJack")
    elif c_score == 0:
        print("You Lose, opponent has a BlackJack")
    elif c_score>21:
        print("You Win, Oponent Went Over")
    elif u_score>21:
        print("You Lose, you went over 21")
    elif u_score>c_score:
        print("You Win")
    else:
        print("You Lose")




def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_end = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards}, current score {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True

        take_card = input("Type 'y' to get another card, 'n' to pass : ")
        if take_card=='y':
            user_cards.append(deal_card())

        elif take_card=='n':
            game_end=True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand : {user_cards}, Your Final Score : {user_score}")
    print(f"Computer Final Hand : {computer_cards}, Computer Final Score : {computer_score}")
    compare(user_score, computer_score)

while input("Do you want to play another round? 'y' to Continue; 'n' to Stop! : ") == 'y':
    print("\n" * 20)
    play_game()

