
requested_toppings = ['マッシュルーム', 'エクストラチーズ']

if 'マッシュルーム' in requested_toppings:
    print("マッシュルームを追加する。")
if 'ペパロニ' in requested_toppings:
    print("ペパロニを追加する。")
if 'エクストラチーズ' in requested_toppings:
    print("エクストラチーズを追加する。")

print("\nピザができました！")

print("/////////////////////////////////////////////")

if 'マッシュルーム' in requested_toppings:
    print("マッシュルームを追加する。")
elif 'ペパロニ' in requested_toppings:
    print("ペパロニを追加する。")
elif 'エクストラチーズ' in requested_toppings:
    print("エクストラチーズを追加する。")

print("\nピザができました！")


print("/////////////////////////////////////////////")

requested_toppings = ['マッシュルーム', 'ピーマン', 'エクストラチーズ']

for requested_topping in requested_toppings:
    if requested_topping == 'ピーマン':
        print("申し訳ありません。ピーマンは品切れです。")
    else:
        print(f"ピザに{requested_topping}を追加します。")

print("\nピザができました！")

print("/////////////////////////////////////////////")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"トッピングに{requested_topping}を追加します。")
    print("\nピザができました！")
else:
    print("プレーンピザでよろしいですか？")

print("/////////////////////////////////////////////")

available_toppings = ['マッシュルーム', 'オリーブ', 'ピーマン', 'ペパロニ', 'パイナップル', 'エクストラチーズ']
requested_toppings = ['マッシュルーム', 'フライドポテト', 'エクストラチーズ']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"ピザに{requested_topping}を追加します。")
    else:
        print(f"申し訳ありません。{requested_topping}はありません。")

print("\nピザができました！")


