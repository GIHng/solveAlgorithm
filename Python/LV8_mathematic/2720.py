
N = int(input())

exchange = [0] * 4
money = 0

for i in range(N):
    money = int(input())
    exchange[0] = money // 25
    money -= exchange[0] * 25

    exchange[1] = money // 10
    money -= exchange[1] * 10

    exchange[2] = money // 5
    money -= exchange[2] * 5

    exchange[3] = money
    money -= exchange[3]

    print(*exchange)

