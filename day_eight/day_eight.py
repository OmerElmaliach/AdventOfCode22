

def main():
    with open('22D8.txt', 'r') as file:
        data = file.read().split()
        print(find_visible_trees(sort_data(data)))  # Solution for part one
        print(highest_scenic_view(data))  # Solution for part two


def find_visible_trees(data):
    vis_trees = 0
    for line in range(len(data)):
        for column in range(len(data[0])):
            if line == 0 or line == len(data) - 1 or column == 0 or column == len(data[0]) - 1\
                    or is_visible(data, line, column):
                vis_trees += 1

    return vis_trees


def is_visible(data, line, column):
    up, down, left, right = True, True, True, True
    # Upwards
    for i in range(line):
        if data[i][column] >= data[line][column]:
            up = False

    # Downwards
    for i in range(line + 1, len(data)):
        if data[i][column] >= data[line][column]:
            down = False

    # Left
    for i in range(column):
        if data[line][i] >= data[line][column]:
            left = False

    # Right
    for i in range(column + 1, len(data[0])):
        if data[line][i] >= data[line][column]:
            right = False

    return up or down or left or right


def highest_scenic_view(data):
    highest_view = 0
    for line in range(len(data)):
        for column in range(len(data[0])):
            highest_view = max(highest_view, return_tree_view(data, line, column))

    return highest_view


def return_tree_view(data, line, column):
    up, down, left, right = 0, 0, 0, 0
    # Upwards
    for i in range(line - 1, -1, -1):
        if data[i][column] >= data[line][column]:
            up += 1
            break
        up += 1

    # Downwards
    for i in range(line + 1, len(data)):
        if data[i][column] >= data[line][column]:
            down += 1
            break
        down += 1

    # Left
    for i in range(column - 1, -1, -1):
        if data[line][i] >= data[line][column]:
            left += 1
            break
        left += 1

    # Right
    for i in range(column + 1, len(data[0])):
        if data[line][i] >= data[line][column]:
            right += 1
            break
        right += 1

    return up * down * left * right


def sort_data(data):
    new_data = []
    for i in range(len(data)):
        new_data.append([eval(i) for i in data[i]])

    return new_data


if __name__ == '__main__':
    main()
