
def make_pizza(*toppings):
    print(toppings)


make_pizza('ペパロニ')
make_pizza('マッシュルーム', 'ピーマン', 'エクストラチーズ')

print("//////////////////////////////////////////////////")

def make_pizza(*toppings):
    print('\n以下のトッピングのピザを作ります')
    for topping in toppings:
        print(f"- {topping}")

make_pizza('ペパロニ')
make_pizza('マッシュルーム', 'ピーマン', 'エクストラチーズ')

print("//////////////////////////////////////////////////")

def make_pizza(size, *toppings):
    print(f"\n{size}インチのピザを、以下のトッピングで作ります")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'ペパロニ')
make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')

