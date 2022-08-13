from collections import Counter


with open('1.txt', encoding='utf-8') as f1:
    file1 = f1.readlines()
    f1.seek(0)
    text1 = f1.read()
with open('2.txt', encoding='utf-8') as f2:
    file2 = f2.readlines()
    f2.seek(0)
    text2 = f2.read()
with open('3.txt', encoding='utf-8') as f3:
    file3 = f3.readlines()
    f3.seek(0)
    text3 = f3.read()

count1 = Counter()
count2 = Counter()
count3 = Counter()


text_list = {
    1: text1,
    2: text2,
    3: text3
}
# Считаем кол-во строк в йале по кол-ву спец. символов
for i in file1:
    count1['\n'] += 1
for i in file2:
    count2['\n'] += 1
for i in file3:
    count3['\n'] += 1

# Создаем словарь с именем файлов и кол-вом строк в нем
count_string = {}
count_string['1.txt'] = count1['\n']
count_string['2.txt'] = count2['\n']
count_string['3.txt'] = count3['\n']

# Сортируем словарь по значениям и перезаписываем словарь
sorted_tuple = sorted(count_string.items(), key=lambda x: x[1])
count_string = dict(sorted_tuple)

# Запускать только 1 раз, т.к. по заданию необходимо лишь записать файл с определенной структурой
with open('new file.txt.', mode='a+', encoding='utf-8') as f:

    for key, value in count_string.items():
        f.write(key + '\n')
        f.write(str(value) + '\n')

    for key in count_string.keys():
        f.write(text_list[int(key.strip('.txt'))] + '\n')
        f.seek(0)
    print(f.read())
