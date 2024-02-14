queue = ['정국','뷔','지민','진', '슈가']
front = -1
rear = 4
while True:
    print('대기 줄 상태 : ', queue)
    front += 1
    if queue[front] == None :
        print(f'식당 영업 종료')
        break
    else :
        print(f'{queue[front]} 님 식당에 들어감')
        queue[front] = None
        for j in range(front+1, rear+1):
            queue[j-1] = queue[j]
            queue[j] = None
        rear -=1
        front = -1
