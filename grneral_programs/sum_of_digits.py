def add_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    while sum > 9:
        sum = add_digits(sum)
    return sum

n = int(input())
print(add_digits(n))
