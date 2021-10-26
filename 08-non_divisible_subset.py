# --------------------------------------------------------------------
# Given a set of distinct integers, print the size of a 
# maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.
# --------------------------------------------------------------------

def non_divisible_subset(k, s):
    res = 0
    non_div = []
    for i in range(s):
        for j in range(s):
            if i == j:
                continue
            else:
                if s[i] + s[j] % k != 0:
                    res +=1
                    non_div.append(s.pop(i))


    

    return res







if __name__ == '__main__':
    test_arr = [1, 7, 2, 4]
    non_divisible_subset(3, test_arr)

    