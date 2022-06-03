with open("5차상황_단어.txt",'r',encoding='utf-8') as f1:
    with open("중복확인용.txt",'r',encoding='utf-8') as f2:
        f1_line = f1.readlines()
        f2_line = f2.readlines()
        f1_list = [line.rstrip() for line in f1_line]
        f2_list = [line.rstrip() for line in f2_line]
        #print(f1_list)
        #print(f2_list)
        for i in f1_list:
            for j in f2_list:
                if i == j:
                    print(i)
