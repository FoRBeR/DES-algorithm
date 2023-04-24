from def_table import exp, sub
from tables import key


def L_R_work(l, r, file):
    file.write('L: ' + l + '\n')
    file.write('R: ' + r + '\n')
    # расширение R
    exp_r = exp(r)
    file.write('Расширенный R: ' + exp_r + '\n')
    # поразрядное суммирование с ключом
    f = ''
    for j in range(48):
        f += str((int(exp_r[j]) + int(key[j])) % 2)
    file.write('F: ' + f + '\n')
    # используем таблицу подстановки
    exit_f = sub(f)
    file.write('F после таблицы подстановки: ' + exit_f + '\n')
    # поразрядное суммирование с L
    exit_r = ''
    for j in range(32):
        exit_r += str((int(exit_f[j]) + int(l[j])) % 2)
    file.write('После суммирования с L: ' + exit_r + '\n')
    # соединение в блок
    s = r + exit_r
    file.write('R + полученное: ' + s + '\n\n\n')
    return s
