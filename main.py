from tables import input_text, key
from def_table import start, end
from L_R_work import L_R_work

# !!! ВХОДНЫЕ ДАННЫЕ ВСТАВИТЬ В TABLES.PY, ВЫХОДНЫЕ ДАННЫЕ БУДУТ В ФАЙЛЕ ТАМ ГДЕ ЛЕЖИТ ПРОГРАММА

file = open('output.txt', 'w')
file.write('Входной текст:\n' + input_text + '\n\n\n')
file.write('Ключ:\n' + key + '\n\n\n')
# делим входной текст на блоки по 64
amended_input = (64 - len(input_text) % 64) * '0' + input_text
input_in_parts = [amended_input[x:x + 64] for x in range(0, len(amended_input), 64)]
file.write('Текст поделенный на блоки:\n' + str(input_in_parts) + '\n\n\n')
# делаем начальные перестановки
after_start = [start(i) for i in input_in_parts]
file.write('Блоки после начальных перестановок:\n' + str(after_start) + '\n\n\n')
# делим на L и R и склеиваем обратно
after_lr = []
for block in after_start:
    l = block[:32]
    r = block[32:]
    file.write('L_R работа с блоком ' + str(len(after_lr) + 1) + '\n')
    after_lr.append(L_R_work(l, r, file))
# конечная перестановка
after_end = [end(i) for i in after_lr]
file.write('После конечной перестановки:\n' + str(after_end) + '\n\n\n')
file.write('Ответ:\n' + ''.join(after_end))
file.close()
