import itertools


def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal

    for row in current_game:
        print(row)
        if all_same(row):
            print(f'Player {row[0]} is the winner horizontally!')
            return True

    # Vertical
    for col in range(len(current_game)):
        checker = []
        for row in current_game:
            checker.append(row[col])
        if all_same(checker):
            print(f'Player {checker[0]} is the winner vertical (|)')
            return True

    # Diagonal
    diax = []
    for col, row in enumerate(reversed(range(len(current_game)))):  # a flash point to get error
        diax.append(current_game[row][col])
    if all_same(diax):
        print(f'Player {diax[0]} is the winner diagonal (/)')
        return True

    diax = []
    for idx in range(len(current_game)):
        diax.append(current_game[idx][idx])
    if all_same(diax):
        print(f'Player {diax[0]} is the winner diagonal (\\)')
        return True

    return False


def game_space(game_map, player=0, row=0, col=0, just_show=False):
    print('-' * 100)
    print(f'having Fun is the goal.')
    print("-" * 100)
    try:
        if game_map[row][col] != 0:
            print('The space you choose is occupied! choose another')
            return game_map, False

        print('   ' + '  '.join(str(i) for i in range(len(game_map))))

        if not just_show:
            game_map[row][col] = player

        for counter, rows in enumerate(game_map):
            print(counter, rows)
        return game_map, True
    except IndexError as e:
        print("Error: make sure you input column/row as 0,1 or 2 ", e)
        return game_map, False

    except Exception as e:
        print('something is wrong!!!', e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game, _ = game_space(game, just_show=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f'current player {current_player}')
        played = False
        while not played:
            try:
                row_choice = int(input('what row do you want to play? 0, 1, 2: '))
            except ValueError as v:
                print("check your input, it has to be 0,1 or 2: ", v)
                row_choice = int(input('what row do you want to play? 0, 1, 2: '))
            try:
                column_choice = int(input('What column do you want to play? 0, 1, 2: '))
            except ValueError as v:
                print("check your input, it has to be 0,1 or 2: ", v)
                column_choice = int(input('what row do you want to play? 0, 1, 2: '))

            game, played = game_space(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n): ")
            if again.lower() == 'y':
                print("restarting")

            elif again.lower() == 'n':
                print('Byeeeeeeeeeeeee')
                play = False
            else:
                print('Not a valid answer')
                play = False