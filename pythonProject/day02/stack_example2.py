f = open("진달래꽃.txt", "r", encoding='UTF-8')

lst = []
while True:
    line = f.readline().strip()
    if not line: break
    lst.append(line)

for i in range(len(lst)-1,-1,-1):
    for j in range(len(lst[i])-1,-1,-1):
        print(lst[i][j], end='')
    print()

