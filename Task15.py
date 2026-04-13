def is_sorted(arr):
    if len(arr) <= 1:
        return "Sorted"
    if arr[0] > arr[1]:
        return "Not sorted"
    return is_sorted(arr[1:])

user_input = input()
arr = [int(x) for x in user_input.split()]

print(is_sorted(arr))
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
