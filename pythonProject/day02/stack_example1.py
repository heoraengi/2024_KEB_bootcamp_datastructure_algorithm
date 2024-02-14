stack = ['우리집']
top = 0

top += 1
stack.append('주황')
top += 1
stack.append('초록')
top += 1
stack.append('파랑')
top += 1
stack.append('보라')
top += 1
stack.append('빨강')
top += 1
stack.append('노랑')
top += 1
stack.append('과자집')
print('과자집에 가는 길 : ', end='')
for i in range(1,len(stack)):
    if i == len(stack)-1:
        print(f'{stack[i]}')
    else:
        print(f'{stack[i]}-->',end='')

print('우리집에 오는 길 : ', end='')
while top > -1 :
    p = stack.pop()
    if p == '과자집':
        pass
    elif top==0:
        print(f'{p}')
    else:
        print(f'{p}-->',end='')
    top -= 1
