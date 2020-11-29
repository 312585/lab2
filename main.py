file = open('steam (1).csv', encoding='utf-8')
MainList = []
column = 2
FullHeaders = file.readline().split(',')
headers = FullHeaders[2:]
lines = file.readlines()
for line in lines:
    SplitedStr = line.split(',')
    SplitedElems = []
    for elem in SplitedStr:
        SplitedElems.append(elem.split(';'))
    MainList.append(SplitedElems)
for ColumnName in headers:
    FileteredList = []
    print('Введите ', ColumnName)
    InsertParams = input().split(',')
    for param in MainList:
        if bool(set(param[column]) & set(InsertParams)) or InsertParams[0] == '':
            FileteredList.append(param)
    column += 1
    MainList = FileteredList
file.close()

results = open('result', 'w', encoding='utf-8')
for param in MainList:
    column = 0
    results.write('Вам подходит игра: \n')
    for elem in FullHeaders:
        results.write(elem + ' : ')
        for m in param[column]:
            results.write(m + ' ')
        results.write('\n')
        column += 1
results.close()
