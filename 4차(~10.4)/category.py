import re
with open("4차_소분류_완료.txt",'w',encoding='utf-8') as f1:
    with open("4차_소분류.txt",'r',encoding='utf-8') as f2:
        f2_line = f2.readlines()
        #print(f2_line)
        print(len(f2_line))
        for i in f2_line:
            #i.split("\n")
            #print(i)
            f1.write(i)
            f1.write(i)
            f1.write(i)
'''
with open("set_number_fin.txt",'w',encoding='utf-8') as f1:
    with open("set_number.txt",'r',encoding='utf-8') as f2:
        f2_line = f2.readlines()
        #print(f2_line)
        for i in f2_line:
            #i.split("\n")
            #print(i)
            f1.write(i)
            f1.write(i)
            f1.write(i)


with open("발화자.txt",'w',encoding='utf-8') as f1:
    for i in range(100):
        f1.write('A-1\n')
        f1.write('A-2\n')
        f1.write('A-3\n')

'''