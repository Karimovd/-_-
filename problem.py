s = input()   #ввод имени файла
p = input()   #действие которое нужно совершить
with open(s, "r") as my_file: #открываем файл
    content = my_file.read()
content = content.split()
p = p.split() #переменная получила значение файла, но в форме строки. Мы переводим строку в список
if p[0] == 'Добавить': # Если р имеет значение например: Добавить в список Виноград - 200
    content += p[3:]
if p[0] == 'Изменить':  # Если р имеет значение например: Изменить запись в списке Огурцы - 50 на Виноград - 200
    t = p[4]
    r = content.index(t)
    content[r] = p[8]
    content[r + 2] = p[10]
if p[0] == "Удалить":  # Если р имеет значение например: Удалить из списка Масло - 40
    t = p[3]
    r = content.index(t)
    a = content.pop(r)
    a = content.pop(r)
    a = content.pop(r)
y = 0 
if p[0] == 'Вычесть':  # Если р имеет значение например: Вычесть общую сумму
    for i in range(2, len(content), 3):
        y += int(content[i])
content = ' '.join(content)
if y != 0: # проверка, если нам надо было вычитать, то выводим сумму
    b = 'Общая сумма = '
    with open(s, "w") as my_file:
        my_file.write(content + '\n')
        my_file.write(b + str(y))
else: # иначе выполняем 1 из 3 других предписанных действий
    with open(s, "w") as my_file:
        my_file.write(content)
 # файл изменен, проверьте файл
