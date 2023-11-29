
print("リストをソート ##########################")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'アウディ', '日産', 'すばる']
cars.sort()
print(cars)

print("一時的なソート ##########################")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('元のリスト')
print(cars)
print('\nソートされたリスト')
print(sorted(cars))
print('\n元のリストを再表示')
print(cars)

print("リストを逆順にする ##########################")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print("リストの長さ ##########################")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print( len(cars) )
