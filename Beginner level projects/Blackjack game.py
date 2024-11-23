import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def blackjack_game():
    def start_deal(deck):
        card = random.choice(deck)
        deck.remove(card)  # Remove the card from the deck
        return card

    def player_loss(player, cpu):
        if sum(player) > 21:
            return True
        if sum(cpu) == 21 and sum(player) != 21:
            return True
        return False

    def done_playing():
        player_sum = sum(player_cards)
        cpu_sum = sum(cpu_cards)
        print(f"Your hand is: {player_cards}, a total of {player_sum}.")
        print(f"The computer's hand is {cpu_cards}, a total of {cpu_sum}.")
        if sum(cpu_cards) > 21:
            print("The computer got a bust, you win!")
        elif player_loss(player_cards, cpu_cards):
            print("You lose.")
        elif sum(player_cards) == 21 and sum(cpu_cards) != 21:
            print("You win!")
        elif sum(player_cards) > 21:
            print("It's a bust, you lose.")
        elif player_sum == cpu_sum:
            print("It's a draw.")
        elif player_sum > cpu_sum:
            print("You win!")
        else:
            print("You lose.")
        play_again = input("Do you want to play again? Type 'y' or 'n': ")
        if play_again == 'y':
            blackjack_game()
        else:
            print("Goodbye.")

    def keep_playing():
        player_cards.append(start_deal(deck))
        player_sum = sum(player_cards)
        
        # Handle Ace value adjustment for player
        if 11 in player_cards and player_sum > 21:
            player_cards[player_cards.index(11)] = 1
        
        print(f"Your hand is: {player_cards}, a total of {player_sum}.")
        
        if player_sum > 21:
            print("It's a bust, you lose.")
            done_playing()
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == 'y':
                keep_playing()
            elif hit == 'n':
                # CPU's turn
                while sum(cpu_cards) < 17:  # CPU hits until it reaches 17 or more
                    cpu_cards.append(start_deal(deck))
                    if 11 in cpu_cards and sum(cpu_cards) > 21:
                        cpu_cards[cpu_cards.index(11)] = 1
                done_playing()

    print(logo)
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    cpu_cards = []
    player_cards.append(start_deal(deck))
    player_cards.append(start_deal(deck))
    cpu_cards.append(start_deal(deck))
    
    print(f"Your cards: {player_cards}")
    print(f"The computer's first card: {cpu_cards[0]}")

    keep_playing()

blackjack_game()
