def algorithm():
    N = int(input())
    cnt = 0
    for i in range(0, N+1, 1):
        for j in range(0, 60, 1):
            for k in range(0, 60, 1):
                if "3" in str(i)+str(j)+str(k):
                    cnt += 1
    print(cnt)


algorithm()
