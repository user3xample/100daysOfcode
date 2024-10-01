#! /usr/bin/env python3
import random
import os
from art import logo

def clear():
    os.system('cls||clear')

def deal_card():
    """Returns a random card from our deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return a score calculated from the cards"""
    if sum (cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum (cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
       return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "win, you have blackjack"
    elif user_score >21:
        return "You Bust, over 21 scored"
    elif computer_score > 21:
        return "Computer went bust you win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "you Lose"

def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card: {user_cards} your score: {user_score}")
        print(f"computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
          is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards {user_cards} computer cards {computer_cards} ")
    print(f"Your Score {user_score} Computer score {computer_score} ")
    print(compare(user_score, computer_score))


while input ("do you want to play a Game_0ne of blackjack 'y' or 'n' : ").lower() == "y":
    clear()
    blackjack()


