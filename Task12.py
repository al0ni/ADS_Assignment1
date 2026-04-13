def array_max(arr):
    if len(arr) == 1:
        return arr[0]
    sub_max = array_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

user_input = input()
arr = [int(x) for x in user_input.split()]
print(array_max(arr))
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
