import sys, math

def divisible_by_two(number): #check for power of two
    if number/2 % 2 != 0
        return int(number/2)
    else:
        return divisible_by_two(number/2)
    

def factorization(number):
    #print('entered factor', number)
    i = 3
    sqrt_n = math.sqrt(number)
    while i <= sqrt_n and number % i != 0:
        i += 2
    if i > sqrt_n: #if i reaches sqrt_n, then no further factors
        #print('i, sqrt_n', i, sqrt_n)
        return number
    else:
        #print('recursive return', number//i)
        return factorization(number//i)
        
        
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    if n % 2 == 0:
        n = divisible_by_two(n)
        #print('new n', n)
    
    if n == 1:
            factor = 2         
    else: 
        factor = factorization(n)
        
    print(factor)