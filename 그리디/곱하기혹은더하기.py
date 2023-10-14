

def algorithm():
    S = list(map(int, input()))

    if len(S) == 0:
        print(0)
        return
    if len(S) == 1:
        print(S)
        return

    result = S[0]
    for num in S[1:]:
        if (result == 0 or result == 1 or num == 0 or num == 1):
            result += num
        else:
            result *= num

    return result
