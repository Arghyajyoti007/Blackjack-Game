# 🃏 Blackjack Game (Python CLI)

A fun command-line simulation of the popular card game **Blackjack** built using Python. Play against a computer dealer, draw cards, and try to reach 21 without going over!

---

## 🎯 Game Objective

The goal of Blackjack is to beat the dealer (computer) by having a hand that totals closer to **21** than the dealer’s — **without exceeding 21**.

---

## 🧠 Features

- Simulates real Blackjack game mechanics
- Random card dealing from a virtual deck
- Handles special rules for Aces (`11` or `1`)
- Computer dealer automatically plays after you pass
- Checks for "Blackjack" (21 with two cards)
- Allows replaying rounds
- ASCII logo display via external module

---

## 🛠️ Technologies Used

- Python 3
- Random Module
- Custom Modules:
- Day11_BlackJackArt.py` – contains the ASCII art/logo

---

## 🎮 Gameplay Example
```
Do you want to play another round? 'y' to Continue; 'n' to Stop! : y

Your cards [10, 7], current score 17
Computer's first card : 8
Type 'y' to get another card, 'n' to pass : n

Your Final Hand : [10, 7], Your Final Score : 17
Computer Final Hand : [8, 9], Computer Final Score : 17
Draw
```

## 🔧 Function Breakdown  
deal_card() 
Randomly selects a card from the list (1-11 and 10s for face cards).  

calculate_score(cards)  
Calculates the total value of a hand. Handles:  

- Blackjack check (21 with 2 cards)  

- Ace value switch (11 → 1 if total > 21)  

compare(user_score, computer_score)  
Prints the result of the game round (win, lose, draw, blackjack, bust, etc.).  

play_game()  
Controls a full round of Blackjack:  

- Deals cards  

- Handles user interaction  

- Runs computer logic  

- Displays result  

## 🚀 Potential Enhancements  
- Add a betting system with chips  

- Simulate a deck with card removal (no infinite draws)  
 
- Add face cards (J, Q, K)  

- GUI with Tkinter  

- Multiplayer support  

##  👨‍💻 Author  
Arghyajyoti Samui  
GitHub: @Arghyajyoti007  



