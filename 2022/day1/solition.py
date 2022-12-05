def day1_solution():
    count = 0
    elfs = {}

    with open('input.txt', 'r') as f:
        calories = []
        big_in_calories = None

        for line in f:
            if line.isspace():
                count += 1
                elfs[count] = sum(calories)

                if len(elfs) == 1:
                    big_in_calories_elf = count
                else:
                    if elfs[count] > elfs[big_in_calories_elf]:
                        big_in_calories_elf = count

                calories = []
            else:
                calories.append(int(line))

        print('Big in calories elf', big_in_calories_elf, 'with', elfs[big_in_calories_elf])



if __name__ == '__main__':
    day1_solution()