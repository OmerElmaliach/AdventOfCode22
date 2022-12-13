

def main():
    with open('22D6.txt', 'r') as file:
        data = file.read()
        print(get_start_of_marker(data, 4))  # Solution for part one
        print(get_start_of_marker(data, 14))  # Solution for part two


def get_start_of_marker(data, unique_chars):
    """
    Finds the index where the start of the message marker is located
    :param data: Input
    :param unique_chars: Length of characters to be checked
    :return: End index of set of unique characters
    """
    for i in range(len(data) - unique_chars - 1):
        sequence, count = data[i:i + unique_chars], 0
        for c in range(unique_chars):
            count += sequence.count(data[i + c])

        if count == unique_chars:
            return i + unique_chars

    return 0


if __name__ == '__main__':
    main()
