# ---------------------------------------------------------------------------------
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# ---------------------------------------------------------------------------------

def diagonal_difference(arr):
    res = 0
    left_right_diag = 0
    right_left_diag = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            # left to right digonal 
            if i == j:
                left_right_diag += arr[i][j]
            elif (i + j == len(arr)):
                right_left_diag += arr[i][j]
            else: pass
    print(left_right_diag)
    print(right_left_diag)
    res = abs(left_right_diag - right_left_diag)


    return res






if __name__=='__main__':
    test_arr = [list(range(1,4)), list(range(4,7)), [9, 8, 9]]
    print(len(test_arr))
    test2 = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    diagonal_difference(test_arr)
    print(diagonal_difference(test_arr))