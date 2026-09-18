import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    h = int(input_data[1])
    w = int(input_data[2])

    cur_x = int(input_data[3]) - 1
    cur_y = int(input_data[4]) - 1

    moves = input_data[5]
    grid_tokens = input_data[6 : 6 + h * w]
    grid = [
        [int(grid_tokens[r * w + c]) for c in range(w)]
        for r in range(h)
    ]

    direction = {
        'F' : (-1, 0),
        'B' : (1, 0),
        'L' : (0, -1),
        'R' : (0, 1),
    }

    results = []
    
    for move in moves:
        dx, dy = direction[move]
        cur_y += dy
        cur_x += dx

        chocolsates = grid[cur_y][cur_x]
        results.append(chocolsates)
        print(chocolsates)
    
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()