def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list


num_terms = 13
fib_sequence = fibonacci(num_terms)
print(fib_sequence)
