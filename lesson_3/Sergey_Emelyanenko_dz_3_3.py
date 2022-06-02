# Домашнеее задание, урок-3, задание-3

names = ['Иван', 'Мария', 'Петр', 'Илья']
def thesaurus():
    Dt_i = dict()
    Dt_lit = dict()
    for n in names:
        l_1 = n[0]
        Dt_lit[l_1] = Dt_lit.setdefault(l_1, []) + [n]
    print(Dt_i, Dt_lit)
thesaurus()
