def algorithm():
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()

    result = 0  # 총 그룹 수
    cnt = 0  # 현재 그룹에 포함된 모험가 수
    for i in data:
        cnt += 1
        if cnt >= i:  # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성
            result += 1  # 총 그룹 수 증가
            cnt = 0  # 현재 그룹에 포함된 모험가의 수 초기화

    print(result)
