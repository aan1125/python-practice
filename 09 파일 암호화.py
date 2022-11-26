
of = open('./text/메모.txt', 'r', encoding='UTF-8')
ef = open('./text/암호화.txt', 'w', encoding='UTF-8')
os = of.read()
es=''
for oc in os:
    ec = chr( ord(oc) + 100 )
    es = es + ec

ef.write(es)

of.close()
ef.close()

print('--- 메모.txt 파일 암호화 완료. ---')
