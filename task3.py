def dora(stuff, weight):
    result = []
    temp_size = 0
    temp_lst = []
    thing, size = zip(*sorted(stuff.items(), key=lambda x: x[1], reverse=True))
    for number, s in enumerate(size, 0):
        temp_size += s
        temp_lst.append((thing[number]))
        for number_n, sn in enumerate(size[number:], number):
            if sn + temp_size <= weight:
                temp_size += sn
                temp_lst.append(thing[number_n])
        result.append(temp_lst)
        temp_lst = []
        temp_size = 0
    return result


our_stuff = {"палатка": 5, "белье": 1, "колонка": 2, "еда": 4, "вода": 3, "аптечка": 2, "посуда": 1}
backpack_max = int(input("Введите обьем рюкзака: "))
[print(things) for things in dora(our_stuff, backpack_max)]
