def array_sum(arr):
    if not arr:
        return 0
    return arr[0] + array_sum(arr[1:])

user_input = input()
arr = [int(x) for x in user_input.split()]

print(array_sum(arr))
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
