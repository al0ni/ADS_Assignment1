def linear_search(arr, target):
    if not arr:
        return "Not found"
    if arr[0] == target:
        return "Found"
    return linear_search(arr[1:], target)

user_input = input()
arr = [int(x) for x in user_input.split()]
target = int(input())
print(linear_search(arr, target))
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
