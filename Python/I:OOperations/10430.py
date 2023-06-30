A, B, C = map(int, input().split())  # split()을 통하여 여러 값을 받은 후 저장, map 통하여 전체 형변환

print((A + B) % C)
print((A % C) + (B % C) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
