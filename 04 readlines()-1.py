f=open('./text/read.txt','r',encoding='UTF-8')


lines=f.readlines()

for i in range(len(lines)): 
    print(lines[i],end='')
    
f.close()
         
