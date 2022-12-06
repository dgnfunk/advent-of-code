def day1_solution():
    count = 0
    elfs = []

    with open('input.txt', 'r') as f:
        calories = []

        for line in f:
            if line.isspace():
                count += 1
                elfs.append(sum(calories))
                calories = []
            else:
                calories.append(int(line))

        elfs.sort(reverse=True)
        print(sum(elfs[0:3]))


if __name__ == '__main__':
    day1_solution()