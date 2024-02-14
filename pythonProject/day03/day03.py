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

    return x



def fibo_monoization(number) -> int :
    '''
    fibonacci function by recursion with monoization
    :param number: integer number
    :return: integer number
    '''
    global memo
    if memo[number] is not None :
        return memo[number]
    if number < 2 :
        result = number
    else :
        result = fibo_monoization(number-1) + fibo_monoization(number-2)
        memo[number] = result
    return result

memo = [None] * 100
for i in range(2,10):
    print(fibo_monoization(i), end=' ')
