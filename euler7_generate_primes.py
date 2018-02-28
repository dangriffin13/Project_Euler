import sys, math

def is_prime(number, primes_list_exc_2):
    #sieve of eratosthenes: check if divisible by primes lower than n^.5
    sqrt_n = math.sqrt(number)
    i = 0
    sieve_val = primes_list_exc_2[i] #assign val to avoid repeat o(n) of index
    while sieve_val <= sqrt_n:
        if number % sieve_val == 0:
            return False
        else:
            i += 1
            sieve_val = primes_list_exc_2[i]
    return True
    
primes_list = [2,3]
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) 
    
    if n > len(primes_list):
        peek_value = primes_list[-1]
        while n > len(primes_list):
            if is_prime(peek_value + 2, primes_list[1:]): #passing only odds, so don't need 2
                primes_list.append(peek_value + 2)
            peek_value += 2
            
    
    print(primes_list[n-1])