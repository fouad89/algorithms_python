# --------------------------------------------------------------------
# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age.
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
# --------------------------------------------------------------------

def birthday_candles(candles):
    tallest = max(candles)
    counter = 0
    for i in candles:
        if i == tallest:
            counter += 1
    return counter





if __name__ == '__main__':
    test_candles = [4, 4, 1, 3]

    print(birthday_candles(test_candles))