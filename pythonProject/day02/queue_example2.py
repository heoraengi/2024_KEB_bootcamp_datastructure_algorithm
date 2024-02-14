def add_waiting_time (func) :
    def warpper(*args, **kwargs):
        global waiting_time,queue,rear
        result = func(*args, **kwargs)
        _, time = queue[rear]
        waiting_time += time
        return result
    return warpper

def print_waiting (func) :
    def warpper(*args, **kwargs):
        global waiting_time
        result = func(*args, **kwargs)
        print()
        if rear == 5 :
            print('최종 대기 콜 --> ', queue)
            print('프로그램 종료!')
        else :
            print(f'귀하의 대기 예상시간은 {waiting_time}분 입니다.')
            print('현재 대기 콜 --> ', queue)
        return result
    return warpper

@print_waiting
@add_waiting_time
def insert_queue (menu, time):
    global rear, queue
    rear +=1
    queue[rear] = (menu,time)

queue = [None,None,None,None,None,None]
front = 0
rear = 0
waiting_time = 0

print(f'귀하의 대기 예상시간은 {waiting_time}분 입니다.')
print('현재 대기 콜 --> ', queue)
insert_queue('사용',9)
insert_queue('고장',3)
insert_queue('환불',4)
insert_queue('환불',4)
insert_queue('고장',3)


