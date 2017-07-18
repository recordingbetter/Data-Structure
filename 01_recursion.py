def factorial(n):
    # 탈출조건
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    n = 4
    result = factorial(n)
    print("The factorial of {} is {}".format(n, result))
