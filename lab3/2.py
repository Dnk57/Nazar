# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group1,group2,sep=','):
    group1 = set(group1.split(sep))
    group2 = group2.split(sep)
    find = group1.intersection(group2)
    return list(find)

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,'|'))