def square_matrix_simple(matrix=[]):
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    
    # Create a new matrix to store the squared values
    squared_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Compute the square values and store them in the new matrix
    for i in range(rows):
        for j in range(cols):
            squared_matrix[i][j] = matrix[i][j] ** 2
    
    return squared_matrix
