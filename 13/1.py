def is_saddle(matrix):
    target_cell = matrix[i][j]
    adjacent_cells = [matrix[i][j-1], matrix[i][j+1], matrix[i-1][j], matrix[i+1][j]]
    if target_cell > adjacent_cells[0] and target_cell > adjacent_cells[1] \
        and target_cell < adjacent_cells[2] and target_cell < adjacent_cells[3]:
        return True
    elif target_cell < adjacent_cells[0] and target_cell < adjacent_cells[1] \
        and target_cell > adjacent_cells[2] and target_cell > adjacent_cells[3]:
        return True
    return False

row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(map(int, (input().split()))))

counter = 0
for i in range(1, row-1):
    for j in range(1, col-1):
        counter += is_saddle(matrix)
    
print(counter)