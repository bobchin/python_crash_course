
# タプル
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# error
# dimensions[0] = 250

for dimension in dimensions:
    print(dimension)

# 上書き
dimensions = (200, 50)
print("元のサイズ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("変更したサイズ")
for dimension in dimensions:
    print(dimension)
