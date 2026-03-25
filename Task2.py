def print_n_to_1(n):
    if n > 0:
        print(n, end=" ")
        print_n_to_1(n - 1)

n = int(input())
print_n_to_1(n)