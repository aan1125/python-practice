f=open('./text/read.txt','r',encoding='UTF-8')

while True:
    line=f.readline()

    if line =='' :break

    print(line,end='')
    
f.close()
       
