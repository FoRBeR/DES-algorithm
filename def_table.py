from tables import subtable, start_table, end_table, exp_table


def sub(f):
    f1 = [f[x:x + 6] for x in range(0, len(f), 6)]
    f2 = []
    for i in f1:
        v1 = int(i[0] + i[5], 2)
        v2 = int(i[1:5], 2)
        f2.append(bin(subtable[v1][v2] + 16)[3:])
    return ''.join(f2)


def start(s):
    s_new = [s[i - 1] for i in start_table]
    return ''.join(s_new)


def end(s):
    s_new = [s[i - 1] for i in end_table]
    return ''.join(s_new)


def exp(r):
    r_new = [r[i - 1] for i in exp_table]
    return ''.join(r_new)


