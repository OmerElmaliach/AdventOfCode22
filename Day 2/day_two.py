

def main():
    print(part_two())


def part_one():
    sum_score = 0
    with open('22D2.txt', 'r') as file:
        data = file.read().splitlines()
        for hand in data:
            sum_score += calculate_win_part_one(hand)

    return sum_score


def calculate_win_part_one(hand):
    """
    :param hand: The hand at play
    :return: Score of player
    """
    opponent_hand, player_hand = hand.split()[0], hand.split()[1]

    # Rock
    if player_hand == 'X' and opponent_hand == 'A':
        return 1 + 3
    elif player_hand == 'X' and opponent_hand == 'B':
        return 1 + 0
    elif player_hand == 'X' and opponent_hand == 'C':
        return 1 + 6

    # Paper
    elif player_hand == 'Y' and opponent_hand == 'A':
        return 2 + 6
    elif player_hand == 'Y' and opponent_hand == 'B':
        return 2 + 3
    elif player_hand == 'Y' and opponent_hand == 'C':
        return 2 + 0

    # Scissors
    elif player_hand == 'Z' and opponent_hand == 'A':
        return 3 + 0
    elif player_hand == 'Z' and opponent_hand == 'B':
        return 3 + 6
    elif player_hand == 'Z' and opponent_hand == 'C':
        return 3 + 3


def part_two():
    sum_score = 0
    with open('22D2.txt', 'r') as file:
        data = file.read().splitlines()
        for hand in data:
            sum_score += calculate_win_part_two(hand)

    return sum_score


def calculate_win_part_two(hand):
    """
    :param hand: The hand at play
    :return: Score of player
    """
    opponent_hand, player_hand = hand.split()[0], hand.split()[1]

    if player_hand == 'X':
        if opponent_hand == 'A':
            return 3 + 0
        elif opponent_hand == 'B':
            return 1 + 0
        elif opponent_hand == 'C':
            return 2 + 0

    if player_hand == 'Y':
        if opponent_hand == 'A':
            return 1 + 3
        elif opponent_hand == 'B':
            return 2 + 3
        elif opponent_hand == 'C':
            return 3 + 3

    if player_hand == 'Z':
        if opponent_hand == 'A':
            return 2 + 6
        elif opponent_hand == 'B':
            return 3 + 6
        elif opponent_hand == 'C':
            return 1 + 6


if __name__ == '__main__':
    main()
