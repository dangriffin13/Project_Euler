n = int(input())

largest = 0

    
for i in range(2, n):
    for j in range(2, n):
        num = pow(i, j)
        digits = list(str(num))
        digital_sum = sum([int(i) for i in digits])
        if digital_sum > largest:
            largest = digital_sum
print(largest)