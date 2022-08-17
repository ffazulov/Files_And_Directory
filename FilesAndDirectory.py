import os

def qq(path,n, level=1):
    tab = '|---' * level
    print(tab+n)
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            n = i
            qq(path+'\\'+i, n, level+1)
        else:
            tab = '|---' * (level+1)
            print(tab+i)

def q(path,list_name = [], level=1):
    list_name.append(os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            q(path+'\\'+i,list_name, level+1)
    return list_name

test = 'test'
path_global = 'C:\\Users\\Acer\\Desktop\\'
path = input('В какую папку полезем?)')
path = path_global + path
qq(path, test)
x = q(path)

dir_name ={}
for i in range(len(x)):
    for j in range(len(x[i])):
        if len(x[i][j].split('.')) != 1:
            if x[i][j].split('.')[-1] in dir_name:
                dir_name[x[i][j].split('.')[-1]] += 1
            else:
                dir_name[x[i][j].split('.')[1]] = 1
        else:
            if 'папка' in dir_name:
                dir_name['папка'] += 1
            else:
                dir_name['папка'] = 2

for i, k in dir_name.items():
    print(f'файлов с раширением \'{i}\': {k} штук')