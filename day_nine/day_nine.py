from math import sqrt


def main():
    with open('22D9.txt', 'r') as file:
        data = file.read().split()
        print(count_unique_lists(count_tail_positions(data)))


def count_tail_positions(data):
    head, loc_list = [0, 0], [[0, 0]]
    for direction, times in zip(data[::2], data[1::2]):
        if direction == 'U':
            for i in range(int(times)):
                head[1] += 1
                if not is_in_range(head, loc_list[-1]):
                    loc_list.append([head[0], head[1] - 1])
        elif direction == 'D':
            for i in range(int(times)):
                head[1] -= 1
                if not is_in_range(head, loc_list[-1]):
                    loc_list.append([head[0], head[1] + 1])
        elif direction == 'L':
            for i in range(int(times)):
                head[0] -= 1
                if not is_in_range(head, loc_list[-1]):
                    loc_list.append([head[0] + 1, head[1]])
        elif direction == 'R':
            for i in range(int(times)):
                head[0] += 1
                if not is_in_range(head, loc_list[-1]):
                    loc_list.append([head[0] - 1, head[1]])

    return loc_list


def is_in_range(pos1, pos2):
    """
    Return if tail is in range of head
    :param pos1: Head location
    :param pos2: Tail location
    :return: True if in range, false if not
    """
    return sqrt((pow(pos1[0] - pos2[0], 2)) + pow(pos1[1] - pos2[1], 2)) < 1.5


def count_unique_lists(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])

    return len(new_lst)


if __name__ == '__main__':
    main()
