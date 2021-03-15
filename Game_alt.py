import os
import copy
import time
import platform

#Detectar o sistema operacional
op_sys = platform.system()


# Gerar filho de x para cada movimento executado
def move_panel(row, col, rowP, colP):
    global board_aux, x

    board = copy.deepcopy(x)
    aux = board[row][col]
    board[row][col] = board[rowP][colP]
    board[rowP][colP] = aux
    if board not in _close:
        if board not in _open:
            board_aux.append(board.copy())


# Movimentar painel
def map_panels(position):
    global x, _close, _open

    global board_aux
    board_aux = []

    row = position[0]
    col = position[1]
    
    # Mover para cima
    if row+1 < 3:
        move_panel(row, col, row+1, col)

    # Mover para direita
    if col-1 >= 0:
        move_panel(row, col, row, col-1)

    # Mover para baixo
    if row-1 >= 0:
        move_panel(row, col, row-1, col)

    # Mover para a esquerda
    if col+1 < 3:
        move_panel(row, col, row, col+1)

    # Add valores filhos à aberto
    board_aux.reverse()
    for index in board_aux:
        _open.insert(0, index.copy())
    
    # Add estado atual à fechado
    _close.append(copy.deepcopy(x))


# Encontrar posição do valor vazio
def empty_value():
    global x

    for i in x:
        if 0 in i:
            return [x.index(i), i.index(0)]


# Gerar posições de vazio e mapear movimentos
def generate_child():
    position = empty_value()
    map_panels(position)


def start(): # Atribuir o valor atual
    global _open, x

    x = _open[0].copy()
    del _open[0]
  

if __name__=='__main__':
    global _open, _close, x

    # Valor 0 representa vazio
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

    _open = [initial]
    _close = []

    while _open != []:
        start()

        if x == final:
            # Mostrar o caminho até o objetivo
            for index in _close:
                if op_sys == "Linux":
                    os.system("clear")
                elif op_sys == "Windows":
                    os.system("cls")

                for index, value in enumerate(index):
                    for i, v in enumerate(value):
                        if v == 0:
                            print(' _ ', end=' ')
                        else:
                            print(f' {v} ', end=' ')
                    print('')
                #print("\n   | \n   |")
                time.sleep(1)
            
            # Mostrar o objetivo
            if op_sys == "Linux":
                os.system("clear")
            elif op_sys == "Windows":
                os.system("cls")
            
            for index, value in enumerate(x):
                for i, v in enumerate(value):
                    if v == 0:
                            print('\033[32m'+' _ '+'\033[32m', end=' ')
                    else:
                        print(f'\033[32m {v} \033[32m', end=' ')
                print('')
            print()
            print('\033[32m'+'SUCESSO!!'+'\033[32m')
            break

        else:
            generate_child()
