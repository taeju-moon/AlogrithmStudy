

def algorithm():
    input__ = input("")
    steps = [[-1, -2], [1, -2],
             [2, -1], [2, 1],
             [1, 2], [-1, 2],
             [-2, 1], [-2, -1]]  # 갈 수 있는 경로의 경우의 수 col, row
    col: int = alphabet_to_number(input__[0])
    row: int = int(input__[1])
    cnt = 0
    for step in steps:
        if is_valid(col+step[0], row+step[1]):
            cnt += 1
    print(cnt)


def alphabet_to_number(alphabet):
    index__ = ["a", "b", "c", "d", "e", "f", "g", "h"].index(alphabet)
    return [1, 2, 3, 4, 5, 6, 7, 8][index__]


def number_to_alphabet(number):
    index__ = [1, 2, 3, 4, 5, 6, 7, 8].index(number)
    return ["a", "b", "c", "d", "e", "f", "g", "h"][index__]


def is_valid(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8


algorithm()
