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

# memo = [0 if i==0 else 1 if i==1 else None for i in range(100)]
memo = [0,1] + [None] * (100-1)

n = int(input('Input number : '))
print(f'fibonacci({n}) : {fibo_monoization(n)}')
