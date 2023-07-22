while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break
    else:
        if A > B:
            print('multiple' if A % B == 0 else 'neither')
        else:
            print('factor' if B % A == 0 else 'neither')