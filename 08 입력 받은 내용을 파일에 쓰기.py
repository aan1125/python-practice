
f = open('./text/메모.txt', 'w', encoding='UTF-8' )
while True:
    line = input('내용 입력:')

    if line =='':break
    
    f.write(line + '\n')
    
f.close()


print('--- 메모.txt 파일에 내용이 저장되었습니다. ---')
