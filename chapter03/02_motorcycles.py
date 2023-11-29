
print("list ////////////////////////////////")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

print("追加 ////////////////////////////////")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

print("空から追加 ////////////////////////////////")

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print("挿入 ////////////////////////////////")

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

print("削除 ////////////////////////////////")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

print("スタック ////////////////////////////////")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

print("インデックス指定で取り出し ////////////////////////////////")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f'最初に手に入れたバイクは{first_owned.title()}です。')

print("値を指定して削除 ////////////////////////////////")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
