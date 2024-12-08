# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group,participants_second_group, a=','):
    one_participants_first_group= set(participants_first_group.split(a))
    two_participants_second_group= set(participants_second_group.split(a))

    common_participants = one_participants_first_group & two_participants_second_group
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group,participants_second_group)
print(common_participants)
