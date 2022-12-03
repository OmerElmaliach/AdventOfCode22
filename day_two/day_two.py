

def main():
    print(part_one())


def part_one():
    sum_score = 0
    with open('22D2.txt', 'r') as file:
        data = file.read().splitlines()
        for hand in data:
            sum_score += calculate_win(hand)

    return sum_score


def calculate_win(hand):
    """
    :param hand: The battle at play
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


if __name__ == '__main__':
    main()
