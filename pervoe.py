import datetime

now = datetime.datetime.now()

print("Введите скобки:")
stroka = str(input())
st = list(stroka)
if (len(st) == 0):
    print("Таких скобок нет!")
elif (len(st) == 1):
    print("Эта скобка под индексом [0]")
elif (st[0] == ')'):
    print("Эта скобка под индексом [0]")
else:
    k = 0
    n = len(st)
    for j in range(1, n, 2):
        for i in range(n):
            if (i + j < n):
                if (st[i] == '(' and st[i + j] == ')'):
                    st[i] = 0
                    st[i + j] = 0
    for i in range(n):
        if (st[i] != 0):
            print("Эта скобка под индексом [", i, "]")
            break
        else:
            k += 1
    if k == n:
        print("У всех скобок есть пара, одиночных скобок не было обнаружено программой в ходе ее выполнения на паре введения в инФормационные технологии в кабинете №5 на кафедре системного анализа и информационных технологий (САИиТ) в федеральном государственном бюджетном образовательном учреждении высшего образования (Санкт-Петербургский государственный технологический институт (технический университет)) (техноложка, станция метро Технологический институт)",
            now.day, 'числа,', now.month, 'месяца,', now.year, 'года в', now.hour, 'часов,', now.minute, 'минут,',
            now.second, 'секунд!')


