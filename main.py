file = open('steam (1).csv', encoding='utf-8')
main_list = []
column = 2
full_headers = file.readline().split(',')
headers = full_headers[2:]
lines = file.readlines()
for line in lines:
    splited_str = line.split(',')
    splited_elems = []
    for elem in splited_str:
        splited_elems.append(elem.split(';'))
    main_list.append(splited_elems)
for column_name in headers:
    filetered_list = []
    print('Введите ', column_name)
    insert_params = input().split(',')
    for param in main_list:
        if bool(set(param[column]) & set(insert_params)) or insert_params[0] == '':
            filetered_list.append(param)
    column += 1
    main_list = filetered_list
file.close()

results = open('result', 'w', encoding='utf-8')
for param in main_list:
    column = 0
    results.write('Вам подходит игра: \n')
    for elem in full_headers:
        results.write(elem + ' : ')
        for m in param[column]:
            results.write(m + ' ')
        results.write('\n')
        column += 1
results.close()
