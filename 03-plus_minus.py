# ------------------------------------------------------------------------------------------------
# Given an array of integers, calculate the ratios of its elements that are positive, 
# negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

# Note: This challenge introduces precision problems.
# The test cases are scaled to six decimal places, 
# though answers with absolute error of up to 10^-4 are acceptable.
# ------------------------------------------------------------------------------------------------


def plus_minus(arr):
    num_positive = 0
    num_zeros = 0
    num_negative = 0
    for i in arr:
    #     if i == 0:

        num_positive += i > 0
        num_zeros += i == 0
        num_negative += i < 0
    r_positive = round(num_positive / len(arr), 6)
    r_zeros = round(num_zeros / len(arr),6)
    r_negative = 1 - r_positive - r_zeros
    print(f"{r_positive}\n{r_negative}\n{r_zeros}")
        




if __name__ == '__main__':
    test_arr = [-4, 3, -9, 0, 4, 1]

    


    plus_minus(test_arr)