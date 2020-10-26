import random
def create_lists():
    player_x_list = ["x", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",]
    player_o_list = ["o", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",]

    return player_x_list, player_o_list

def roll_the_die(turn):
    if turn % 2 != 0:
        input("Player x press enter to roll!")
        die_roll = random.randint(1,6)
        print("Player x rolled a", die_roll)
        #turn = turn + 1

    else: # whos_turn % 2 == 0
        input("Player o press enter to roll!")
        die_roll = random.randint(1,6)
        print("Player x rolled a", die_roll)
        #turn = turn + 1
    
    return die_roll

def display_game_state(player_x_list, player_o_list):
    astericks = '*' * 36
    print(astericks)
    print("Player x: ", ' '.join(player_x_list))
    print("Player o: ", ' '.join(player_o_list))
    print(astericks)
    
 
def update_player_x(die_roll, player_x_list):
    # find index value of previous 'x' position
    for index in range(len(player_x_list)):
        if ord(player_x_list[index]) == 120:
            previous_pos_x = index
            player_x_list[index] = '-' # change previous index to = '-'

    player_x_list[previous_pos_x + die_roll] = 'x' # find new position with previous index + die_roll

def update_player_o(die_roll, player_o_list):
    # find index value of previous 'o' position
    for index in range(len(player_o_list)):
        if ord(player_o_list[index]) == 111:
            previous_pos_o = index
            player_o_list[index] = '-' # change previous index to = '-'

    player_o_list[previous_pos_o + die_roll] = 'o' # find new position with previous index + die_roll

def update_players_pos(die_roll, player_x_list, player_o_list, turn):
    if turn % 2 != 0:
        update_player_x(die_roll, player_x_list)
        turn = turn + 1
    else:
        update_player_o(die_roll, player_o_list)
        turn = turn + 1

    return turn

def game_end(game, player_x_list, player_o_list):
    if ord(player_x_list[12]) == 120:
        game = False
    elif ord(player_o_list[12]) == 111:
        game = False
    return game


def main():
# print starting lines
    print("Players begin in the starting position")
    player_x_list, player_o_list = create_lists()
    game = True
    turn = 1
    while game:
    # start of loop here:
        display_game_state(player_x_list, player_o_list)
        die_roll = roll_the_die(turn)
        turn = update_players_pos(die_roll, player_x_list, player_o_list, turn)
        game_end(game, player_x_list, player_o_list)


main()



    
    
    
    