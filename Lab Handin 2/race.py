import random

# this function creates the lists from which we derive the positions of player x and y
def create_lists():
    player_x_list = ["x", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",]
    player_o_list = ["o", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",]

    return player_x_list, player_o_list


# this function generates a random number from 1 to 6
# the parameter turn is type integer
def roll_the_die(turn):
    # if the remainder of turn/2 is 0, then it is even. Player 'x' is coded to be odd, player 'o' is coded to be even.
    # We keep track of each player's die rolls using the turn value
    if turn % 2 != 0:
        input("Player x press enter to roll!")
        die_roll = random.randint(1,6)
        print("Player x rolled a", die_roll)
        #turn = turn + 1

    else: # whos_turn % 2 == 0
        input("Player o press enter to roll!")
        die_roll = random.randint(1,6)
        print("Player o rolled a", die_roll)
        #turn = turn + 1
    
    return die_roll


# We display the player's positions
# Both parameters are type list
def display_game_state(player_x_list, player_o_list):
    astericks = '*' * 36
    print(astericks)
    print("Player x: ", ' '.join(player_x_list)) # use the .join() to get rid of '[', ']' and ' ,'
    print("Player o: ", ' '.join(player_o_list))
    print(astericks)
    

# use the value from roll_the_die to update the player position lists
# the paramter die_roll is type integer, whereas the other it type list
def update_player_x(die_roll, player_x_list):
    # find index value of previous 'x' position
    for index in range(len(player_x_list)):
        if ord(player_x_list[index]) == 120:
            previous_pos_x = index
            player_x_list[index] = '-' # change previous index to = '-'

    # as long as they don't over roll, then they keep moving forward 
    if previous_pos_x + die_roll <= 12:
        player_x_list[previous_pos_x + die_roll] = 'x' # find new position with previous index + die_roll
    else:
        player_x_list[0] = 'x'
        player_x_list[previous_pos_x] = '-'


# use the value from roll_the_die to update the player position lists
# the paramter die_roll is type integer, whereas the other it type list
def update_player_o(die_roll, player_o_list):
    # find index value of previous 'o' position
    for index in range(len(player_o_list)):
        if ord(player_o_list[index]) == 111:
            previous_pos_o = index
            player_o_list[index] = '-' # change previous index to = '-'

    # as long as they don't over roll, then they keep moving forward 
    if previous_pos_o + die_roll <= 12:
        player_o_list[previous_pos_o + die_roll] = 'o' # find new position with previous index + die_roll
    else: # other wise we reset the list back to starting positions
        player_o_list[0] = 'o'
        player_o_list[previous_pos_o] = '-'

# Update a player list depending on who's turn it is
# The parameters die_roll and turn are type int, the other 2 are type list
def update_players_pos(die_roll, player_x_list, player_o_list, turn):
    if turn % 2 != 0:
        update_player_x(die_roll, player_x_list)
        turn = turn + 1 # add 1 for each round, so the turns alternate
    else: # other wise we reset the list back to starting positions
        update_player_o(die_roll, player_o_list)
        turn = turn + 1

    return turn

# this is the game end condition. where the last index is 'x' or 'o'
# the parameter game is type bool, the other two are type list
def game_end(game, player_x_list, player_o_list):
    if ord(player_x_list[12]) == 120:
        game = False
        display_game_state(player_x_list, player_o_list)
        print("Player x has won!")
    elif ord(player_o_list[12]) == 111:
        game = False
        display_game_state(player_x_list, player_o_list)
        print("Player o has won!")
    return game


def main():
    # print starting lines
    print("Players begin in the starting position")
    player_x_list, player_o_list = create_lists()
    game = True # set game to True so game can start
    turn = 1 # set turn to 1 so die_rolls will start for player x
    while game:
    # start of loop here:
        display_game_state(player_x_list, player_o_list)
        die_roll = roll_the_die(turn)
        turn = update_players_pos(die_roll, player_x_list, player_o_list, turn)
        game = game_end(game, player_x_list, player_o_list)

main()



    
    
    
    