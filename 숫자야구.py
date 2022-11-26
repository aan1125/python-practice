import random
print('숫자 야구게임!!!')
print('게임을 시작합니다.')
print()

while True:

    num=list(range(1,10))
    r_num=random.sample(num,3)
    print(r_num)

    print()
    print('랜덤으로 숫자가 생성되었습니다.')
    print('각 자리의 숫자는 서로 중복되지 않습니다.')
    print()

    print('10 번 안에 맞춰주세요.')
    print('세 자리 숫자를 입력하세요.')
    print()

    for n in range(1,11):

        while True:
            g_num=input(str(n)+'번째 시도:')
            if g_num.isdigit() and (99 < int(g_num)<1000):
                break 
            print('잘못 입력하셨습니다.')
            print()
            
        g_num=list(input(str(n)+'번째 시도:'))

        s=0
        b=0
        o=0
        for i in range(3):
            if int(g_num[i])==r_num[i]:
                s=s+1
            elif int(g_num[i]) in r_num:
                b=b+1
            else:
                o=o+1
        print(s,'스트라이크,',b,'볼,',o,'아웃')

        if s==3:break
    r_num=''.join(map(str,r_num))

    if s==3:
        print(r_num,'맞았습니다.')
    elif n==10:
        print('10번의 시도를 다 하셨습니다.')
        print('숫자는',r_num,'입니다.')

    print()
    ctn=input('게임을 다시 할까요?(y/n):')

    if ctn=='n':
        print('게임을 종료합니다.')
        break
