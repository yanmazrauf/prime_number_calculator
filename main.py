def primes_in_range(start, end):
    limit = end
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    primes = []
    for num in range(start, limit + 1):
        if is_prime[num]:
            primes.append(num)
    return primes

start = int(input("Lower limit of range: "))
end = int(input("Upper Limit of range: "))

primes = primes_in_range(start, end)

print("Total number of prime numbers:", len(primes))
print("First 10 prime numbers:", primes[:10])

