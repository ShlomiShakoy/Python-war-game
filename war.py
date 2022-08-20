import random
import os
suits= ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten', 'Jack', 'Queen', 'King', 'Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
player1_wins=[]
player2_wins=[]

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank+" of "+self.suit

class Deck():
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

def play(player_one_name,player_two_name):
    player_one=Player(player_one_name)
    player_two=Player(player_two_name)
    new_deck=Deck()
    new_deck.shuffle()

    for item in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    game_on=True
    round_num=0
    while game_on:
        round_num+=1
        if round_num==500:
            print('The result of this game is deuce!')
            print(f'\n{player_one_name} wins amount: {len(player1_wins)}')
            print(f'{player_two_name} wins amount: {len(player2_wins)}\n')
            result=input('Enter either 1 to replay or other key for exit: ')
            if result=='1':
                os.system('cls')
                play(player_one_name,player_two_name)
            return
        print(f'Round {round_num}')
        if len(player_one.all_cards)==0:
            print(f'\n{player_one.name} out of cards! {player_two.name} wins!\n')
            player2_wins.append('win')
            print(f'{player_one_name} wins amount: {len(player1_wins)}')
            print(f'{player_two_name} wins amount: {len(player2_wins)}\n')
            result = input('Enter either 1 to replay or other key for exit: ')
            if result == '1':
                os.system('cls')
                play(player_one_name,player_two_name)
            game_on=False
            break

        if len(player_two.all_cards)==0:
            print(f'\n{player_two.name} out of cards! {player_one.name} wins!')
            game_on=False
            player1_wins.append('win')
            print(f'\n{player_one_name} wins amount: {len(player1_wins)}')
            print(f'{player_two_name} wins amount: {len(player2_wins)}\n')
            result = input('Enter either 1 to replay or other key for exit: ')
            if result == '1':
                os.system('cls')
                play(player_one_name,player_two_name)
            break

        player_one_cards=[]
        player_one_cards.append(player_one.remove_one())
        player_two_cards=[]
        player_two_cards.append((player_two.remove_one()))

        at_war=True
        while at_war:
            if player_one_cards[-1].value>player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war=False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
            else:
                print('War!')
                if len(player_one.all_cards)<5:
                    player2_wins.append('win')
                    print(f"\n{player_one.name} doesn't have enough card to declare war.")
                    print(f'{player_two.name} wins!\n')
                    print(f'{player_one_name} wins amount: {len(player1_wins)}')
                    print(f'{player_two_name} wins amount: {len(player2_wins)}\n')
                    game_on=False
                    result = input('Enter either 1 to replay or other key for exit: ')
                    if result == '1':
                        os.system('cls')
                        play(player_one_name,player_two_name)
                    break
                elif len(player_two.all_cards)<5:
                    player1_wins.append('win')
                    print(f"\n{player_two.name} doesn't have enough card to declare war.")
                    print(f'{player_one.name} wins!\n')
                    print(f'{player_one_name} wins amount: {len(player1_wins)}')
                    print(f'{player_two_name} wins amount: {len(player2_wins)}\n')
                    game_on = False
                    result = input('Enter either 1 to replay or other key for exit: ')
                    if result == '1':
                        os.system('cls')
                        play(player_one_name,player_two_name)
                    break
                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

if __name__=='__main__':
    player_one_name = input('Player 1 please enter your name: ')
    player_two_name = input('Player 2 please enter your name: ')
    print(f'{player_one_name} wins amount: {len(player1_wins)}')
    print(f'{player_two_name} wins amount: {len(player2_wins)}')
    play(player_one_name,player_two_name)