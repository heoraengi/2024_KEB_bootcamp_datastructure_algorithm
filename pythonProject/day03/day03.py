def fibo_recursion(number: int) -> int:
    '''
    fibonacci function by recursion
    :param number: integer number
    :return: integer number
    '''

    if number ==0:
        return 0
    elif number == 1:
        return 1
    else :
        return fibo_recursion(number-1) + fibo_recursion(number-2)

def fibo_repetition(number: int) -> int:
    '''
    fibonacci function by repetition
    :param number: integer number
    :return: integer number
    '''

    x, y = 0 , 1
    for i in range(number):
        x, y = y , x+y

    return y


for i in range(2,20):
    print(fibo_repetition(i), end=' ')