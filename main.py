active_player = "X"
round_counter = 0
winner = ""
separator = "=" * 40
rules = f"GAME RULES:\nEach player can place one mark (or stone)\nper turn on the 3x3 grid. The WINNER is\nwho succeeds in placing three of their\nmarks in a:\n* horizontal,\n* vertical,\n* diagonal row"
grid_line = "+---+---+---+"
cells = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
"""
cells:
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
"""

def print_rules():
    print("Welcome to Tic Tac Toe")
    print(separator)
    print(rules)
    print(separator)
    print("Let's start the game")
    print("-" *40)

def print_grid():
    print(grid_line)
    print("| {} | {} | {} |".format(cells["7"], cells["8"], cells["9"]))
    print(grid_line)
    print("| {} | {} | {} |".format(cells["4"], cells["5"], cells["6"]))
    print(grid_line)
    print("| {} | {} | {} |".format(cells["1"], cells["2"], cells["3"]))
    print(grid_line)

def player_move(player):
    print(separator)

    while True:
        global active_player, round_counter
        move = input(f"Player {player} | Please enter your move number: ")

        if move in cells:
                if cells[move] == " ":
                    cells[move] = player
                    round_counter += 1
                    if active_player == "X":
                        active_player = "O"
                    else:
                        active_player = "X"
                    break
                else:
                    print(f"Cell {move} is not empty!")
        else:
            print("Please enter number in range 1-9!")
    print(separator)

def check_results():
    global winner

    if cells["1"] == cells["2"] == cells["3"] != " ":
        winner = cells["1"]
        return False
    elif cells["4"] == cells["5"] == cells["6"] != " ":
        winner = cells["4"]
        return False
    elif cells["7"] == cells["8"] == cells["9"] != " ":
        winner = cells["7"]
        return False
    elif cells["1"] == cells["4"] == cells["7"] != " ":
        winner = cells["1"]
        return False
    elif cells["2"] == cells["5"] == cells["8"] != " ":
        winner = cells["2"]
        return False
    elif cells["3"] == cells["6"] == cells["9"] != " ":
        winner = cells["3"]
        return False
    elif cells["1"] == cells["5"] == cells["9"] != " ":
        winner = cells["1"]
        return False
    elif cells["3"] == cells["5"] == cells["7"] != " ":
        winner = cells["3"]
        return False
    elif round_counter == 9:
        winner = "draw"
        return False
    else:
        return True

if __name__ == '__main__':
    print_rules()
    print_grid()

    while True:
        player_move(active_player)
        print_grid()

        if check_results():
            continue
        else:
            print(separator)
            if winner in "XO":
                print(f"Congratulations, the player {winner} WON!")
            else:
                print("DRAW!")
            print(separator)
            break

            print("ahoj")