li=[]

while True:
    num = int(input('숫자를 입력해 주세욧! : '))
    if 0 < num < 100:
        li.append(num)
    elif num < 0:
        print('1이상 숫자를 입력하세욧!')
    else:
        break

li.sort()
min = li[0]
max = li[-1]
print(min+max)