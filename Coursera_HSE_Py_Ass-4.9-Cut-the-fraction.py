def ReduceFraction(red_n, red_m):
    if red_n > 1 and red_m > 1:
        for d in range(2, min(red_n, red_m) + 1):
            if red_n % d == 0 and red_m % d == 0:
                return ReduceFraction(red_n // d, red_m // d)
            elif d == min(red_n, red_m):
                return red_n, red_m
    else:
        return red_n, red_m


n = int(input())
m = int(input())
print(ReduceFraction(n, m)[0], ReduceFraction(n, m)[1])
