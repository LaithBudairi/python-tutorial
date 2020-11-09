i = 5

for x in range(0, i, 2):
    print(x)


def find_sum(my_list):
    _sum = 0
    for x in my_list:
        _sum += x
    return _sum


def find_average(my_list):
    return find_sum(my_list) / len(my_list)


my_list = [1, 2, 3, 4, 5]

print_stm = "Average is: {}"

print(print_stm.format(find_average(my_list)))

#############################################

