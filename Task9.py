def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))
# Time Complexity: O(2^n)
# Space Complexity: O(n)
