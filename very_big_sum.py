# ----------------------------------------------------------------
# In this challenge, you are required to calculate and print the sum of the elements in an array, 
# keeping in mind that some of those integers may be quite large.

# Function Description

# Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

# aVeryBigSum has the following parameter(s):

# int ar[n]: an array of integers .
# ----------------------------------------------------------------

def very_big_sum(arr):
    res = 0
    for i in arr:
        res += i
    return res


if __name__ == '__main__':
    test_arr = [10**5, 10**10, 30**10, 30**10, 30**10]
    print(very_big_sum(test_arr))
    