def algorithm():
    input__: str = input()
    alphas = ""
    numbers = ""
    for letter in input__:
        if letter.isdigit():
            numbers += letter
        else:
            alphas += letter
    print(''.join(sorted(alphas)+sorted(numbers)))


algorithm()
