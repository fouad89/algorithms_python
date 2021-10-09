# ----------------------------------------------------------------
# Staircase detail

# This is a staircase of n=4 size :

#    #
#   ##
#  ###
# ####
# Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size .
# ----------------------------------------------------------------

def staircase(n):
    for i in range(1, n+1):
        if i == n:
            print('#'*i)
        else:
            print(' '*(n-i-1),'#'*i)




if __name__ == '__main__':
    n = int(input('Number of steps: ').strip())
    # n_test = 4
    staircase(n)


      #