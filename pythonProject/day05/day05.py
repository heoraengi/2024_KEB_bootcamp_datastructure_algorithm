def fibo_memo(n):
    global memo, cnt_memo

    if memo[n] is not None:
        return memo[n]
    if n < 2 :
        result = n
    else :
        cnt_memo += 1
        result = fibo_memo(n-1) + fibo_memo(n-2)
        memo[n] = result
    return result

def fibo(n) :
    global cnt
    cnt +=1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

cnt_memo = 0
cnt = 0
memo = [None] * 100
memo[0] = 0
memo[1] = 1

print(fibo(30))
print(fibo_memo(30))
print(cnt)
print(cnt_memo)