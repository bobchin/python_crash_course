
age = 12

if age < 4:
    print("入場料金は0円です。")
elif age < 18:
    print("入場料金は2500円です。")
else:
    print("入場料金は4000円です。")


if age < 4:
    price = 0
elif age < 18:
    price = 2500
elif age < 65:
    price = 4000
else:
    price = 2000

print(f"入場料金は{price}円です。")
