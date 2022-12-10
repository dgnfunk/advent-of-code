from os.path import dirname, join
import string

# Given a set of supplies on rucksacks
# each supply has a type
# each rucksack contain tu compartiments
# each line represent a rucksack
# compartiments split in two the rucksack
# each type has a priority
#   a to z is 1 to 26
#   A to Z is 27 to 52
def get_type_value(type):
    alphabet_values = list(string.ascii_letters)
    index = alphabet_values.index(type)
    return index + 1

def day3_solution():
    rucksacks = []
    elves_groups = []

    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, 'r') as f:
        count = 0
        group = []

        for line in f:
            count += 1
            items = line.rstrip()
            lenght_items = len(items)
            list_items = list(items)
            group.append(set(list_items))

            if count == 3:
                elves_groups.append(group)
                count = 0
                group = []

            half_len = int(lenght_items / 2)
            first_half = set(list_items[0:half_len])
            second_half = set(list_items[half_len:lenght_items])

            # interesaction between two compartiments 
            same_type = first_half & second_half
            type = same_type.pop()
            same_type_value = get_type_value(type)
            rucksacks.append(same_type_value)
            # print('Elves groups:', elves_groups)
        
        groups_priority = []
        for group in elves_groups:
            badge = set.intersection(*group)
            badge_type = badge.pop()
            groups_priority.append(get_type_value(badge_type))
            # print('Badge type', )
        print('Groups priority', sum(groups_priority))
        print('Rucksacks', sum(rucksacks))



if __name__ == '__main__':
    day3_solution()