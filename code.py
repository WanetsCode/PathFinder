import time
#╔═══╗      ╔╗ ╔╗   ╔═══╗        ╔╗       
#║╔═╗║     ╔╝╚╗║║   ║╔══╝        ║║       
#║╚═╝║╔══╗ ╚╗╔╝║╚═╗ ║╚══╗╔╗╔═╗ ╔═╝║╔══╗╔═╗
#║╔══╝╚ ╗║  ║║ ║╔╗║ ║╔══╝╠╣║╔╗╗║╔╗║║╔╗║║╔╝
#║║   ║╚╝╚╗ ║╚╗║║║║╔╝╚╗  ║║║║║║║╚╝║║║═╣║║ 
#╚╝   ╚═══╝ ╚═╝╚╝╚╝╚══╝  ╚╝╚╝╚╝╚══╝╚══╝╚╝
def newline():
    print("------------------------------------")

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end='')
        print()

def find_path(board, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = [(start, [])]
    visited = set()

    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == end:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != '🔲' and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None

def main():
    input_board = [
        ['🚩', '🔲', '🔲', '🏁', '🔲', '💠', '💠', '💠', '💠', '💠'],
        ['💠', '🔲', '🔲', '💠', '🔲', '💠', '💠', '💠', '💠', '💠'],
        ['💠', '🔲', '🔲', '💠', '🔲', '🔲', '🔲', '💠', '💠', '💠'],
        ['💠', '💠', '💠', '💠', '🔲', '💠', '🔲', '💠', '💠', '💠'],
        ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲']
    ]

    end_pos = None
    for i in range(len(input_board)):
        for j in range(len(input_board[0])):
            if input_board[i][j] == '🏁':
                end_pos = (i, j)
                break

    if end_pos is None:
        print("You need to place atleast 1 end position")
        return

    start_pos = None
    for i in range(len(input_board)):
        for j in range(len(input_board[0])):
            if input_board[i][j] == '🚩':
                start_pos = (i, j)
                break

    if start_pos is None:
        print("You need to place a start position")
        return

    path = find_path(input_board, start_pos, end_pos)

    if path is None:
        print("Error! This map is unbeatable, or you have placed too much elements")
    else:
        print("Path calculated")
        for step in path:
            board_copy = [row[:] for row in input_board]
            board_copy[step[0]][step[1]] = '🤖'
            newline()
            print_board(board_copy)
            time.sleep(0.5)  # Adjust the delay time as needed
            

if __name__ == "__main__":
    main()
