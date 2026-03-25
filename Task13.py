def count_occurrences(arr, target):
    if not arr:
        return 0
    count = 1 if arr[0] == target else 0
    return count + count_occurrences(arr[1:], target)

user_input = input()
arr = [int(x) for x in user_input.split()]
target = int(input())
print(count_occurrences(arr, target))