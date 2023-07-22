while True:
    N = int(input())
    if N == -1:
        break
    l = []
    sum = 0
    if N % 2 == 0:
        for i in range(1, int(N / 2) + 1):
            if N % i == 0:
                l.append(i)
                sum = sum + i

        if sum == N:
            print(N, '=', end=' ')
            for i in l[0:-1]:
                print(i, end=' + ')
            print(l[-1])
        else:
            print(f'{N} is NOT perfect.')
    else:
        print(f'{N} is NOT perfect.')