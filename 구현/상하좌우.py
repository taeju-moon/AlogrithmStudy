def algorithm():
    # 동, 북, 서, 남
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    N = int(input(""))
    locationVectors = input("")
    currentX = 1
    currentY = 1
    for vector in locationVectors:
        if vector == "R" and validate(currentX + dx[0], currentY + dy[0], N):
            currentX += dx[0]
            currentY += dy[0]
        elif vector == "U" and validate(currentX + dx[1], currentY + dy[1], N):
            currentX += dx[1]
            currentY += dy[1]
        elif vector == "L" and validate(currentX + dx[2], currentY + dy[2], N):
            currentX += dx[2]
            currentY += dy[2]
        elif vector == "D" and validate(currentX + dx[3], currentY + dy[3], N):
            currentX += dx[3]
            currentY += dy[3]
    print(currentY, currentX)


def validate(x, y, N):
    return 1 <= x <= N and 1 <= y <= N


algorithm()
