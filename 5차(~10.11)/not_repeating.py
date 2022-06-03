with open('3번반복.txt','r',encoding='utf-8') as f:
    f_lines = f.readlines()
    with open('1번반복.txt','w',encoding='utf-8') as f2:
        new_list = []
        for v in f_lines:
            if v not in new_list:
                new_list.append(v)
                f2.write(v)