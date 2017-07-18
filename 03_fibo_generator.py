def fibo_gen(n):
    a = b = 1
    # generator 사용
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    f = fibo_gen(10)
    for i in range(10):
        print(next(f), end="    ")
