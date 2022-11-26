import random

print('가위/바위/보 중 하나를 숫자로 입력하세요.')
사용자 = input('1.가위 / 2.바위 / 3.보 : ')
컴퓨터 = random.randint(1,3)

if 사용자 == '1': #가위
    if 컴퓨터 == 1:
        print('비겼습니다.')
    elif 컴퓨터 == 2:
        print('졌습니다.')
    elif 컴퓨터 == 3:
        print('이겼습니다.')
if 사용자 == '2': #바위
    if 컴퓨터 == 1:
        print('이겼습니다.')
    elif 컴퓨터 == 2:
        print('비겼습니다.')
    elif 컴퓨터 == 3:
        print('졌습니다.')
if 사용자 == '3': #보
    if 컴퓨터 == 1:
        print('졌습니다.')
    elif 컴퓨터 == 2:
        print('이겼습니다.')
    elif 컴퓨터 == 3:
        print('비겼습니다.')
else:
    print('잘못 입력하셨습니다.')


       
                
