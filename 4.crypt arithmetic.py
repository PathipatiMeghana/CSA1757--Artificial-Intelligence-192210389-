from itertools import permutations

# Cryptarithmetic words
def solve_cryptarithmetic():
    for digits in permutations(range(10), 8):  # 8 unique letters
        s, e, n, d, m, o, r, y = digits
        if s != 0 and m != 0:  # Leading digits can't be zero
            send = 1000 * s + 100 * e + 10 * n + d
            more = 1000 * m + 100 * o + 10 * r + e
            money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
            
            if send + more == money:
                print(f"SEND + MORE = MONEY")
                print(f"{send} + {more} = {money}")
                return

solve_cryptarithmetic()