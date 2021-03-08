#def game():

#def search:
#    abertos = [0]
#    fechados = []
#    x = None
#    while abertos != []:
#        x = abertos[0]
#        abertos.pop(1)
#        if x == board_final:
#            break
#            print("Sucesso")
#            print('')
#            print(board)
#        else:

#def generating_board:
#    a = {}

#def search_empty:


def draw_board():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()

board = [[1,2,3],
         [4,5,0],
         [7,8,9]]
board_final = [[1,2,3],
               [4,5,6],
               [0,7,8]]
state_board = [0,[]]
board.index(0)
draw_board()