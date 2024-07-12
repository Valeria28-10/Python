# Задание 1. 
# Напишите функцию для транспонирования матрицы.

def transpose_matrix(matrix):
    transposed_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return(transposed_matrix)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    print(f"Изначальная матрица: ", matrix)
    print(f"Транспонированная матрица: ", transpose_matrix(matrix))