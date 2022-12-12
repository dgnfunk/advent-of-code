from os.path import dirname, join
import pprint
pp = pprint.PrettyPrinter(depth=4)
#     [C]             [L]         [T]
#     [V] [R] [M]     [T]         [B]
#     [F] [G] [H] [Q] [Q]         [H]
#     [W] [L] [P] [V] [M] [V]     [F]
#     [P] [C] [W] [S] [Z] [B] [S] [P]
# [G] [R] [M] [B] [F] [J] [S] [Z] [D]
# [J] [L] [P] [F] [C] [H] [F] [J] [C]
# [Z] [Q] [F] [L] [G] [W] [H] [F] [M]
#  1   2   3   4   5   6   7   8   9 

def get_prep_data_stack():
    uno = ['Z', 'J', 'G']
    dos = ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C']
    tres = ['F', 'P', 'M', 'C', 'L', 'G', 'R']
    cuatro = ['L', 'F', 'B', 'W', 'P', 'H', 'M']
    cinco = ['G', 'C', 'F', 'S', 'V', 'Q']
    seis = ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L']
    siete = ['H', 'F', 'S', 'B', 'V']
    ocho = ['F', 'J', 'Z', 'S']
    nueve = ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']
    
    return [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve]

def print_stacks(stacks):
    count = 0
    for stack in stacks:
        count += 1
        col = f'{count} '
        for row in range(21):
            try:
                col = col + f'[{stack[row]}]'
            except IndexError:
                col = col + '[ ]'
        print(col)


def get_movements():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, 'r') as f:
        movements = []
        for line in f:
            clean_line = line.rstrip()
            raw_move = clean_line.split(' ')
            movement = {
                'qty': int(raw_move[1]),
                'from': int(raw_move[3]) - 1,
                'to': int(raw_move[5]) - 1
            }

            movements.append(movement)
        
        return movements

def day3_solution():
    stacks = get_prep_data_stack()
    print_stacks(stacks)

    movements = get_movements()
    pp.pprint(movements)

    for move in movements:
        qty_moves = range(move['qty'])
        from_stack = stacks[move['from']]
        to_stack = stacks[move['to']]
        for i in qty_moves:
            crate = from_stack.pop()
            print('Popped crate', crate)
            to_stack.append(crate)
        
        print_stacks(stacks)

if __name__ == '__main__':
    day3_solution()