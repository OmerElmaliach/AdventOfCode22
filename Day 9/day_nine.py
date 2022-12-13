from math import sqrt


def main():
    with open('22D9.txt', 'r') as file:
        data = file.read().split()
        rope = setup_rope(10)
        print(count_tail_pos(data, rope))


def setup_rope(num):
    rope = []
    for i in range(num):
        rope.append([0, 0])

    return rope


def count_tail_pos(data, rope):
    loc_lst = []
    for direction, times in zip(data[::2], data[1::2]):
        tail_pos = move_rope(rope, direction, times)
        for loc in tail_pos:
            if loc not in loc_lst:
                loc_lst.append(loc)

    return len(loc_lst)


def move_rope(rope, direction, times):
    tail_pos, current_pos, prev_head_pos = [0, 0], [0, 0], [0, 0]
    for i in range(int(times)):
        tail_pos.append(rope[-1].copy())
        for k in range(len(rope)):
            if k == 0:
                prev_head_pos = rope[0].copy()
                if direction == 'U':
                    rope[0][1] += 1
                elif direction == 'D':
                    rope[0][1] -= 1
                elif direction == 'L':
                    rope[0][0] -= 1
                elif direction == 'R':
                    rope[0][0] += 1

            elif not is_in_range(rope[k - 1], rope[k]):
                current_pos = rope[k]
                rope[k] = prev_head_pos
                prev_head_pos = current_pos

    return tail_pos


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
