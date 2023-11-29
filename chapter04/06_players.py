
# スライス
players = ['charlie', 'martina', 'michael', 'eli']
print(players[0:3])

print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])


# スライスのループ
players = ['charlie', 'martina', 'michael', 'florence', 'eli']
print("チームの最初の３人の選手です。")
for player in players[:3]:
    print(player.title())

