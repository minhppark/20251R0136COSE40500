def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        print(f"Fetching memo[{n}] = {memo[n]}")
        return memo[n]
    if n <= 2:
        return 1
    print(f"Computing fibonacci({n})")
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def generate_sequence(count):
    print(f"Generating Fibonacci sequence up to {count}:")
    for i in range(1, count + 1):
        print(f"fib({i}) = {fibonacci(i)}")

if __name__ == "__main__":
    generate_sequence(10)