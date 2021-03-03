sum = 0
for i in range(1,1001):
    for j in range(1,1001):
        if(i == j):
            sum += (i ** j)

sum = str(sum)
reversed_sum = sum[::-1]
d = 0
digit = list()
for digits in reversed_sum:
    if(d < 10):
        digits = int(digits)
        digit.append((digits%10))
        digits /= 10
        d += 1

print(digit)
