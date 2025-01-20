# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, rasdelitel = ','):
    part1 = set(group1.split(rasdelitel))
    part2 = set(group2.split(rasdelitel))

    dwa_rasa = part1.intersection(part2)
    sorted(dwa_rasa)

    return dwa_rasa

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

dwa_rasa = find_common_participants(participants_first_group, participants_second_group, rasdelitel='|')

print(dwa_rasa)
