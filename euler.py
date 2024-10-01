def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def eulers_totient(n):
    count = 0
    
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    
    return count