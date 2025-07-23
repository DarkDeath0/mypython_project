"""
    Written by Dark_Death0
    Solving the n-queen puzzle with the IDA* solution method
    
"""





def is_safe(board, row, col):
   # Checking for inconsistencies in rows, columns, and diagonals
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def heuristic(board):
    # Evaluation function: Number of pairs of ministers that threaten each other
    count = 0
    for i in range(len(board)):
        if board[i] == -1:
            continue
        for j in range(i + 1, len(board)):
            if board[j] == -1:
                continue
            if abs(board[i] - board[j]) == abs(i - j):
                count += 1
    return count

def solve_n_queens_ida_star(board, col, bound, solutions):
    if col == len(board):
        # An answer has been found. We add it to the list of answers
        solutions.append(list(board))
        return False  # We continue searching until all the answers are found.
    
    f = col + heuristic(board)  # Estimated cost (depth + assessment)
    if f > bound:
        return f  # Returns the new bound value
    
    min_bound = float('inf')  # Minimum new bound value
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[col] = row
            result = solve_n_queens_ida_star(board, col + 1, bound, solutions)
            if result == False:
                board[col] = -1  # Reset position
                return False  # All answers found
            min_bound = min(min_bound, result)
            board[col] = -1  # Reset position
    
    return min_bound

def solve_n_queens_ida(n):
    board = [-1] * n  # Chessboard with initial value -1 (empty spaces)
    solutions = []
    bound = heuristic(board)
    
    while True:
        result = solve_n_queens_ida_star(board, 0, bound, solutions)
        if result == False:  # All answers found
            break
        bound = result  # New bound value for the next round of searching
    
    return solutions

# Example for 8 ministers
solutions = solve_n_queens_ida(8)

# Display answers as a chessboard
def print_solution(solution):
    for row in solution:
        for col in range(len(solution)):
            if col == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Print all answers
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    print_solution(solution)
    print()