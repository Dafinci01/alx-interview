def isWinner(x, nums):
    """
    Determines the winner of a game where players alternate picking numbers from a list.

    Args:
        x (int): The maximum number of primes a player can pick.
        nums (list): A list of numbers.

    Returns:
        str: The name of the winner ("Maria" or "Ben"), or None if there is no winner.
    """
    if x == 0 or not nums:
        return None

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i : max_n+1 : i] = [False] * len(sieve[i*i : max_n+1 : i])

    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        cnt = prime_count[n]
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
