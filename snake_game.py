#!/usr/bin/python3

import random

players = {}
initial_position = 0
win = 100
snakes = {12:4, 45:32, 67:5, 99:1}
ladders = {3:43, 23:56, 38:78, 66:98}

# Removes the player if he wins
def remove_player(player):
    print("\n\n{} Won!\n\n".format(player))
    players.pop(player)

# Updates the position of the player
def update_position(player,dice):
    new_pos = players[player] + dice
    if new_pos == win:
        remove_player(player)
    elif new_pos in snakes.keys():
        players[player] = snakes[new_pos]
    elif new_pos in ladders.keys():
        players[player] = ladders[new_pos]
    elif (players[player] + dice) > win:
        pass
    else:
        players[player] = new_pos

# Rolls the dice
def roll_dice():
    for player in players:
        if player.split("_")[0] == "comp":
            dice = random.randrange(1,6)
            print("Dice value for comp is: {}".format(dice))
            update_position(player, dice)
        else:
            dice = int(input("Enter the dice value for {}: ".format(player)))
            update_position(player,dice)

# Takes user input
def user() :
    number_of_players = int(input("Enter the no. of users: "))
    for i in range(number_of_players):
        player = input("Enter the name: ")
        players.update({player:initial_position})
    comp_players = int(input("Enter the no. of comp players: "))
    for i in range(comp_players):
        comp = "comp_"+str(i)
        players.update({comp:initial_position})

# Starts the game
def game():
    user()
    while players:
        roll_dice()
        print(players)

game()