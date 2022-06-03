
with open('5차소분류.txt','r',encoding='utf-8') as f:
    f_lines = f.readlines()
    with open('5차소분류(완료).txt','w',encoding='utf-8') as f2:
        for i in f_lines:
            f2.write(i)
            f2.write(i)
            f2.write(i)

'''
with open('5차상황_원어.txt','r',encoding='utf-8') as f:
    f_lines = f.readlines()
    with open('5차상황_원어(완료).txt','w',encoding='utf-8') as f2:
        for i in f_lines:
            f2.write('('+i+')'+'\n')
            f2.write('('+i+')'+'\n')
            f2.write('('+i+')'+'\n')
'''