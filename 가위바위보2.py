import random

print('가위/바위/보 중 하나를 입력하세요.')
사용자 = input('1.가위 / 2.바위 / 3.보 : ')

if(사용자 == '가위' or 사용자 == '바위' or 사용자 == '보') :
    컴퓨터 = random.choice(['가위','바위','보'])
    print('컴퓨터:',컴퓨터)

    if 사용자 == 컴퓨터:
        print('비겼습니다.')
    elif (사용자 == '가위' and 컴퓨터 == '보') :
            print('이겼습니다.')
    elif (사용자 == '가위' and 컴퓨터 == '보') :
            print('이겼습니다.')
    elif (사용자 == '가위' and 컴퓨터 == '보') :
            print('이겼습니다.')
    else:
        print('졌습니다.')
else:
    print('잘못 입력하셨습니다.')
