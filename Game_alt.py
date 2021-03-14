
import os
import copy

class board:
    def __init__(self):
        self.name = name
        self.board = board
        self.boards = boards
    

    def printBoard(self):
        print(name)
        print(board)


# Movimentar painel
def move_panel(position):
    global x, _close, _open, count

    #for index in x:
    #    print(index)

    row = position[0]
    col = position[1]

    board_aux = []
    # Mover para cima
    if row+1 < 3:
        board_up = copy.deepcopy(x)
        aux = board_up[row][col]
        board_up[row][col] = board_up[row+1][col]
        board_up[row+1][col] = aux
        #print('mover para cima')
        #for index in board_up:
        #    print(index)
        if board_up not in _close:
            if board_up not in _open:
                # _open.append(board_up.copy())
                board_aux.append(board_up.copy())
    
    # Mover para direita
    if col-1 >= 0:
        board_right = copy.deepcopy(x)
        aux = board_right[row][col]
        board_right[row][col] = board_right[row][col-1]
        board_right[row][col-1] = aux
        #print('mover para direita')
        #for index in board_right:
        #    print(index)
        if board_right not in _close:
            if board_right not in _open:
                #_open.append(board_right.copy())
                board_aux.append(board_right.copy())

    # Mover para baixo
    if row-1 >= 0:
        board_down = copy.deepcopy(x)
        aux = board_down[row][col]
        board_down[row][col] = board_down[row-1][col]
        board_down[row-1][col] = aux
        #print('mover para baixo')
        #for index in board_down:
        #    print(index)
        if board_down not in _close: 
            if board_down not in _open:
                #_open.append(board_down.copy())
                board_aux.append(board_down.copy())

    # Mover para a esquerda
    if col+1 < 3:
        board_left = copy.deepcopy(x)
        aux = board_left[row][col]
        board_left[row][col] = board_left[row][col+1]
        board_left[row][col+1] = aux
        #print('mover para esquerda')
        #for index in board_left:
        #    print(index)
        if board_left not in _close:
            if board_left not in _open:
                # _open.append(board_left.copy())
                board_aux.append(board_left.copy())

    board_aux.reverse()
    for index in board_aux:
        _open.insert(0, index.copy())
    

    print(f'add {x} x À fechado')
    _close.append(copy.deepcopy(x))
    

def empty_value():
    global x

    for index in x:
        if 0 in index:
            return [x.index(index), index.index(0)]


def generate_child():
    position = empty_value()
    #sprint(position)
    #input()
    move_panel(position)

def start():
    global _open, x

    x = _open[0].copy()
    del _open[0]
    

if __name__=='__main__':

    initial = [
        [1,2,3], 
        [4,5,0], 
        [7,8,6]
        ]

    final = [
        [1,2,3], 
        [4,5,6], 
        [0,7,8]
        ]

    global _open
    _open = [initial]
    global _close
    _close = []
    global x

    while _open != []:
        start()

        if x == final:
            walk = list(map(lambda lista: print(f'{lista[0]}\n{lista[1]}\n{lista[2]}\n  |\n  |'), _close))
  
            goal = list(map(lambda row: print(f'{row}'), x))
            break
        else:
            generate_child()

    #del _open[0]
    #print(_open[0])
    #print(_open)
    #prt1 = list(map(lambda lista: print(f'{lista[0]}\n{lista[1]}\n{lista[2]}\n  |\n  |'), _close))
