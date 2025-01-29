def isWinner(x, nums):
    # Function to find all prime numbers up to n using the Sieve of Eratosthenes
    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(2, n + 1) if is_prime[i]]
    
    maria_wins = 0
    ben_wins = 0
    
    # Simulate each round
    for n in nums:
        primes = sieve(n)
        # If the number of primes is odd, Maria wins, else Ben wins
        if len(primes) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Return the player who won more rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

