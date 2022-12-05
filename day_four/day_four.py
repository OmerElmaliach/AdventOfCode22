

def main():
    print(part_two())


def part_one():
    count = 0
    with open('22D4.txt', 'r') as file:
        data = file.read().splitlines()
        for item in data:
            sections = item.split(',')
            first_sec, second_sec = sections[0], sections[1]
            lst_nums = [int(i) for i in first_sec.split('-') + second_sec.split('-')]
            if (lst_nums[2] <= lst_nums[0] <= lst_nums[3] and lst_nums[2] <= lst_nums[1] <= lst_nums[3]) \
                    or (lst_nums[0] <= lst_nums[2] <= lst_nums[1] and lst_nums[0] <= lst_nums[3] <= lst_nums[1]):
                count += 1

    return count


def part_two():
    count = 0
    with open('22D4.txt', 'r') as file:
        data = file.read().splitlines()
        for item in data:
            sections = item.split(',')
            first_sec, second_sec = sections[0], sections[1]
            lst_nums = [int(i) for i in first_sec.split('-') + second_sec.split('-')]
            if (lst_nums[2] <= lst_nums[0] <= lst_nums[3] or lst_nums[2] <= lst_nums[1] <= lst_nums[3]) \
                    or (lst_nums[0] <= lst_nums[2] <= lst_nums[1] or lst_nums[0] <= lst_nums[3] <= lst_nums[1]):
                count += 1

    return count


if __name__ == '__main__':
    main()
