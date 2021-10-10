# --------------------------------------------------------------------
# Given five positive integers, find the minimum and maximum values that can be
# calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# ---------------------------------------------------------------------

def min_max_sum(arr):
    arr = sorted(arr)
    max_sum = sum(arr[1:])
    min_sum = sum(arr[:-1])
    print(f"{min_sum} {max_sum}")

    




if __name__ == '__main__':
    # arr = list(map(int, input().strip().split())) # input seperated by space

    test_arr = [1, 3, 5, 7, 9]
    test2 = [7, 69, 2, 221, 8974]
    min_max_sum(test_arr)
    min_max_sum(test2)
        