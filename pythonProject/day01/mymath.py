def factorial(number) -> int:
    """
    팩토리얼 함수 생성
    :param number:
    :return: factorial 결과 반환
    """
    if number <=1 :
        return number
    return number * factorial(number-1)

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