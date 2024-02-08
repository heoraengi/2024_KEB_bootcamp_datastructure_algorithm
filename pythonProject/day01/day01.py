def factorial(number) -> int:
    if number <=1 :
        return number
    return number * factorial(number-1)

def nCr(n,r) -> int:
    """
    조합 함수 생성
    :param n:
    :param r:
    :return: 경우의 수
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator / denominator

if __name__ == "__main__":
    n = int(input("Input n : "))
    r = int(input("Input r : "))

    print(f'{n}C{r} = {nCr(n,r)}')
