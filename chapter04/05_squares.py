
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print( min(digits) )
print( max(digits) )
print( sum(digits) )


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


# リスト内包表記
squares = [value ** 2 for value in range(1, 11)]
print(squares)
