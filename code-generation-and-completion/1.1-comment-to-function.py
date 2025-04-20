#Return the nth Fibonacci number using memoization
def fibonacci(n):
    memo = {}
    def fib(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    return fib(n)


# Test the function
# print(fibonacci(10))  # Output: 55

# tests for fibonacci function
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
# Run the tests
# test_fibonacci()


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# tests for gcd
def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(56, 98) == 14
    assert gcd(101, 10) == 1
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0
# Run the tests
test_gcd()

