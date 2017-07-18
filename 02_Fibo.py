def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n - 2) + fibo(n - 1)


if __name__ == "__main__":
    n = 10
    for i in range(n):
        print(fibo(i), end='    ')
