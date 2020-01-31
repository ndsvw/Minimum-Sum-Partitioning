def min_sum_first_attempt(arr):
    n = len(arr)
    sum_of_all = sum(arr)
    matrix = [[0 for _ in range(sum_of_all+1)] for _ in range(n)]
    matrix[0] = [abs(sum_of_all - i - i) for i in range(sum_of_all+1)]
    for i in range(1, n):
        for j in range(sum_of_all, -1, -1):
            matrix[i][j] = matrix[i-1][j]
            if j+arr[i] <= sum_of_all:
                if matrix[i-1][j+arr[i]] <= matrix[i][j]:
                    matrix[i][j] = matrix[i-1][j+arr[i]]
    return matrix[n-1][0]


def min_sum_space_improved(arr):
    n = len(arr)
    sum_of_all = sum(arr)
    matrix = [
        [abs(sum_of_all - i - i) for i in range(sum_of_all+1)],
        [None for _ in range(sum_of_all+1)]
    ]
    for i in range(1, n):
        for j in range(sum_of_all, -1, -1):
            matrix[1][j] = matrix[0][j]
            if j+arr[i] <= sum_of_all:
                if matrix[0][j+arr[i]] <= matrix[1][j]:
                    matrix[1][j] = matrix[0][j+arr[i]]
        matrix[0] = [e for e in matrix[1]]
    return matrix[1][0]
