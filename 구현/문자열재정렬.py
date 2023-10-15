def algorithm():
    input__: str = input()
    alphas = ""
    number = 0
    for letter in input__:
        if letter.isdigit():
            number += int(letter)
        else:
            alphas += letter
    print(''.join(sorted(alphas)+[str(number)]))


algorithm()
