file = open('steam (1).csv', 'r', encoding='utf-8')
mainList = []
counter = 2
headers0 = file.readline().split(',')
headers = headers0[2::]
lines = file.readlines()
for line in lines:
    splitedStr = line.split(',')
    splitedElems = []
    for elem in splitedStr:
        splitedElems.append(elem.split(';'))
    mainList.append(splitedElems)
for colomnName in headers:
    fileteredList = []
    print('Введите ', colomnName)
    insertParams = input().split(',')
    for param in mainList:
        if bool(set(param[counter]) & set(insertParams)) or insertParams[0] == '':
            fileteredList.append(param)
    counter += 1
    mainList = fileteredList
file.close()

results = open('result', 'w', encoding='utf-8')
for param in mainList:
    counter = 0
    results.write('Вам подходит игра: \n')
    for elem in headers0:
        results.write(elem+' : ')
        for m in param[counter]:
            results.write(m+' ')
        results.write('\n')
        counter += 1
results.close()
