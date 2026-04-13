def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

n = int(input())
print(sum_numbers(n))
# Time Complexity: O(n)
# Space Complexity: O(n)
