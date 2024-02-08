import random

if __name__ == "__main__":
    cnt = 1
    random_number = random.randint(1,100)

    while True:
        number = int(input("1-100 사이의 숫자를 입력하세요. : "))
        if random_number == number :
            print('정답입니다')
            print('정답을 맞추기 위해서 걸린 횟수 : ', cnt)
            break

        elif random_number > number:
            print('더 큰 수입니다~')

        elif random_number < number:
            print('더 작은 수입니다~')

        cnt+=1