

def main():
    print(part_two())


def part_one():
    lst_crates = filter_crates()
    with open('22D5.txt', 'r') as file:
        for data in file.readlines():
            if 'move' in data:
                cmds = [int(i) for i in data.split() if i.isdigit()]
                for i in range(cmds[0]):
                    lst_crates[cmds[2] - 1].insert(0, lst_crates[cmds[1] - 1].pop(0))

    return return_sequence(lst_crates)


def part_two():
    lst_crates = filter_crates()
    with open('22D5.txt', 'r') as file:
        for data in file.readlines():
            if 'move' in data:
                cmds = [int(i) for i in data.split() if i.isdigit()]
                for i in range(cmds[0], 0, -1):
                    lst_crates[cmds[2] - 1].insert(0, lst_crates[cmds[1] - 1].pop(i - 1))

    return return_sequence(lst_crates)


def return_sequence(dict_lst):
    sequence = ""
    for i in range(len(dict_lst.keys())):
        sequence += dict_lst[i][0][1]
    return sequence


def filter_crates():
    """
    :return: Dictionary containing each crate, first item in list is the top crate in each stack
    """
    lst_crates = {}
    with open('22D5.txt', 'r') as file:
        for data in file.readlines():
            for i in range(0, len(data), 4):
                if '[' in data[i:i + 3]:
                    if int(i / 4) in lst_crates.keys():
                        lst_crates[int(i / 4)].append(data[i:i + 3])
                    else:
                        lst_crates[int(i / 4)] = [data[i:i + 3]]

    return lst_crates


if __name__ == '__main__':
    main()
