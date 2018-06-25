import math

t = int(input())


def sum_of_divisors(number):
    s = 0
    stop = int(math.floor(math.sqrt(number)))
    for i in range(2,stop):
        if number%i == 0:
            s += i + number/i
    return int(s+1)


amicable_numbers = []    
for i in range(100001):
    y = sum_of_divisors(i)
    if sum_of_divisors(y) == i and i != y and i not in amicable_numbers:
        if y < 100001:
            amicable_numbers.extend([i, y])
            #print(amicable_numbers)
        else:
            amicable_numbers.append(i)
            #print(amicable_numbers)

for _ in range(t):
    n = int(input())
    print(sum([i for i in amicable_numbers if i < n]))