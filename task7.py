def check(game):
    result = ""
    for j in range(0, 3):
        if game[0][j] == game[1][j] == game[2][j]:
            result = game[0][j]
            print(result)
    # column check
    for j in range(0, 3):
        if game[j][0] == game[j][1] == game[j][2]:
            result = game[j][0]
            print(result)
    # string check
    for j in range(0, 3):
        if game[0][0] == game[1][1] == game[2][2]:
            result = game[0][0]
            print(result)
    # diagonal check
    else:
        if result == "":
            print('D')
check(['X.O','XX.','OOO'])