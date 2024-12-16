def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.
    """
    if not nums or x < 1:
        return None

    # Precompute primes up to the maximum number in nums
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Precompute the number of primes removed for each n
    # `prime_counts[n]` will store the total number of primes used up to n
    prime_counts = [0] * (max_num + 1)
    count = 0
    for i in range(1, max_num + 1):
        if primes[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    # Simulate the game for each round
    for n in nums:
        # If prime_counts[n] is odd, Maria wins; otherwise, Ben wins
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def sieve_of_eratosthenes(n):
    """
    Generates a list of primes up to n using the Sieve of Eratosthenes.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes

