import logging
def check(game):
    logging.basicConfig(level = logging.DEBUG, filename = 'game.log',
                        format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    result = ""
    # column check
    for j in range(0, 3):
        if game[0][j] == game[1][j] == game[2][j]:
            result = game[0][j]
            print(result)
            logging.debug(f"{result} wins!")
    # string check
    for j in range(0, 3):
        if game[j][0] == game[j][1] == game[j][2]:
            result = game[j][0]
            print(result)
            logging.debug(f"{result} wins!")
    # diagonal check
    if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0]:
        result = game[0][0]
        print(result)
        logging.debug(f"{result} wins!")
    else:
        if result == "":
            print('D')
            logging.debug("no one wins!")
check(['X.O','XX.','OOO'])