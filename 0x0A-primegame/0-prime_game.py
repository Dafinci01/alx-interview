def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if x <= 0 or not nums:
        return None

    # Process only the first x elements of nums
    considered_nums = nums[:x]
    max_n = max(considered_nums) if considered_nums else 0

    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i : max_n+1 : i] = [False] * len(sieve[i*i : max_n+1 : i])

    # Compute the cumulative count of primes up to each number
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in considered_nums:
        if n < 0:
            # No primes in negative numbers, Ben wins
            ben_wins += 1
            continue
        # Ensure we don't index out of bounds
        cnt = prime_count[n] if n <= max_n else 0
        if cnt % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

