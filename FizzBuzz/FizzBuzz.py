print("Введите натуральное число:")
n = int(input())

for count in range(1, n + 1):
    t = count % 3 == 0
    f = count % 5 == 0
    if (t):
        if (f):
            print("fizzbuzz")
        else:
            print("fizz")
    elif (f):
        print("buzz")
    else:
        print(count)