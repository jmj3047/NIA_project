with open("4차_원어(상황)_완료.txt",'w',encoding='utf-8') as f1:
    with open("4차_원어(상황).txt",'r',encoding='utf-8') as f2:
        f2_line = f2.readlines()
        #print(f2_line)
        for i in f2_line:
            #i.split("\n")
            #print(i)
            f1.write(i)
            f1.write(i)
            f1.write(i)
            
with open("4차_한국어(상황)_완료.txt",'w',encoding='utf-8') as f1:
    with open("4차_한국어(상황).txt",'r',encoding='utf-8') as f2:
        f2_line = f2.readlines()
        #print(f2_line)
        for i in f2_line:
            #i.split("\n")
            #print(i)
            f1.write(i)
            f1.write(i)
            f1.write(i)

with open("4차_단어(상황)_완료.txt",'w',encoding='utf-8') as f3:
    with open("4차_한국어(상황)_완료.txt",'r',encoding='utf-8') as f1:
        with open("4차_원어(상황)_완료.txt",'r',encoding='utf-8') as f2:
            f1_line = f1.readlines()
            f2_line = f2.readlines()
            f1_list = [line.rstrip() for line in f1_line]
            f2_list = [line.rstrip() for line in f2_line]
            for i in f2_list:
                #f3.write(i+'('+'\n')
                f3.write(i+')'+'\n')
