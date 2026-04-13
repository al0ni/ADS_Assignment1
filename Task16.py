def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    return binary_search(arr, target, mid + 1, high)

user_input = input()
arr = [int(x) for x in user_input.split()]
target = int(input())

index = binary_search(arr, target, 0, len(arr) - 1)
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Not found")

# Time Complexity: O(log n)
# Space Complexity: O(log n)
