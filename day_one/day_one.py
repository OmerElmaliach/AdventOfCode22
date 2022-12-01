
def main():
    print(part_two())


def part_one():
    with open('22D1.txt', 'r') as file:
        lst = file.read().splitlines()
        max_cal, current_cal = 0, 0
        for i in lst:
            if len(i) > 0:
                current_cal += int(i)
            else:
                max_cal = max(max_cal, current_cal)
                current_cal = 0

    return max_cal


def part_two():
    with open('22D1.txt', 'r') as file:
        lst = sorted(sort_list_per_cal(file.read().splitlines()))
        return lst[-1] + lst[-2] + lst[-3]


def sort_list_per_cal(lst):
    new_lst, current_cal = [], 0
    for i in lst:
        if len(i) > 0:
            current_cal += int(i)
        else:
            new_lst.append(current_cal)
            current_cal = 0

    return new_lst


if __name__ == "__main__":
    main()
