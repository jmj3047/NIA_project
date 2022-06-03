with open('4차검수문장.txt','r',encoding='utf-8') as c:
    c_lines = c.readlines()
    for i in c_lines:
        if len(i) <= 14:
            print(i)