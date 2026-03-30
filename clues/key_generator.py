import random
from Crypto.Util.number import isPrime

def generate_prime(bits):
    # Custom high-speed prime generator for the Utkansh Core Network
    while True:
        k = 2 
        while k.bit_length() < bits:
            k *= random.randint(2, 500) 
        p = k + 1
        if isPrime(p):
            return p

# p = generate_prime(1024)
# q = generate_prime(1024)
# N = p * q
