import time

def timer(fucn) :
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fucn(*args, **kwargs)
        end = time.time()
        print(f'time elapsed : {end - start}')
        return result
    return wrapper

def factorial(number) -> int:
    """
    팩토리얼 함수 생성
    :param number:
    :return: factorial 결과 반환
    """
    if number <=1 :
        return number
    return number * factorial(number-1)

def factorial_with_for(number) -> int:
    total = 1
    for i in range(1,number+1):
        total *= i

    return total
@timer
def nCr(n,r) -> int:
    """
    combination 함수 생성
    :param n:
    :param r:
    :return: 경우의 수
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator / denominator