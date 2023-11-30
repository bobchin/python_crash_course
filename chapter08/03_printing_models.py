
def print_models(unprinted, copmpleted):
    """
    リストからなくなるまでデザインを3D印刷する
    各デザインは印刷後に、copmpleted に移動する
    """
    while unprinted:
        current = unprinted.pop()
        print(f"3D印刷中: {current}")
        copmpleted.append(current)

def show_completed_models(completeds):
    """3D印刷されたすべてのモデルの情報を出力する"""
    for completed in completeds:
        print(completed)

unprinted_models = ['iPhoneケース', 'ロボットのペンダント', '12面体']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)
print(unprinted_models)

print("//////////////////////////////////////////")

unprinted_models = ['iPhoneケース', 'ロボットのペンダント', '12面体']
completed_models = []

print_models(unprinted_models[:], completed_models)
show_completed_models(completed_models)
print(unprinted_models)
