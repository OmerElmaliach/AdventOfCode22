

def main():
    print(part_two())


def part_one():
    sum_chars = 0
    with open('22D3.txt', 'r') as file:
        data = file.read().splitlines()
        for item in data:
            current_char = ''
            comp_one, comp_two = item[:len(item[::2])], item[len(item[::2]):]
            for char in comp_one:
                if char in comp_two and char is not current_char:
                    current_char += char
                    if char.isupper():
                        sum_chars += ord(char) - 38
                    else:
                        sum_chars += ord(char) - 96

    return sum_chars


def part_two():
    sum_chars = 0
    with open('22D3.txt', 'r') as file:
        data = file.read().splitlines()
        for index in range(0, len(data), 3):
            current_char = ''
            for char in data[index]:
                if char in data[index + 1] and char in data[index + 2] and char is not current_char:
                    current_char += char
                    if char.isupper():
                        sum_chars += ord(char) - 38
                    else:
                        sum_chars += ord(char) - 96

    return sum_chars


if __name__ == '__main__':
    main()
